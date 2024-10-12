# AwsResourceAccessManager.DefaultApi

All URIs are relative to *http://ram.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acceptResourceShareInvitation**](DefaultApi.md#acceptResourceShareInvitation) | **POST** /acceptresourceshareinvitation | 
[**associateResourceShare**](DefaultApi.md#associateResourceShare) | **POST** /associateresourceshare | 
[**associateResourceSharePermission**](DefaultApi.md#associateResourceSharePermission) | **POST** /associateresourcesharepermission | 
[**createPermission**](DefaultApi.md#createPermission) | **POST** /createpermission | 
[**createPermissionVersion**](DefaultApi.md#createPermissionVersion) | **POST** /createpermissionversion | 
[**createResourceShare**](DefaultApi.md#createResourceShare) | **POST** /createresourceshare | 
[**deletePermission**](DefaultApi.md#deletePermission) | **DELETE** /deletepermission#permissionArn | 
[**deletePermissionVersion**](DefaultApi.md#deletePermissionVersion) | **DELETE** /deletepermissionversion#permissionArn&amp;permissionVersion | 
[**deleteResourceShare**](DefaultApi.md#deleteResourceShare) | **DELETE** /deleteresourceshare#resourceShareArn | 
[**disassociateResourceShare**](DefaultApi.md#disassociateResourceShare) | **POST** /disassociateresourceshare | 
[**disassociateResourceSharePermission**](DefaultApi.md#disassociateResourceSharePermission) | **POST** /disassociateresourcesharepermission | 
[**enableSharingWithAwsOrganization**](DefaultApi.md#enableSharingWithAwsOrganization) | **POST** /enablesharingwithawsorganization | 
[**getPermission**](DefaultApi.md#getPermission) | **POST** /getpermission | 
[**getResourcePolicies**](DefaultApi.md#getResourcePolicies) | **POST** /getresourcepolicies | 
[**getResourceShareAssociations**](DefaultApi.md#getResourceShareAssociations) | **POST** /getresourceshareassociations | 
[**getResourceShareInvitations**](DefaultApi.md#getResourceShareInvitations) | **POST** /getresourceshareinvitations | 
[**getResourceShares**](DefaultApi.md#getResourceShares) | **POST** /getresourceshares | 
[**listPendingInvitationResources**](DefaultApi.md#listPendingInvitationResources) | **POST** /listpendinginvitationresources | 
[**listPermissionAssociations**](DefaultApi.md#listPermissionAssociations) | **POST** /listpermissionassociations | 
[**listPermissionVersions**](DefaultApi.md#listPermissionVersions) | **POST** /listpermissionversions | 
[**listPermissions**](DefaultApi.md#listPermissions) | **POST** /listpermissions | 
[**listPrincipals**](DefaultApi.md#listPrincipals) | **POST** /listprincipals | 
[**listReplacePermissionAssociationsWork**](DefaultApi.md#listReplacePermissionAssociationsWork) | **POST** /listreplacepermissionassociationswork | 
[**listResourceSharePermissions**](DefaultApi.md#listResourceSharePermissions) | **POST** /listresourcesharepermissions | 
[**listResourceTypes**](DefaultApi.md#listResourceTypes) | **POST** /listresourcetypes | 
[**listResources**](DefaultApi.md#listResources) | **POST** /listresources | 
[**promotePermissionCreatedFromPolicy**](DefaultApi.md#promotePermissionCreatedFromPolicy) | **POST** /promotepermissioncreatedfrompolicy | 
[**promoteResourceShareCreatedFromPolicy**](DefaultApi.md#promoteResourceShareCreatedFromPolicy) | **POST** /promoteresourcesharecreatedfrompolicy#resourceShareArn | 
[**rejectResourceShareInvitation**](DefaultApi.md#rejectResourceShareInvitation) | **POST** /rejectresourceshareinvitation | 
[**replacePermissionAssociations**](DefaultApi.md#replacePermissionAssociations) | **POST** /replacepermissionassociations | 
[**setDefaultPermissionVersion**](DefaultApi.md#setDefaultPermissionVersion) | **POST** /setdefaultpermissionversion | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tagresource | 
[**untagResource**](DefaultApi.md#untagResource) | **POST** /untagresource | 
[**updateResourceShare**](DefaultApi.md#updateResourceShare) | **POST** /updateresourceshare | 



## acceptResourceShareInvitation

> AcceptResourceShareInvitationResponse acceptResourceShareInvitation(acceptResourceShareInvitationRequest, opts)



Accepts an invitation to a resource share from another Amazon Web Services account. After you accept the invitation, the resources included in the resource share are available to interact with in the relevant Amazon Web Services Management Consoles and tools.

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let acceptResourceShareInvitationRequest = new AwsResourceAccessManager.AcceptResourceShareInvitationRequest(); // AcceptResourceShareInvitationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.acceptResourceShareInvitation(acceptResourceShareInvitationRequest, opts, (error, data, response) => {
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
 **acceptResourceShareInvitationRequest** | [**AcceptResourceShareInvitationRequest**](AcceptResourceShareInvitationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AcceptResourceShareInvitationResponse**](AcceptResourceShareInvitationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## associateResourceShare

> AssociateResourceShareResponse associateResourceShare(associateResourceShareRequest, opts)



Adds the specified list of principals and list of resources to a resource share. Principals that already have access to this resource share immediately receive access to the added resources. Newly added principals immediately receive access to the resources shared in this resource share. 

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let associateResourceShareRequest = new AwsResourceAccessManager.AssociateResourceShareRequest(); // AssociateResourceShareRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateResourceShare(associateResourceShareRequest, opts, (error, data, response) => {
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
 **associateResourceShareRequest** | [**AssociateResourceShareRequest**](AssociateResourceShareRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AssociateResourceShareResponse**](AssociateResourceShareResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## associateResourceSharePermission

> AssociateResourceSharePermissionResponse associateResourceSharePermission(associateResourceSharePermissionRequest, opts)



Adds or replaces the RAM permission for a resource type included in a resource share. You can have exactly one permission associated with each resource type in the resource share. You can add a new RAM permission only if there are currently no resources of that resource type currently in the resource share.

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let associateResourceSharePermissionRequest = new AwsResourceAccessManager.AssociateResourceSharePermissionRequest(); // AssociateResourceSharePermissionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateResourceSharePermission(associateResourceSharePermissionRequest, opts, (error, data, response) => {
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
 **associateResourceSharePermissionRequest** | [**AssociateResourceSharePermissionRequest**](AssociateResourceSharePermissionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AssociateResourceSharePermissionResponse**](AssociateResourceSharePermissionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPermission

> CreatePermissionResponse createPermission(createPermissionRequest, opts)



Creates a customer managed permission for a specified resource type that you can attach to resource shares. It is created in the Amazon Web Services Region in which you call the operation.

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let createPermissionRequest = new AwsResourceAccessManager.CreatePermissionRequest(); // CreatePermissionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createPermission(createPermissionRequest, opts, (error, data, response) => {
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
 **createPermissionRequest** | [**CreatePermissionRequest**](CreatePermissionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreatePermissionResponse**](CreatePermissionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPermissionVersion

> CreatePermissionVersionResponse createPermissionVersion(createPermissionVersionRequest, opts)



&lt;p&gt;Creates a new version of the specified customer managed permission. The new version is automatically set as the default version of the customer managed permission. New resource shares automatically use the default permission. Existing resource shares continue to use their original permission versions, but you can use &lt;a&gt;ReplacePermissionAssociations&lt;/a&gt; to update them.&lt;/p&gt; &lt;p&gt;If the specified customer managed permission already has the maximum of 5 versions, then you must delete one of the existing versions before you can create a new one.&lt;/p&gt;

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let createPermissionVersionRequest = new AwsResourceAccessManager.CreatePermissionVersionRequest(); // CreatePermissionVersionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createPermissionVersion(createPermissionVersionRequest, opts, (error, data, response) => {
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
 **createPermissionVersionRequest** | [**CreatePermissionVersionRequest**](CreatePermissionVersionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreatePermissionVersionResponse**](CreatePermissionVersionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createResourceShare

> CreateResourceShareResponse createResourceShare(createResourceShareRequest, opts)



&lt;p&gt;Creates a resource share. You can provide a list of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Names (ARNs)&lt;/a&gt; for the resources that you want to share, a list of principals you want to share the resources with, and the permissions to grant those principals.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Sharing a resource makes it available for use by principals outside of the Amazon Web Services account that created the resource. Sharing doesn&#39;t change any permissions or quotas that apply to the resource in the account that created it.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let createResourceShareRequest = new AwsResourceAccessManager.CreateResourceShareRequest(); // CreateResourceShareRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createResourceShare(createResourceShareRequest, opts, (error, data, response) => {
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
 **createResourceShareRequest** | [**CreateResourceShareRequest**](CreateResourceShareRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateResourceShareResponse**](CreateResourceShareResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deletePermission

> DeletePermissionResponse deletePermission(permissionArn, opts)



Deletes the specified customer managed permission in the Amazon Web Services Region in which you call this operation. You can delete a customer managed permission only if it isn&#39;t attached to any resource share. The operation deletes all versions associated with the customer managed permission.

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let permissionArn = "permissionArn_example"; // String | Specifies the <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Name (ARN)</a> of the customer managed permission that you want to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'clientToken': "clientToken_example" // String | <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href=\"https://wikipedia.org/wiki/Universally_unique_identifier\">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>
};
apiInstance.deletePermission(permissionArn, opts, (error, data, response) => {
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
 **permissionArn** | **String**| Specifies the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Name (ARN)&lt;/a&gt; of the customer managed permission that you want to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **clientToken** | **String**| &lt;p&gt;Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a &lt;a href&#x3D;\&quot;https://wikipedia.org/wiki/Universally_unique_identifier\&quot;&gt;UUID type of value.&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you don&#39;t provide this value, then Amazon Web Services generates a random one for you.&lt;/p&gt; &lt;p&gt;If you retry the operation with the same &lt;code&gt;ClientToken&lt;/code&gt;, but with different parameters, the retry fails with an &lt;code&gt;IdempotentParameterMismatch&lt;/code&gt; error.&lt;/p&gt; | [optional] 

### Return type

[**DeletePermissionResponse**](DeletePermissionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deletePermissionVersion

> DeletePermissionVersionResponse deletePermissionVersion(permissionArn, permissionVersion, opts)



&lt;p&gt;Deletes one version of a customer managed permission. The version you specify must not be attached to any resource share and must not be the default version for the permission.&lt;/p&gt; &lt;p&gt;If a customer managed permission has the maximum of 5 versions, then you must delete at least one version before you can create another.&lt;/p&gt;

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let permissionArn = "permissionArn_example"; // String | Specifies the <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Name (ARN)</a> of the permission with the version you want to delete.
let permissionVersion = 56; // Number | <p>Specifies the version number to delete.</p> <p>You can't delete the default version for a customer managed permission.</p> <p>You can't delete a version if it's the only version of the permission. You must either first create another version, or delete the permission completely.</p> <p>You can't delete a version if it is attached to any resource shares. If the version is the default, you must first use <a>SetDefaultPermissionVersion</a> to set a different version as the default for the customer managed permission, and then use <a>AssociateResourceSharePermission</a> to update your resource shares to use the new default version.</p>
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'clientToken': "clientToken_example" // String | <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href=\"https://wikipedia.org/wiki/Universally_unique_identifier\">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>
};
apiInstance.deletePermissionVersion(permissionArn, permissionVersion, opts, (error, data, response) => {
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
 **permissionArn** | **String**| Specifies the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Name (ARN)&lt;/a&gt; of the permission with the version you want to delete. | 
 **permissionVersion** | **Number**| &lt;p&gt;Specifies the version number to delete.&lt;/p&gt; &lt;p&gt;You can&#39;t delete the default version for a customer managed permission.&lt;/p&gt; &lt;p&gt;You can&#39;t delete a version if it&#39;s the only version of the permission. You must either first create another version, or delete the permission completely.&lt;/p&gt; &lt;p&gt;You can&#39;t delete a version if it is attached to any resource shares. If the version is the default, you must first use &lt;a&gt;SetDefaultPermissionVersion&lt;/a&gt; to set a different version as the default for the customer managed permission, and then use &lt;a&gt;AssociateResourceSharePermission&lt;/a&gt; to update your resource shares to use the new default version.&lt;/p&gt; | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **clientToken** | **String**| &lt;p&gt;Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a &lt;a href&#x3D;\&quot;https://wikipedia.org/wiki/Universally_unique_identifier\&quot;&gt;UUID type of value.&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you don&#39;t provide this value, then Amazon Web Services generates a random one for you.&lt;/p&gt; &lt;p&gt;If you retry the operation with the same &lt;code&gt;ClientToken&lt;/code&gt;, but with different parameters, the retry fails with an &lt;code&gt;IdempotentParameterMismatch&lt;/code&gt; error.&lt;/p&gt; | [optional] 

### Return type

[**DeletePermissionVersionResponse**](DeletePermissionVersionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteResourceShare

> DeleteResourceShareResponse deleteResourceShare(resourceShareArn, opts)



&lt;p&gt;Deletes the specified resource share.&lt;/p&gt; &lt;important&gt; &lt;p&gt;This doesn&#39;t delete any of the resources that were associated with the resource share; it only stops the sharing of those resources through this resource share.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let resourceShareArn = "resourceShareArn_example"; // String | Specifies the <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Name (ARN)</a> of the resource share to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'clientToken': "clientToken_example" // String | <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href=\"https://wikipedia.org/wiki/Universally_unique_identifier\">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>
};
apiInstance.deleteResourceShare(resourceShareArn, opts, (error, data, response) => {
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
 **resourceShareArn** | **String**| Specifies the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Name (ARN)&lt;/a&gt; of the resource share to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **clientToken** | **String**| &lt;p&gt;Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a &lt;a href&#x3D;\&quot;https://wikipedia.org/wiki/Universally_unique_identifier\&quot;&gt;UUID type of value.&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you don&#39;t provide this value, then Amazon Web Services generates a random one for you.&lt;/p&gt; &lt;p&gt;If you retry the operation with the same &lt;code&gt;ClientToken&lt;/code&gt;, but with different parameters, the retry fails with an &lt;code&gt;IdempotentParameterMismatch&lt;/code&gt; error.&lt;/p&gt; | [optional] 

### Return type

[**DeleteResourceShareResponse**](DeleteResourceShareResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disassociateResourceShare

> DisassociateResourceShareResponse disassociateResourceShare(disassociateResourceShareRequest, opts)



Removes the specified principals or resources from participating in the specified resource share.

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let disassociateResourceShareRequest = new AwsResourceAccessManager.DisassociateResourceShareRequest(); // DisassociateResourceShareRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateResourceShare(disassociateResourceShareRequest, opts, (error, data, response) => {
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
 **disassociateResourceShareRequest** | [**DisassociateResourceShareRequest**](DisassociateResourceShareRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DisassociateResourceShareResponse**](DisassociateResourceShareResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## disassociateResourceSharePermission

> DisassociateResourceSharePermissionResponse disassociateResourceSharePermission(disassociateResourceSharePermissionRequest, opts)



Removes a managed permission from a resource share. Permission changes take effect immediately. You can remove a managed permission from a resource share only if there are currently no resources of the relevant resource type currently attached to the resource share.

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let disassociateResourceSharePermissionRequest = new AwsResourceAccessManager.DisassociateResourceSharePermissionRequest(); // DisassociateResourceSharePermissionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateResourceSharePermission(disassociateResourceSharePermissionRequest, opts, (error, data, response) => {
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
 **disassociateResourceSharePermissionRequest** | [**DisassociateResourceSharePermissionRequest**](DisassociateResourceSharePermissionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DisassociateResourceSharePermissionResponse**](DisassociateResourceSharePermissionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## enableSharingWithAwsOrganization

> EnableSharingWithAwsOrganizationResponse enableSharingWithAwsOrganization(opts)



&lt;p&gt;Enables resource sharing within your organization in Organizations. This operation creates a service-linked role called &lt;code&gt;AWSServiceRoleForResourceAccessManager&lt;/code&gt; that has the IAM managed policy named AWSResourceAccessManagerServiceRolePolicy attached. This role permits RAM to retrieve information about the organization and its structure. This lets you share resources with all of the accounts in the calling account&#39;s organization by specifying the organization ID, or all of the accounts in an organizational unit (OU) by specifying the OU ID. Until you enable sharing within the organization, you can specify only individual Amazon Web Services accounts, or for supported resource types, IAM roles and users.&lt;/p&gt; &lt;p&gt;You must call this operation from an IAM role or user in the organization&#39;s management account.&lt;/p&gt; &lt;p/&gt;

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.enableSharingWithAwsOrganization(opts, (error, data, response) => {
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

[**EnableSharingWithAwsOrganizationResponse**](EnableSharingWithAwsOrganizationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPermission

> GetPermissionResponse getPermission(getPermissionRequest, opts)



Retrieves the contents of a managed permission in JSON format.

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let getPermissionRequest = new AwsResourceAccessManager.GetPermissionRequest(); // GetPermissionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getPermission(getPermissionRequest, opts, (error, data, response) => {
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
 **getPermissionRequest** | [**GetPermissionRequest**](GetPermissionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetPermissionResponse**](GetPermissionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getResourcePolicies

> GetResourcePoliciesResponse getResourcePolicies(getResourcePoliciesRequest, opts)



Retrieves the resource policies for the specified resources that you own and have shared.

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let getResourcePoliciesRequest = new AwsResourceAccessManager.GetResourcePoliciesRequest(); // GetResourcePoliciesRequest | 
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
apiInstance.getResourcePolicies(getResourcePoliciesRequest, opts, (error, data, response) => {
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
 **getResourcePoliciesRequest** | [**GetResourcePoliciesRequest**](GetResourcePoliciesRequest.md)|  | 
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

[**GetResourcePoliciesResponse**](GetResourcePoliciesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getResourceShareAssociations

> GetResourceShareAssociationsResponse getResourceShareAssociations(getResourceShareAssociationsRequest, opts)



Retrieves the lists of resources and principals that associated for resource shares that you own.

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let getResourceShareAssociationsRequest = new AwsResourceAccessManager.GetResourceShareAssociationsRequest(); // GetResourceShareAssociationsRequest | 
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
apiInstance.getResourceShareAssociations(getResourceShareAssociationsRequest, opts, (error, data, response) => {
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
 **getResourceShareAssociationsRequest** | [**GetResourceShareAssociationsRequest**](GetResourceShareAssociationsRequest.md)|  | 
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

[**GetResourceShareAssociationsResponse**](GetResourceShareAssociationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getResourceShareInvitations

> GetResourceShareInvitationsResponse getResourceShareInvitations(getResourceShareInvitationsRequest, opts)



Retrieves details about invitations that you have received for resource shares.

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let getResourceShareInvitationsRequest = new AwsResourceAccessManager.GetResourceShareInvitationsRequest(); // GetResourceShareInvitationsRequest | 
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
apiInstance.getResourceShareInvitations(getResourceShareInvitationsRequest, opts, (error, data, response) => {
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
 **getResourceShareInvitationsRequest** | [**GetResourceShareInvitationsRequest**](GetResourceShareInvitationsRequest.md)|  | 
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

[**GetResourceShareInvitationsResponse**](GetResourceShareInvitationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getResourceShares

> GetResourceSharesResponse getResourceShares(getResourceSharesRequest, opts)



Retrieves details about the resource shares that you own or that are shared with you.

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let getResourceSharesRequest = new AwsResourceAccessManager.GetResourceSharesRequest(); // GetResourceSharesRequest | 
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
apiInstance.getResourceShares(getResourceSharesRequest, opts, (error, data, response) => {
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
 **getResourceSharesRequest** | [**GetResourceSharesRequest**](GetResourceSharesRequest.md)|  | 
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

[**GetResourceSharesResponse**](GetResourceSharesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listPendingInvitationResources

> ListPendingInvitationResourcesResponse listPendingInvitationResources(listPendingInvitationResourcesRequest, opts)



Lists the resources in a resource share that is shared with you but for which the invitation is still &lt;code&gt;PENDING&lt;/code&gt;. That means that you haven&#39;t accepted or rejected the invitation and the invitation hasn&#39;t expired.

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let listPendingInvitationResourcesRequest = new AwsResourceAccessManager.ListPendingInvitationResourcesRequest(); // ListPendingInvitationResourcesRequest | 
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
apiInstance.listPendingInvitationResources(listPendingInvitationResourcesRequest, opts, (error, data, response) => {
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
 **listPendingInvitationResourcesRequest** | [**ListPendingInvitationResourcesRequest**](ListPendingInvitationResourcesRequest.md)|  | 
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

[**ListPendingInvitationResourcesResponse**](ListPendingInvitationResourcesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listPermissionAssociations

> ListPermissionAssociationsResponse listPermissionAssociations(listPermissionAssociationsRequest, opts)



Lists information about the managed permission and its associations to any resource shares that use this managed permission. This lets you see which resource shares use which versions of the specified managed permission.

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let listPermissionAssociationsRequest = new AwsResourceAccessManager.ListPermissionAssociationsRequest(); // ListPermissionAssociationsRequest | 
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
apiInstance.listPermissionAssociations(listPermissionAssociationsRequest, opts, (error, data, response) => {
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
 **listPermissionAssociationsRequest** | [**ListPermissionAssociationsRequest**](ListPermissionAssociationsRequest.md)|  | 
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

[**ListPermissionAssociationsResponse**](ListPermissionAssociationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listPermissionVersions

> ListPermissionVersionsResponse listPermissionVersions(listPermissionVersionsRequest, opts)



Lists the available versions of the specified RAM permission.

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let listPermissionVersionsRequest = new AwsResourceAccessManager.ListPermissionVersionsRequest(); // ListPermissionVersionsRequest | 
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
apiInstance.listPermissionVersions(listPermissionVersionsRequest, opts, (error, data, response) => {
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
 **listPermissionVersionsRequest** | [**ListPermissionVersionsRequest**](ListPermissionVersionsRequest.md)|  | 
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

[**ListPermissionVersionsResponse**](ListPermissionVersionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listPermissions

> ListPermissionsResponse listPermissions(listPermissionsRequest, opts)



Retrieves a list of available RAM permissions that you can use for the supported resource types. 

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let listPermissionsRequest = new AwsResourceAccessManager.ListPermissionsRequest(); // ListPermissionsRequest | 
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
apiInstance.listPermissions(listPermissionsRequest, opts, (error, data, response) => {
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
 **listPermissionsRequest** | [**ListPermissionsRequest**](ListPermissionsRequest.md)|  | 
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

[**ListPermissionsResponse**](ListPermissionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listPrincipals

> ListPrincipalsResponse listPrincipals(listPrincipalsRequest, opts)



Lists the principals that you are sharing resources with or that are sharing resources with you.

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let listPrincipalsRequest = new AwsResourceAccessManager.ListPrincipalsRequest(); // ListPrincipalsRequest | 
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
apiInstance.listPrincipals(listPrincipalsRequest, opts, (error, data, response) => {
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
 **listPrincipalsRequest** | [**ListPrincipalsRequest**](ListPrincipalsRequest.md)|  | 
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

[**ListPrincipalsResponse**](ListPrincipalsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listReplacePermissionAssociationsWork

> ListReplacePermissionAssociationsWorkResponse listReplacePermissionAssociationsWork(listReplacePermissionAssociationsWorkRequest, opts)



Retrieves the current status of the asynchronous tasks performed by RAM when you perform the &lt;a&gt;ReplacePermissionAssociationsWork&lt;/a&gt; operation.

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let listReplacePermissionAssociationsWorkRequest = new AwsResourceAccessManager.ListReplacePermissionAssociationsWorkRequest(); // ListReplacePermissionAssociationsWorkRequest | 
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
apiInstance.listReplacePermissionAssociationsWork(listReplacePermissionAssociationsWorkRequest, opts, (error, data, response) => {
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
 **listReplacePermissionAssociationsWorkRequest** | [**ListReplacePermissionAssociationsWorkRequest**](ListReplacePermissionAssociationsWorkRequest.md)|  | 
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

[**ListReplacePermissionAssociationsWorkResponse**](ListReplacePermissionAssociationsWorkResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listResourceSharePermissions

> ListResourceSharePermissionsResponse listResourceSharePermissions(listResourceSharePermissionsRequest, opts)



Lists the RAM permissions that are associated with a resource share.

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let listResourceSharePermissionsRequest = new AwsResourceAccessManager.ListResourceSharePermissionsRequest(); // ListResourceSharePermissionsRequest | 
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
apiInstance.listResourceSharePermissions(listResourceSharePermissionsRequest, opts, (error, data, response) => {
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
 **listResourceSharePermissionsRequest** | [**ListResourceSharePermissionsRequest**](ListResourceSharePermissionsRequest.md)|  | 
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

[**ListResourceSharePermissionsResponse**](ListResourceSharePermissionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listResourceTypes

> ListResourceTypesResponse listResourceTypes(listResourceTypesRequest, opts)



Lists the resource types that can be shared by RAM.

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let listResourceTypesRequest = new AwsResourceAccessManager.ListResourceTypesRequest(); // ListResourceTypesRequest | 
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
apiInstance.listResourceTypes(listResourceTypesRequest, opts, (error, data, response) => {
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
 **listResourceTypesRequest** | [**ListResourceTypesRequest**](ListResourceTypesRequest.md)|  | 
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

[**ListResourceTypesResponse**](ListResourceTypesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listResources

> ListResourcesResponse listResources(listResourcesRequest, opts)



Lists the resources that you added to a resource share or the resources that are shared with you.

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let listResourcesRequest = new AwsResourceAccessManager.ListResourcesRequest(); // ListResourcesRequest | 
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
apiInstance.listResources(listResourcesRequest, opts, (error, data, response) => {
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
 **listResourcesRequest** | [**ListResourcesRequest**](ListResourcesRequest.md)|  | 
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

[**ListResourcesResponse**](ListResourcesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## promotePermissionCreatedFromPolicy

> PromotePermissionCreatedFromPolicyResponse promotePermissionCreatedFromPolicy(promotePermissionCreatedFromPolicyRequest, opts)



&lt;p&gt;When you attach a resource-based policy to a resource, RAM automatically creates a resource share of &lt;code&gt;featureSet&lt;/code&gt;&#x3D;&lt;code&gt;CREATED_FROM_POLICY&lt;/code&gt; with a managed permission that has the same IAM permissions as the original resource-based policy. However, this type of managed permission is visible to only the resource share owner, and the associated resource share can&#39;t be modified by using RAM.&lt;/p&gt; &lt;p&gt;This operation creates a separate, fully manageable customer managed permission that has the same IAM permissions as the original resource-based policy. You can associate this customer managed permission to any resource shares.&lt;/p&gt; &lt;p&gt;Before you use &lt;a&gt;PromoteResourceShareCreatedFromPolicy&lt;/a&gt;, you should first run this operation to ensure that you have an appropriate customer managed permission that can be associated with the promoted resource share.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The original &lt;code&gt;CREATED_FROM_POLICY&lt;/code&gt; policy isn&#39;t deleted, and resource shares using that original policy aren&#39;t automatically updated.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You can&#39;t modify a &lt;code&gt;CREATED_FROM_POLICY&lt;/code&gt; resource share so you can&#39;t associate the new customer managed permission by using &lt;code&gt;ReplacePermsissionAssociations&lt;/code&gt;. However, if you use &lt;a&gt;PromoteResourceShareCreatedFromPolicy&lt;/a&gt;, that operation automatically associates the fully manageable customer managed permission to the newly promoted &lt;code&gt;STANDARD&lt;/code&gt; resource share.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;After you promote a resource share, if the original &lt;code&gt;CREATED_FROM_POLICY&lt;/code&gt; managed permission has no other associations to A resource share, then RAM automatically deletes it.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let promotePermissionCreatedFromPolicyRequest = new AwsResourceAccessManager.PromotePermissionCreatedFromPolicyRequest(); // PromotePermissionCreatedFromPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.promotePermissionCreatedFromPolicy(promotePermissionCreatedFromPolicyRequest, opts, (error, data, response) => {
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
 **promotePermissionCreatedFromPolicyRequest** | [**PromotePermissionCreatedFromPolicyRequest**](PromotePermissionCreatedFromPolicyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PromotePermissionCreatedFromPolicyResponse**](PromotePermissionCreatedFromPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## promoteResourceShareCreatedFromPolicy

> PromoteResourceShareCreatedFromPolicyResponse promoteResourceShareCreatedFromPolicy(resourceShareArn, opts)



&lt;p&gt;When you attach a resource-based policy to a resource, RAM automatically creates a resource share of &lt;code&gt;featureSet&lt;/code&gt;&#x3D;&lt;code&gt;CREATED_FROM_POLICY&lt;/code&gt; with a managed permission that has the same IAM permissions as the original resource-based policy. However, this type of managed permission is visible to only the resource share owner, and the associated resource share can&#39;t be modified by using RAM.&lt;/p&gt; &lt;p&gt;This operation promotes the resource share to a &lt;code&gt;STANDARD&lt;/code&gt; resource share that is fully manageable in RAM. When you promote a resource share, you can then manage the resource share in RAM and it becomes visible to all of the principals you shared it with.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Before you perform this operation, you should first run &lt;a&gt;PromotePermissionCreatedFromPolicy&lt;/a&gt;to ensure that you have an appropriate customer managed permission that can be associated with this resource share after its is promoted. If this operation can&#39;t find a managed permission that exactly matches the existing &lt;code&gt;CREATED_FROM_POLICY&lt;/code&gt; permission, then this operation fails.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let resourceShareArn = "resourceShareArn_example"; // String | Specifies the <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Name (ARN)</a> of the resource share to promote.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.promoteResourceShareCreatedFromPolicy(resourceShareArn, opts, (error, data, response) => {
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
 **resourceShareArn** | **String**| Specifies the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Name (ARN)&lt;/a&gt; of the resource share to promote. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PromoteResourceShareCreatedFromPolicyResponse**](PromoteResourceShareCreatedFromPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rejectResourceShareInvitation

> RejectResourceShareInvitationResponse rejectResourceShareInvitation(rejectResourceShareInvitationRequest, opts)



Rejects an invitation to a resource share from another Amazon Web Services account.

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let rejectResourceShareInvitationRequest = new AwsResourceAccessManager.RejectResourceShareInvitationRequest(); // RejectResourceShareInvitationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.rejectResourceShareInvitation(rejectResourceShareInvitationRequest, opts, (error, data, response) => {
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
 **rejectResourceShareInvitationRequest** | [**RejectResourceShareInvitationRequest**](RejectResourceShareInvitationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RejectResourceShareInvitationResponse**](RejectResourceShareInvitationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## replacePermissionAssociations

> ReplacePermissionAssociationsResponse replacePermissionAssociations(replacePermissionAssociationsRequest, opts)



&lt;p&gt;Updates all resource shares that use a managed permission to a different managed permission. This operation always applies the default version of the target managed permission. You can optionally specify that the update applies to only resource shares that currently use a specified version. This enables you to update to the latest version, without changing the which managed permission is used.&lt;/p&gt; &lt;p&gt;You can use this operation to update all of your resource shares to use the current default version of the permission by specifying the same value for the &lt;code&gt;fromPermissionArn&lt;/code&gt; and &lt;code&gt;toPermissionArn&lt;/code&gt; parameters.&lt;/p&gt; &lt;p&gt;You can use the optional &lt;code&gt;fromPermissionVersion&lt;/code&gt; parameter to update only those resources that use a specified version of the managed permission to the new managed permission.&lt;/p&gt; &lt;important&gt; &lt;p&gt;To successfully perform this operation, you must have permission to update the resource-based policy on all affected resource types.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let replacePermissionAssociationsRequest = new AwsResourceAccessManager.ReplacePermissionAssociationsRequest(); // ReplacePermissionAssociationsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.replacePermissionAssociations(replacePermissionAssociationsRequest, opts, (error, data, response) => {
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
 **replacePermissionAssociationsRequest** | [**ReplacePermissionAssociationsRequest**](ReplacePermissionAssociationsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ReplacePermissionAssociationsResponse**](ReplacePermissionAssociationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setDefaultPermissionVersion

> SetDefaultPermissionVersionResponse setDefaultPermissionVersion(setDefaultPermissionVersionRequest, opts)



Designates the specified version number as the default version for the specified customer managed permission. New resource shares automatically use this new default permission. Existing resource shares continue to use their original permission version, but you can use &lt;a&gt;ReplacePermissionAssociations&lt;/a&gt; to update them.

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let setDefaultPermissionVersionRequest = new AwsResourceAccessManager.SetDefaultPermissionVersionRequest(); // SetDefaultPermissionVersionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.setDefaultPermissionVersion(setDefaultPermissionVersionRequest, opts, (error, data, response) => {
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
 **setDefaultPermissionVersionRequest** | [**SetDefaultPermissionVersionRequest**](SetDefaultPermissionVersionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**SetDefaultPermissionVersionResponse**](SetDefaultPermissionVersionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(tagResourceRequest, opts)



&lt;p&gt;Adds the specified tag keys and values to a resource share or managed permission. If you choose a resource share, the tags are attached to only the resource share, not to the resources that are in the resource share.&lt;/p&gt; &lt;p&gt;The tags on a managed permission are the same for all versions of the managed permission.&lt;/p&gt;

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let tagResourceRequest = new AwsResourceAccessManager.TagResourceRequest(); // TagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(tagResourceRequest, opts, (error, data, response) => {
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

> Object untagResource(untagResourceRequest, opts)



Removes the specified tag key and value pairs from the specified resource share or managed permission.

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let untagResourceRequest = new AwsResourceAccessManager.UntagResourceRequest(); // UntagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(untagResourceRequest, opts, (error, data, response) => {
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


## updateResourceShare

> UpdateResourceShareResponse updateResourceShare(updateResourceShareRequest, opts)



Modifies some of the properties of the specified resource share.

### Example

```javascript
import AwsResourceAccessManager from 'aws_resource_access_manager';
let defaultClient = AwsResourceAccessManager.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsResourceAccessManager.DefaultApi();
let updateResourceShareRequest = new AwsResourceAccessManager.UpdateResourceShareRequest(); // UpdateResourceShareRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateResourceShare(updateResourceShareRequest, opts, (error, data, response) => {
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
 **updateResourceShareRequest** | [**UpdateResourceShareRequest**](UpdateResourceShareRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateResourceShareResponse**](UpdateResourceShareResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

