# AmazonVerifiedPermissions.DefaultApi

All URIs are relative to *http://verifiedpermissions.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createIdentitySource**](DefaultApi.md#createIdentitySource) | **POST** /#X-Amz-Target&#x3D;VerifiedPermissions.CreateIdentitySource | 
[**createPolicy**](DefaultApi.md#createPolicy) | **POST** /#X-Amz-Target&#x3D;VerifiedPermissions.CreatePolicy | 
[**createPolicyStore**](DefaultApi.md#createPolicyStore) | **POST** /#X-Amz-Target&#x3D;VerifiedPermissions.CreatePolicyStore | 
[**createPolicyTemplate**](DefaultApi.md#createPolicyTemplate) | **POST** /#X-Amz-Target&#x3D;VerifiedPermissions.CreatePolicyTemplate | 
[**deleteIdentitySource**](DefaultApi.md#deleteIdentitySource) | **POST** /#X-Amz-Target&#x3D;VerifiedPermissions.DeleteIdentitySource | 
[**deletePolicy**](DefaultApi.md#deletePolicy) | **POST** /#X-Amz-Target&#x3D;VerifiedPermissions.DeletePolicy | 
[**deletePolicyStore**](DefaultApi.md#deletePolicyStore) | **POST** /#X-Amz-Target&#x3D;VerifiedPermissions.DeletePolicyStore | 
[**deletePolicyTemplate**](DefaultApi.md#deletePolicyTemplate) | **POST** /#X-Amz-Target&#x3D;VerifiedPermissions.DeletePolicyTemplate | 
[**getIdentitySource**](DefaultApi.md#getIdentitySource) | **POST** /#X-Amz-Target&#x3D;VerifiedPermissions.GetIdentitySource | 
[**getPolicy**](DefaultApi.md#getPolicy) | **POST** /#X-Amz-Target&#x3D;VerifiedPermissions.GetPolicy | 
[**getPolicyStore**](DefaultApi.md#getPolicyStore) | **POST** /#X-Amz-Target&#x3D;VerifiedPermissions.GetPolicyStore | 
[**getPolicyTemplate**](DefaultApi.md#getPolicyTemplate) | **POST** /#X-Amz-Target&#x3D;VerifiedPermissions.GetPolicyTemplate | 
[**getSchema**](DefaultApi.md#getSchema) | **POST** /#X-Amz-Target&#x3D;VerifiedPermissions.GetSchema | 
[**isAuthorized**](DefaultApi.md#isAuthorized) | **POST** /#X-Amz-Target&#x3D;VerifiedPermissions.IsAuthorized | 
[**isAuthorizedWithToken**](DefaultApi.md#isAuthorizedWithToken) | **POST** /#X-Amz-Target&#x3D;VerifiedPermissions.IsAuthorizedWithToken | 
[**listIdentitySources**](DefaultApi.md#listIdentitySources) | **POST** /#X-Amz-Target&#x3D;VerifiedPermissions.ListIdentitySources | 
[**listPolicies**](DefaultApi.md#listPolicies) | **POST** /#X-Amz-Target&#x3D;VerifiedPermissions.ListPolicies | 
[**listPolicyStores**](DefaultApi.md#listPolicyStores) | **POST** /#X-Amz-Target&#x3D;VerifiedPermissions.ListPolicyStores | 
[**listPolicyTemplates**](DefaultApi.md#listPolicyTemplates) | **POST** /#X-Amz-Target&#x3D;VerifiedPermissions.ListPolicyTemplates | 
[**putSchema**](DefaultApi.md#putSchema) | **POST** /#X-Amz-Target&#x3D;VerifiedPermissions.PutSchema | 
[**updateIdentitySource**](DefaultApi.md#updateIdentitySource) | **POST** /#X-Amz-Target&#x3D;VerifiedPermissions.UpdateIdentitySource | 
[**updatePolicy**](DefaultApi.md#updatePolicy) | **POST** /#X-Amz-Target&#x3D;VerifiedPermissions.UpdatePolicy | 
[**updatePolicyStore**](DefaultApi.md#updatePolicyStore) | **POST** /#X-Amz-Target&#x3D;VerifiedPermissions.UpdatePolicyStore | 
[**updatePolicyTemplate**](DefaultApi.md#updatePolicyTemplate) | **POST** /#X-Amz-Target&#x3D;VerifiedPermissions.UpdatePolicyTemplate | 



## createIdentitySource

> CreateIdentitySourceOutput createIdentitySource(xAmzTarget, createIdentitySourceInput, opts)



&lt;p&gt;Creates a reference to an Amazon Cognito user pool as an external identity provider (IdP). &lt;/p&gt; &lt;p&gt;After you create an identity source, you can use the identities provided by the IdP as proxies for the principal in authorization queries that use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html\&quot;&gt;IsAuthorizedWithToken&lt;/a&gt; operation. These identities take the form of tokens that contain claims about the user, such as IDs, attributes and group memberships. Amazon Cognito provides both identity tokens and access tokens, and Verified Permissions can use either or both. Any combination of identity and access tokens results in the same Cedar principal. Verified Permissions automatically translates the information about the identities into the standard Cedar attributes that can be evaluated by your policies. Because the Amazon Cognito identity and access tokens can contain different information, the tokens you choose to use determine which principal attributes are available to access when evaluating Cedar policies.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If you delete a Amazon Cognito user pool or user, tokens from that deleted pool or that deleted user continue to be usable until they expire.&lt;/p&gt; &lt;/important&gt; &lt;note&gt; &lt;p&gt;To reference a user from this identity source in your Cedar policies, use the following syntax.&lt;/p&gt; &lt;p&gt; &lt;i&gt;IdentityType::\&quot;&amp;lt;CognitoUserPoolIdentifier&amp;gt;|&amp;lt;CognitoClientId&amp;gt;&lt;/i&gt; &lt;/p&gt; &lt;p&gt;Where &lt;code&gt;IdentityType&lt;/code&gt; is the string that you provide to the &lt;code&gt;PrincipalEntityType&lt;/code&gt; parameter for this operation. The &lt;code&gt;CognitoUserPoolId&lt;/code&gt; and &lt;code&gt;CognitoClientId&lt;/code&gt; are defined by the Amazon Cognito user pool.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonVerifiedPermissions from 'amazon_verified_permissions';
let defaultClient = AmazonVerifiedPermissions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVerifiedPermissions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createIdentitySourceInput = new AmazonVerifiedPermissions.CreateIdentitySourceInput(); // CreateIdentitySourceInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createIdentitySource(xAmzTarget, createIdentitySourceInput, opts, (error, data, response) => {
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
 **createIdentitySourceInput** | [**CreateIdentitySourceInput**](CreateIdentitySourceInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateIdentitySourceOutput**](CreateIdentitySourceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPolicy

> CreatePolicyOutput createPolicy(xAmzTarget, createPolicyInput, opts)



&lt;p&gt;Creates a Cedar policy and saves it in the specified policy store. You can create either a static policy or a policy linked to a policy template.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;To create a static policy, provide the Cedar policy text in the &lt;code&gt;StaticPolicy&lt;/code&gt; section of the &lt;code&gt;PolicyDefinition&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To create a policy that is dynamically linked to a policy template, specify the policy template ID and the principal and resource to associate with this policy in the &lt;code&gt;templateLinked&lt;/code&gt; section of the &lt;code&gt;PolicyDefinition&lt;/code&gt;. If the policy template is ever updated, any policies linked to the policy template automatically use the updated template.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;Creating a policy causes it to be validated against the schema in the policy store. If the policy doesn&#39;t pass validation, the operation fails and the policy isn&#39;t stored.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonVerifiedPermissions from 'amazon_verified_permissions';
let defaultClient = AmazonVerifiedPermissions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVerifiedPermissions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createPolicyInput = new AmazonVerifiedPermissions.CreatePolicyInput(); // CreatePolicyInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createPolicy(xAmzTarget, createPolicyInput, opts, (error, data, response) => {
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
 **createPolicyInput** | [**CreatePolicyInput**](CreatePolicyInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreatePolicyOutput**](CreatePolicyOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPolicyStore

> CreatePolicyStoreOutput createPolicyStore(xAmzTarget, createPolicyStoreInput, opts)



&lt;p&gt;Creates a policy store. A policy store is a container for policy resources.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Although &lt;a href&#x3D;\&quot;https://docs.cedarpolicy.com/schema.html#namespace\&quot;&gt;Cedar supports multiple namespaces&lt;/a&gt;, Verified Permissions currently supports only one namespace per policy store.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonVerifiedPermissions from 'amazon_verified_permissions';
let defaultClient = AmazonVerifiedPermissions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVerifiedPermissions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createPolicyStoreInput = new AmazonVerifiedPermissions.CreatePolicyStoreInput(); // CreatePolicyStoreInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createPolicyStore(xAmzTarget, createPolicyStoreInput, opts, (error, data, response) => {
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
 **createPolicyStoreInput** | [**CreatePolicyStoreInput**](CreatePolicyStoreInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreatePolicyStoreOutput**](CreatePolicyStoreOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPolicyTemplate

> CreatePolicyTemplateOutput createPolicyTemplate(xAmzTarget, createPolicyTemplateInput, opts)



Creates a policy template. A template can use placeholders for the principal and resource. A template must be instantiated into a policy by associating it with specific principals and resources to use for the placeholders. That instantiated policy can then be considered in authorization decisions. The instantiated policy works identically to any other policy, except that it is dynamically linked to the template. If the template changes, then any policies that are linked to that template are immediately updated as well.

### Example

```javascript
import AmazonVerifiedPermissions from 'amazon_verified_permissions';
let defaultClient = AmazonVerifiedPermissions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVerifiedPermissions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createPolicyTemplateInput = new AmazonVerifiedPermissions.CreatePolicyTemplateInput(); // CreatePolicyTemplateInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createPolicyTemplate(xAmzTarget, createPolicyTemplateInput, opts, (error, data, response) => {
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
 **createPolicyTemplateInput** | [**CreatePolicyTemplateInput**](CreatePolicyTemplateInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreatePolicyTemplateOutput**](CreatePolicyTemplateOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteIdentitySource

> Object deleteIdentitySource(xAmzTarget, deleteIdentitySourceInput, opts)



Deletes an identity source that references an identity provider (IdP) such as Amazon Cognito. After you delete the identity source, you can no longer use tokens for identities from that identity source to represent principals in authorization queries made using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html\&quot;&gt;IsAuthorizedWithToken&lt;/a&gt;. operations.

### Example

```javascript
import AmazonVerifiedPermissions from 'amazon_verified_permissions';
let defaultClient = AmazonVerifiedPermissions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVerifiedPermissions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteIdentitySourceInput = new AmazonVerifiedPermissions.DeleteIdentitySourceInput(); // DeleteIdentitySourceInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteIdentitySource(xAmzTarget, deleteIdentitySourceInput, opts, (error, data, response) => {
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
 **deleteIdentitySourceInput** | [**DeleteIdentitySourceInput**](DeleteIdentitySourceInput.md)|  | 
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


## deletePolicy

> Object deletePolicy(xAmzTarget, deletePolicyInput, opts)



&lt;p&gt;Deletes the specified policy from the policy store.&lt;/p&gt; &lt;p&gt;This operation is idempotent; if you specify a policy that doesn&#39;t exist, the request response returns a successful &lt;code&gt;HTTP 200&lt;/code&gt; status code.&lt;/p&gt;

### Example

```javascript
import AmazonVerifiedPermissions from 'amazon_verified_permissions';
let defaultClient = AmazonVerifiedPermissions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVerifiedPermissions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deletePolicyInput = new AmazonVerifiedPermissions.DeletePolicyInput(); // DeletePolicyInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deletePolicy(xAmzTarget, deletePolicyInput, opts, (error, data, response) => {
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
 **deletePolicyInput** | [**DeletePolicyInput**](DeletePolicyInput.md)|  | 
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


## deletePolicyStore

> Object deletePolicyStore(xAmzTarget, deletePolicyStoreInput, opts)



&lt;p&gt;Deletes the specified policy store.&lt;/p&gt; &lt;p&gt;This operation is idempotent. If you specify a policy store that does not exist, the request response will still return a successful HTTP 200 status code.&lt;/p&gt;

### Example

```javascript
import AmazonVerifiedPermissions from 'amazon_verified_permissions';
let defaultClient = AmazonVerifiedPermissions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVerifiedPermissions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deletePolicyStoreInput = new AmazonVerifiedPermissions.DeletePolicyStoreInput(); // DeletePolicyStoreInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deletePolicyStore(xAmzTarget, deletePolicyStoreInput, opts, (error, data, response) => {
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
 **deletePolicyStoreInput** | [**DeletePolicyStoreInput**](DeletePolicyStoreInput.md)|  | 
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


## deletePolicyTemplate

> Object deletePolicyTemplate(xAmzTarget, deletePolicyTemplateInput, opts)



&lt;p&gt;Deletes the specified policy template from the policy store.&lt;/p&gt; &lt;important&gt; &lt;p&gt;This operation also deletes any policies that were created from the specified policy template. Those policies are immediately removed from all future API responses, and are asynchronously deleted from the policy store.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonVerifiedPermissions from 'amazon_verified_permissions';
let defaultClient = AmazonVerifiedPermissions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVerifiedPermissions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deletePolicyTemplateInput = new AmazonVerifiedPermissions.DeletePolicyTemplateInput(); // DeletePolicyTemplateInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deletePolicyTemplate(xAmzTarget, deletePolicyTemplateInput, opts, (error, data, response) => {
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
 **deletePolicyTemplateInput** | [**DeletePolicyTemplateInput**](DeletePolicyTemplateInput.md)|  | 
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


## getIdentitySource

> GetIdentitySourceOutput getIdentitySource(xAmzTarget, getIdentitySourceInput, opts)



Retrieves the details about the specified identity source.

### Example

```javascript
import AmazonVerifiedPermissions from 'amazon_verified_permissions';
let defaultClient = AmazonVerifiedPermissions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVerifiedPermissions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getIdentitySourceInput = new AmazonVerifiedPermissions.GetIdentitySourceInput(); // GetIdentitySourceInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getIdentitySource(xAmzTarget, getIdentitySourceInput, opts, (error, data, response) => {
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
 **getIdentitySourceInput** | [**GetIdentitySourceInput**](GetIdentitySourceInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetIdentitySourceOutput**](GetIdentitySourceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getPolicy

> GetPolicyOutput getPolicy(xAmzTarget, getPolicyInput, opts)



Retrieves information about the specified policy.

### Example

```javascript
import AmazonVerifiedPermissions from 'amazon_verified_permissions';
let defaultClient = AmazonVerifiedPermissions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVerifiedPermissions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getPolicyInput = new AmazonVerifiedPermissions.GetPolicyInput(); // GetPolicyInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getPolicy(xAmzTarget, getPolicyInput, opts, (error, data, response) => {
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
 **getPolicyInput** | [**GetPolicyInput**](GetPolicyInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetPolicyOutput**](GetPolicyOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getPolicyStore

> GetPolicyStoreOutput getPolicyStore(xAmzTarget, getPolicyStoreInput, opts)



Retrieves details about a policy store.

### Example

```javascript
import AmazonVerifiedPermissions from 'amazon_verified_permissions';
let defaultClient = AmazonVerifiedPermissions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVerifiedPermissions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getPolicyStoreInput = new AmazonVerifiedPermissions.GetPolicyStoreInput(); // GetPolicyStoreInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getPolicyStore(xAmzTarget, getPolicyStoreInput, opts, (error, data, response) => {
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
 **getPolicyStoreInput** | [**GetPolicyStoreInput**](GetPolicyStoreInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetPolicyStoreOutput**](GetPolicyStoreOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getPolicyTemplate

> GetPolicyTemplateOutput getPolicyTemplate(xAmzTarget, getPolicyTemplateInput, opts)



Retrieve the details for the specified policy template in the specified policy store.

### Example

```javascript
import AmazonVerifiedPermissions from 'amazon_verified_permissions';
let defaultClient = AmazonVerifiedPermissions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVerifiedPermissions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getPolicyTemplateInput = new AmazonVerifiedPermissions.GetPolicyTemplateInput(); // GetPolicyTemplateInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getPolicyTemplate(xAmzTarget, getPolicyTemplateInput, opts, (error, data, response) => {
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
 **getPolicyTemplateInput** | [**GetPolicyTemplateInput**](GetPolicyTemplateInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetPolicyTemplateOutput**](GetPolicyTemplateOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getSchema

> GetSchemaOutput getSchema(xAmzTarget, getSchemaInput, opts)



Retrieve the details for the specified schema in the specified policy store.

### Example

```javascript
import AmazonVerifiedPermissions from 'amazon_verified_permissions';
let defaultClient = AmazonVerifiedPermissions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVerifiedPermissions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getSchemaInput = new AmazonVerifiedPermissions.GetSchemaInput(); // GetSchemaInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSchema(xAmzTarget, getSchemaInput, opts, (error, data, response) => {
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
 **getSchemaInput** | [**GetSchemaInput**](GetSchemaInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSchemaOutput**](GetSchemaOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## isAuthorized

> IsAuthorizedOutput isAuthorized(xAmzTarget, isAuthorizedInput, opts)



Makes an authorization decision about a service request described in the parameters. The information in the parameters can also define additional context that Verified Permissions can include in the evaluation. The request is evaluated against all matching policies in the specified policy store. The result of the decision is either &lt;code&gt;Allow&lt;/code&gt; or &lt;code&gt;Deny&lt;/code&gt;, along with a list of the policies that resulted in the decision.

### Example

```javascript
import AmazonVerifiedPermissions from 'amazon_verified_permissions';
let defaultClient = AmazonVerifiedPermissions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVerifiedPermissions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let isAuthorizedInput = new AmazonVerifiedPermissions.IsAuthorizedInput(); // IsAuthorizedInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.isAuthorized(xAmzTarget, isAuthorizedInput, opts, (error, data, response) => {
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
 **isAuthorizedInput** | [**IsAuthorizedInput**](IsAuthorizedInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**IsAuthorizedOutput**](IsAuthorizedOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## isAuthorizedWithToken

> IsAuthorizedWithTokenOutput isAuthorizedWithToken(xAmzTarget, isAuthorizedWithTokenInput, opts)



&lt;p&gt;Makes an authorization decision about a service request described in the parameters. The principal in this request comes from an external identity source. The information in the parameters can also define additional context that Verified Permissions can include in the evaluation. The request is evaluated against all matching policies in the specified policy store. The result of the decision is either &lt;code&gt;Allow&lt;/code&gt; or &lt;code&gt;Deny&lt;/code&gt;, along with a list of the policies that resulted in the decision.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If you delete a Amazon Cognito user pool or user, tokens from that deleted pool or that deleted user continue to be usable until they expire.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonVerifiedPermissions from 'amazon_verified_permissions';
let defaultClient = AmazonVerifiedPermissions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVerifiedPermissions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let isAuthorizedWithTokenInput = new AmazonVerifiedPermissions.IsAuthorizedWithTokenInput(); // IsAuthorizedWithTokenInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.isAuthorizedWithToken(xAmzTarget, isAuthorizedWithTokenInput, opts, (error, data, response) => {
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
 **isAuthorizedWithTokenInput** | [**IsAuthorizedWithTokenInput**](IsAuthorizedWithTokenInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**IsAuthorizedWithTokenOutput**](IsAuthorizedWithTokenOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listIdentitySources

> ListIdentitySourcesOutput listIdentitySources(xAmzTarget, listIdentitySourcesInput, opts)



Returns a paginated list of all of the identity sources defined in the specified policy store.

### Example

```javascript
import AmazonVerifiedPermissions from 'amazon_verified_permissions';
let defaultClient = AmazonVerifiedPermissions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVerifiedPermissions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listIdentitySourcesInput = new AmazonVerifiedPermissions.ListIdentitySourcesInput(); // ListIdentitySourcesInput | 
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
apiInstance.listIdentitySources(xAmzTarget, listIdentitySourcesInput, opts, (error, data, response) => {
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
 **listIdentitySourcesInput** | [**ListIdentitySourcesInput**](ListIdentitySourcesInput.md)|  | 
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

[**ListIdentitySourcesOutput**](ListIdentitySourcesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listPolicies

> ListPoliciesOutput listPolicies(xAmzTarget, listPoliciesInput, opts)



Returns a paginated list of all policies stored in the specified policy store.

### Example

```javascript
import AmazonVerifiedPermissions from 'amazon_verified_permissions';
let defaultClient = AmazonVerifiedPermissions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVerifiedPermissions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listPoliciesInput = new AmazonVerifiedPermissions.ListPoliciesInput(); // ListPoliciesInput | 
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
apiInstance.listPolicies(xAmzTarget, listPoliciesInput, opts, (error, data, response) => {
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
 **listPoliciesInput** | [**ListPoliciesInput**](ListPoliciesInput.md)|  | 
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

[**ListPoliciesOutput**](ListPoliciesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listPolicyStores

> ListPolicyStoresOutput listPolicyStores(xAmzTarget, listPolicyStoresInput, opts)



Returns a paginated list of all policy stores in the calling Amazon Web Services account.

### Example

```javascript
import AmazonVerifiedPermissions from 'amazon_verified_permissions';
let defaultClient = AmazonVerifiedPermissions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVerifiedPermissions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listPolicyStoresInput = new AmazonVerifiedPermissions.ListPolicyStoresInput(); // ListPolicyStoresInput | 
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
apiInstance.listPolicyStores(xAmzTarget, listPolicyStoresInput, opts, (error, data, response) => {
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
 **listPolicyStoresInput** | [**ListPolicyStoresInput**](ListPolicyStoresInput.md)|  | 
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

[**ListPolicyStoresOutput**](ListPolicyStoresOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listPolicyTemplates

> ListPolicyTemplatesOutput listPolicyTemplates(xAmzTarget, listPolicyTemplatesInput, opts)



Returns a paginated list of all policy templates in the specified policy store.

### Example

```javascript
import AmazonVerifiedPermissions from 'amazon_verified_permissions';
let defaultClient = AmazonVerifiedPermissions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVerifiedPermissions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listPolicyTemplatesInput = new AmazonVerifiedPermissions.ListPolicyTemplatesInput(); // ListPolicyTemplatesInput | 
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
apiInstance.listPolicyTemplates(xAmzTarget, listPolicyTemplatesInput, opts, (error, data, response) => {
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
 **listPolicyTemplatesInput** | [**ListPolicyTemplatesInput**](ListPolicyTemplatesInput.md)|  | 
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

[**ListPolicyTemplatesOutput**](ListPolicyTemplatesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putSchema

> PutSchemaOutput putSchema(xAmzTarget, putSchemaInput, opts)



Creates or updates the policy schema in the specified policy store. The schema is used to validate any Cedar policies and policy templates submitted to the policy store. Any changes to the schema validate only policies and templates submitted after the schema change. Existing policies and templates are not re-evaluated against the changed schema. If you later update a policy, then it is evaluated against the new schema at that time.

### Example

```javascript
import AmazonVerifiedPermissions from 'amazon_verified_permissions';
let defaultClient = AmazonVerifiedPermissions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVerifiedPermissions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let putSchemaInput = new AmazonVerifiedPermissions.PutSchemaInput(); // PutSchemaInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putSchema(xAmzTarget, putSchemaInput, opts, (error, data, response) => {
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
 **putSchemaInput** | [**PutSchemaInput**](PutSchemaInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutSchemaOutput**](PutSchemaOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateIdentitySource

> UpdateIdentitySourceOutput updateIdentitySource(xAmzTarget, updateIdentitySourceInput, opts)



Updates the specified identity source to use a new identity provider (IdP) source, or to change the mapping of identities from the IdP to a different principal entity type.

### Example

```javascript
import AmazonVerifiedPermissions from 'amazon_verified_permissions';
let defaultClient = AmazonVerifiedPermissions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVerifiedPermissions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateIdentitySourceInput = new AmazonVerifiedPermissions.UpdateIdentitySourceInput(); // UpdateIdentitySourceInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateIdentitySource(xAmzTarget, updateIdentitySourceInput, opts, (error, data, response) => {
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
 **updateIdentitySourceInput** | [**UpdateIdentitySourceInput**](UpdateIdentitySourceInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateIdentitySourceOutput**](UpdateIdentitySourceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updatePolicy

> UpdatePolicyOutput updatePolicy(xAmzTarget, updatePolicyInput, opts)



&lt;p&gt;Modifies a Cedar static policy in the specified policy store. You can change only certain elements of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyInput.html#amazonverifiedpermissions-UpdatePolicy-request-UpdatePolicyDefinition\&quot;&gt;UpdatePolicyDefinition&lt;/a&gt; parameter. You can directly update only static policies. To change a template-linked policy, you must update the template instead, using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyTemplate.html\&quot;&gt;UpdatePolicyTemplate&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If policy validation is enabled in the policy store, then updating a static policy causes Verified Permissions to validate the policy against the schema in the policy store. If the updated static policy doesn&#39;t pass validation, the operation fails and the update isn&#39;t stored.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonVerifiedPermissions from 'amazon_verified_permissions';
let defaultClient = AmazonVerifiedPermissions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVerifiedPermissions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updatePolicyInput = new AmazonVerifiedPermissions.UpdatePolicyInput(); // UpdatePolicyInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updatePolicy(xAmzTarget, updatePolicyInput, opts, (error, data, response) => {
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
 **updatePolicyInput** | [**UpdatePolicyInput**](UpdatePolicyInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdatePolicyOutput**](UpdatePolicyOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updatePolicyStore

> UpdatePolicyStoreOutput updatePolicyStore(xAmzTarget, updatePolicyStoreInput, opts)



Modifies the validation setting for a policy store.

### Example

```javascript
import AmazonVerifiedPermissions from 'amazon_verified_permissions';
let defaultClient = AmazonVerifiedPermissions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVerifiedPermissions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updatePolicyStoreInput = new AmazonVerifiedPermissions.UpdatePolicyStoreInput(); // UpdatePolicyStoreInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updatePolicyStore(xAmzTarget, updatePolicyStoreInput, opts, (error, data, response) => {
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
 **updatePolicyStoreInput** | [**UpdatePolicyStoreInput**](UpdatePolicyStoreInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdatePolicyStoreOutput**](UpdatePolicyStoreOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updatePolicyTemplate

> UpdatePolicyTemplateOutput updatePolicyTemplate(xAmzTarget, updatePolicyTemplateInput, opts)



&lt;p&gt;Updates the specified policy template. You can update only the description and the some elements of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyTemplate.html#amazonverifiedpermissions-UpdatePolicyTemplate-request-policyBody\&quot;&gt;policyBody&lt;/a&gt;. &lt;/p&gt; &lt;important&gt; &lt;p&gt;Changes you make to the policy template content are immediately reflected in authorization decisions that involve all template-linked policies instantiated from this template.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonVerifiedPermissions from 'amazon_verified_permissions';
let defaultClient = AmazonVerifiedPermissions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonVerifiedPermissions.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updatePolicyTemplateInput = new AmazonVerifiedPermissions.UpdatePolicyTemplateInput(); // UpdatePolicyTemplateInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updatePolicyTemplate(xAmzTarget, updatePolicyTemplateInput, opts, (error, data, response) => {
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
 **updatePolicyTemplateInput** | [**UpdatePolicyTemplateInput**](UpdatePolicyTemplateInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdatePolicyTemplateOutput**](UpdatePolicyTemplateOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

