# AmazonCognitoIdentity.DefaultApi

All URIs are relative to *http://cognito-identity.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createIdentityPool**](DefaultApi.md#createIdentityPool) | **POST** /#X-Amz-Target&#x3D;AWSCognitoIdentityService.CreateIdentityPool | 
[**deleteIdentities**](DefaultApi.md#deleteIdentities) | **POST** /#X-Amz-Target&#x3D;AWSCognitoIdentityService.DeleteIdentities | 
[**deleteIdentityPool**](DefaultApi.md#deleteIdentityPool) | **POST** /#X-Amz-Target&#x3D;AWSCognitoIdentityService.DeleteIdentityPool | 
[**describeIdentity**](DefaultApi.md#describeIdentity) | **POST** /#X-Amz-Target&#x3D;AWSCognitoIdentityService.DescribeIdentity | 
[**describeIdentityPool**](DefaultApi.md#describeIdentityPool) | **POST** /#X-Amz-Target&#x3D;AWSCognitoIdentityService.DescribeIdentityPool | 
[**getCredentialsForIdentity**](DefaultApi.md#getCredentialsForIdentity) | **POST** /#X-Amz-Target&#x3D;AWSCognitoIdentityService.GetCredentialsForIdentity | 
[**getId**](DefaultApi.md#getId) | **POST** /#X-Amz-Target&#x3D;AWSCognitoIdentityService.GetId | 
[**getIdentityPoolRoles**](DefaultApi.md#getIdentityPoolRoles) | **POST** /#X-Amz-Target&#x3D;AWSCognitoIdentityService.GetIdentityPoolRoles | 
[**getOpenIdToken**](DefaultApi.md#getOpenIdToken) | **POST** /#X-Amz-Target&#x3D;AWSCognitoIdentityService.GetOpenIdToken | 
[**getOpenIdTokenForDeveloperIdentity**](DefaultApi.md#getOpenIdTokenForDeveloperIdentity) | **POST** /#X-Amz-Target&#x3D;AWSCognitoIdentityService.GetOpenIdTokenForDeveloperIdentity | 
[**getPrincipalTagAttributeMap**](DefaultApi.md#getPrincipalTagAttributeMap) | **POST** /#X-Amz-Target&#x3D;AWSCognitoIdentityService.GetPrincipalTagAttributeMap | 
[**listIdentities**](DefaultApi.md#listIdentities) | **POST** /#X-Amz-Target&#x3D;AWSCognitoIdentityService.ListIdentities | 
[**listIdentityPools**](DefaultApi.md#listIdentityPools) | **POST** /#X-Amz-Target&#x3D;AWSCognitoIdentityService.ListIdentityPools | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **POST** /#X-Amz-Target&#x3D;AWSCognitoIdentityService.ListTagsForResource | 
[**lookupDeveloperIdentity**](DefaultApi.md#lookupDeveloperIdentity) | **POST** /#X-Amz-Target&#x3D;AWSCognitoIdentityService.LookupDeveloperIdentity | 
[**mergeDeveloperIdentities**](DefaultApi.md#mergeDeveloperIdentities) | **POST** /#X-Amz-Target&#x3D;AWSCognitoIdentityService.MergeDeveloperIdentities | 
[**setIdentityPoolRoles**](DefaultApi.md#setIdentityPoolRoles) | **POST** /#X-Amz-Target&#x3D;AWSCognitoIdentityService.SetIdentityPoolRoles | 
[**setPrincipalTagAttributeMap**](DefaultApi.md#setPrincipalTagAttributeMap) | **POST** /#X-Amz-Target&#x3D;AWSCognitoIdentityService.SetPrincipalTagAttributeMap | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /#X-Amz-Target&#x3D;AWSCognitoIdentityService.TagResource | 
[**unlinkDeveloperIdentity**](DefaultApi.md#unlinkDeveloperIdentity) | **POST** /#X-Amz-Target&#x3D;AWSCognitoIdentityService.UnlinkDeveloperIdentity | 
[**unlinkIdentity**](DefaultApi.md#unlinkIdentity) | **POST** /#X-Amz-Target&#x3D;AWSCognitoIdentityService.UnlinkIdentity | 
[**untagResource**](DefaultApi.md#untagResource) | **POST** /#X-Amz-Target&#x3D;AWSCognitoIdentityService.UntagResource | 
[**updateIdentityPool**](DefaultApi.md#updateIdentityPool) | **POST** /#X-Amz-Target&#x3D;AWSCognitoIdentityService.UpdateIdentityPool | 



## createIdentityPool

> IdentityPool createIdentityPool(xAmzTarget, createIdentityPoolInput, opts)



&lt;p&gt;Creates a new identity pool. The identity pool is a store of user identity information that is specific to your AWS account. The keys for &lt;code&gt;SupportedLoginProviders&lt;/code&gt; are as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Facebook: &lt;code&gt;graph.facebook.com&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Google: &lt;code&gt;accounts.google.com&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon: &lt;code&gt;www.amazon.com&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Twitter: &lt;code&gt;api.twitter.com&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Digits: &lt;code&gt;www.digits.com&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;You must use AWS Developer credentials to call this API.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoIdentity from 'amazon_cognito_identity';
let defaultClient = AmazonCognitoIdentity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoIdentity.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createIdentityPoolInput = new AmazonCognitoIdentity.CreateIdentityPoolInput(); // CreateIdentityPoolInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createIdentityPool(xAmzTarget, createIdentityPoolInput, opts, (error, data, response) => {
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
 **createIdentityPoolInput** | [**CreateIdentityPoolInput**](CreateIdentityPoolInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**IdentityPool**](IdentityPool.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteIdentities

> DeleteIdentitiesResponse deleteIdentities(xAmzTarget, deleteIdentitiesInput, opts)



&lt;p&gt;Deletes identities from an identity pool. You can specify a list of 1-60 identities that you want to delete.&lt;/p&gt; &lt;p&gt;You must use AWS Developer credentials to call this API.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoIdentity from 'amazon_cognito_identity';
let defaultClient = AmazonCognitoIdentity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoIdentity.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteIdentitiesInput = new AmazonCognitoIdentity.DeleteIdentitiesInput(); // DeleteIdentitiesInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteIdentities(xAmzTarget, deleteIdentitiesInput, opts, (error, data, response) => {
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
 **deleteIdentitiesInput** | [**DeleteIdentitiesInput**](DeleteIdentitiesInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteIdentitiesResponse**](DeleteIdentitiesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteIdentityPool

> deleteIdentityPool(xAmzTarget, deleteIdentityPoolInput, opts)



&lt;p&gt;Deletes an identity pool. Once a pool is deleted, users will not be able to authenticate with the pool.&lt;/p&gt; &lt;p&gt;You must use AWS Developer credentials to call this API.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoIdentity from 'amazon_cognito_identity';
let defaultClient = AmazonCognitoIdentity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoIdentity.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteIdentityPoolInput = new AmazonCognitoIdentity.DeleteIdentityPoolInput(); // DeleteIdentityPoolInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteIdentityPool(xAmzTarget, deleteIdentityPoolInput, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **deleteIdentityPoolInput** | [**DeleteIdentityPoolInput**](DeleteIdentityPoolInput.md)|  | 
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


## describeIdentity

> IdentityDescription describeIdentity(xAmzTarget, describeIdentityInput, opts)



&lt;p&gt;Returns metadata related to the given identity, including when the identity was created and any associated linked logins.&lt;/p&gt; &lt;p&gt;You must use AWS Developer credentials to call this API.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoIdentity from 'amazon_cognito_identity';
let defaultClient = AmazonCognitoIdentity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoIdentity.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeIdentityInput = new AmazonCognitoIdentity.DescribeIdentityInput(); // DescribeIdentityInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeIdentity(xAmzTarget, describeIdentityInput, opts, (error, data, response) => {
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
 **describeIdentityInput** | [**DescribeIdentityInput**](DescribeIdentityInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**IdentityDescription**](IdentityDescription.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeIdentityPool

> IdentityPool describeIdentityPool(xAmzTarget, describeIdentityPoolInput, opts)



&lt;p&gt;Gets details about a particular identity pool, including the pool name, ID description, creation date, and current number of users.&lt;/p&gt; &lt;p&gt;You must use AWS Developer credentials to call this API.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoIdentity from 'amazon_cognito_identity';
let defaultClient = AmazonCognitoIdentity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoIdentity.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeIdentityPoolInput = new AmazonCognitoIdentity.DescribeIdentityPoolInput(); // DescribeIdentityPoolInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeIdentityPool(xAmzTarget, describeIdentityPoolInput, opts, (error, data, response) => {
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
 **describeIdentityPoolInput** | [**DescribeIdentityPoolInput**](DescribeIdentityPoolInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**IdentityPool**](IdentityPool.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getCredentialsForIdentity

> GetCredentialsForIdentityResponse getCredentialsForIdentity(xAmzTarget, getCredentialsForIdentityInput, opts)



&lt;p&gt;Returns credentials for the provided identity ID. Any provided logins will be validated against supported login providers. If the token is for cognito-identity.amazonaws.com, it will be passed through to AWS Security Token Service with the appropriate role for the token.&lt;/p&gt; &lt;p&gt;This is a public API. You do not need any credentials to call this API.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoIdentity from 'amazon_cognito_identity';
let defaultClient = AmazonCognitoIdentity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoIdentity.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getCredentialsForIdentityInput = new AmazonCognitoIdentity.GetCredentialsForIdentityInput(); // GetCredentialsForIdentityInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getCredentialsForIdentity(xAmzTarget, getCredentialsForIdentityInput, opts, (error, data, response) => {
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
 **getCredentialsForIdentityInput** | [**GetCredentialsForIdentityInput**](GetCredentialsForIdentityInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetCredentialsForIdentityResponse**](GetCredentialsForIdentityResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getId

> GetIdResponse getId(xAmzTarget, getIdInput, opts)



&lt;p&gt;Generates (or retrieves) a Cognito ID. Supplying multiple logins will create an implicit linked account.&lt;/p&gt; &lt;p&gt;This is a public API. You do not need any credentials to call this API.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoIdentity from 'amazon_cognito_identity';
let defaultClient = AmazonCognitoIdentity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoIdentity.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getIdInput = new AmazonCognitoIdentity.GetIdInput(); // GetIdInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getId(xAmzTarget, getIdInput, opts, (error, data, response) => {
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
 **getIdInput** | [**GetIdInput**](GetIdInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetIdResponse**](GetIdResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getIdentityPoolRoles

> GetIdentityPoolRolesResponse getIdentityPoolRoles(xAmzTarget, getIdentityPoolRolesInput, opts)



&lt;p&gt;Gets the roles for an identity pool.&lt;/p&gt; &lt;p&gt;You must use AWS Developer credentials to call this API.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoIdentity from 'amazon_cognito_identity';
let defaultClient = AmazonCognitoIdentity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoIdentity.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getIdentityPoolRolesInput = new AmazonCognitoIdentity.GetIdentityPoolRolesInput(); // GetIdentityPoolRolesInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getIdentityPoolRoles(xAmzTarget, getIdentityPoolRolesInput, opts, (error, data, response) => {
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
 **getIdentityPoolRolesInput** | [**GetIdentityPoolRolesInput**](GetIdentityPoolRolesInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetIdentityPoolRolesResponse**](GetIdentityPoolRolesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getOpenIdToken

> GetOpenIdTokenResponse getOpenIdToken(xAmzTarget, getOpenIdTokenInput, opts)



&lt;p&gt;Gets an OpenID token, using a known Cognito ID. This known Cognito ID is returned by &lt;a&gt;GetId&lt;/a&gt;. You can optionally add additional logins for the identity. Supplying multiple logins creates an implicit link.&lt;/p&gt; &lt;p&gt;The OpenID token is valid for 10 minutes.&lt;/p&gt; &lt;p&gt;This is a public API. You do not need any credentials to call this API.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoIdentity from 'amazon_cognito_identity';
let defaultClient = AmazonCognitoIdentity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoIdentity.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getOpenIdTokenInput = new AmazonCognitoIdentity.GetOpenIdTokenInput(); // GetOpenIdTokenInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getOpenIdToken(xAmzTarget, getOpenIdTokenInput, opts, (error, data, response) => {
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
 **getOpenIdTokenInput** | [**GetOpenIdTokenInput**](GetOpenIdTokenInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetOpenIdTokenResponse**](GetOpenIdTokenResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getOpenIdTokenForDeveloperIdentity

> GetOpenIdTokenForDeveloperIdentityResponse getOpenIdTokenForDeveloperIdentity(xAmzTarget, getOpenIdTokenForDeveloperIdentityInput, opts)



&lt;p&gt;Registers (or retrieves) a Cognito &lt;code&gt;IdentityId&lt;/code&gt; and an OpenID Connect token for a user authenticated by your backend authentication process. Supplying multiple logins will create an implicit linked account. You can only specify one developer provider as part of the &lt;code&gt;Logins&lt;/code&gt; map, which is linked to the identity pool. The developer provider is the \&quot;domain\&quot; by which Cognito will refer to your users.&lt;/p&gt; &lt;p&gt;You can use &lt;code&gt;GetOpenIdTokenForDeveloperIdentity&lt;/code&gt; to create a new identity and to link new logins (that is, user credentials issued by a public provider or developer provider) to an existing identity. When you want to create a new identity, the &lt;code&gt;IdentityId&lt;/code&gt; should be null. When you want to associate a new login with an existing authenticated/unauthenticated identity, you can do so by providing the existing &lt;code&gt;IdentityId&lt;/code&gt;. This API will create the identity in the specified &lt;code&gt;IdentityPoolId&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;You must use AWS Developer credentials to call this API.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoIdentity from 'amazon_cognito_identity';
let defaultClient = AmazonCognitoIdentity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoIdentity.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getOpenIdTokenForDeveloperIdentityInput = new AmazonCognitoIdentity.GetOpenIdTokenForDeveloperIdentityInput(); // GetOpenIdTokenForDeveloperIdentityInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getOpenIdTokenForDeveloperIdentity(xAmzTarget, getOpenIdTokenForDeveloperIdentityInput, opts, (error, data, response) => {
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
 **getOpenIdTokenForDeveloperIdentityInput** | [**GetOpenIdTokenForDeveloperIdentityInput**](GetOpenIdTokenForDeveloperIdentityInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetOpenIdTokenForDeveloperIdentityResponse**](GetOpenIdTokenForDeveloperIdentityResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getPrincipalTagAttributeMap

> GetPrincipalTagAttributeMapResponse getPrincipalTagAttributeMap(xAmzTarget, getPrincipalTagAttributeMapInput, opts)



Use &lt;code&gt;GetPrincipalTagAttributeMap&lt;/code&gt; to list all mappings between &lt;code&gt;PrincipalTags&lt;/code&gt; and user attributes.

### Example

```javascript
import AmazonCognitoIdentity from 'amazon_cognito_identity';
let defaultClient = AmazonCognitoIdentity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoIdentity.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getPrincipalTagAttributeMapInput = new AmazonCognitoIdentity.GetPrincipalTagAttributeMapInput(); // GetPrincipalTagAttributeMapInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getPrincipalTagAttributeMap(xAmzTarget, getPrincipalTagAttributeMapInput, opts, (error, data, response) => {
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
 **getPrincipalTagAttributeMapInput** | [**GetPrincipalTagAttributeMapInput**](GetPrincipalTagAttributeMapInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetPrincipalTagAttributeMapResponse**](GetPrincipalTagAttributeMapResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listIdentities

> ListIdentitiesResponse listIdentities(xAmzTarget, listIdentitiesInput, opts)



&lt;p&gt;Lists the identities in an identity pool.&lt;/p&gt; &lt;p&gt;You must use AWS Developer credentials to call this API.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoIdentity from 'amazon_cognito_identity';
let defaultClient = AmazonCognitoIdentity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoIdentity.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listIdentitiesInput = new AmazonCognitoIdentity.ListIdentitiesInput(); // ListIdentitiesInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listIdentities(xAmzTarget, listIdentitiesInput, opts, (error, data, response) => {
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
 **listIdentitiesInput** | [**ListIdentitiesInput**](ListIdentitiesInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListIdentitiesResponse**](ListIdentitiesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listIdentityPools

> ListIdentityPoolsResponse listIdentityPools(xAmzTarget, listIdentityPoolsInput, opts)



&lt;p&gt;Lists all of the Cognito identity pools registered for your account.&lt;/p&gt; &lt;p&gt;You must use AWS Developer credentials to call this API.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoIdentity from 'amazon_cognito_identity';
let defaultClient = AmazonCognitoIdentity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoIdentity.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listIdentityPoolsInput = new AmazonCognitoIdentity.ListIdentityPoolsInput(); // ListIdentityPoolsInput | 
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
apiInstance.listIdentityPools(xAmzTarget, listIdentityPoolsInput, opts, (error, data, response) => {
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
 **listIdentityPoolsInput** | [**ListIdentityPoolsInput**](ListIdentityPoolsInput.md)|  | 
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

[**ListIdentityPoolsResponse**](ListIdentityPoolsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(xAmzTarget, listTagsForResourceInput, opts)



&lt;p&gt;Lists the tags that are assigned to an Amazon Cognito identity pool.&lt;/p&gt; &lt;p&gt;A tag is a label that you can apply to identity pools to categorize and manage them in different ways, such as by purpose, owner, environment, or other criteria.&lt;/p&gt; &lt;p&gt;You can use this action up to 10 times per second, per account.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoIdentity from 'amazon_cognito_identity';
let defaultClient = AmazonCognitoIdentity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoIdentity.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listTagsForResourceInput = new AmazonCognitoIdentity.ListTagsForResourceInput(); // ListTagsForResourceInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTagsForResource(xAmzTarget, listTagsForResourceInput, opts, (error, data, response) => {
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
 **listTagsForResourceInput** | [**ListTagsForResourceInput**](ListTagsForResourceInput.md)|  | 
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


## lookupDeveloperIdentity

> LookupDeveloperIdentityResponse lookupDeveloperIdentity(xAmzTarget, lookupDeveloperIdentityInput, opts)



&lt;p&gt;Retrieves the &lt;code&gt;IdentityID&lt;/code&gt; associated with a &lt;code&gt;DeveloperUserIdentifier&lt;/code&gt; or the list of &lt;code&gt;DeveloperUserIdentifier&lt;/code&gt; values associated with an &lt;code&gt;IdentityId&lt;/code&gt; for an existing identity. Either &lt;code&gt;IdentityID&lt;/code&gt; or &lt;code&gt;DeveloperUserIdentifier&lt;/code&gt; must not be null. If you supply only one of these values, the other value will be searched in the database and returned as a part of the response. If you supply both, &lt;code&gt;DeveloperUserIdentifier&lt;/code&gt; will be matched against &lt;code&gt;IdentityID&lt;/code&gt;. If the values are verified against the database, the response returns both values and is the same as the request. Otherwise a &lt;code&gt;ResourceConflictException&lt;/code&gt; is thrown.&lt;/p&gt; &lt;p&gt; &lt;code&gt;LookupDeveloperIdentity&lt;/code&gt; is intended for low-throughput control plane operations: for example, to enable customer service to locate an identity ID by username. If you are using it for higher-volume operations such as user authentication, your requests are likely to be throttled. &lt;a&gt;GetOpenIdTokenForDeveloperIdentity&lt;/a&gt; is a better option for higher-volume operations for user authentication.&lt;/p&gt; &lt;p&gt;You must use AWS Developer credentials to call this API.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoIdentity from 'amazon_cognito_identity';
let defaultClient = AmazonCognitoIdentity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoIdentity.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let lookupDeveloperIdentityInput = new AmazonCognitoIdentity.LookupDeveloperIdentityInput(); // LookupDeveloperIdentityInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.lookupDeveloperIdentity(xAmzTarget, lookupDeveloperIdentityInput, opts, (error, data, response) => {
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
 **lookupDeveloperIdentityInput** | [**LookupDeveloperIdentityInput**](LookupDeveloperIdentityInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**LookupDeveloperIdentityResponse**](LookupDeveloperIdentityResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## mergeDeveloperIdentities

> MergeDeveloperIdentitiesResponse mergeDeveloperIdentities(xAmzTarget, mergeDeveloperIdentitiesInput, opts)



&lt;p&gt;Merges two users having different &lt;code&gt;IdentityId&lt;/code&gt;s, existing in the same identity pool, and identified by the same developer provider. You can use this action to request that discrete users be merged and identified as a single user in the Cognito environment. Cognito associates the given source user (&lt;code&gt;SourceUserIdentifier&lt;/code&gt;) with the &lt;code&gt;IdentityId&lt;/code&gt; of the &lt;code&gt;DestinationUserIdentifier&lt;/code&gt;. Only developer-authenticated users can be merged. If the users to be merged are associated with the same public provider, but as two different users, an exception will be thrown.&lt;/p&gt; &lt;p&gt;The number of linked logins is limited to 20. So, the number of linked logins for the source user, &lt;code&gt;SourceUserIdentifier&lt;/code&gt;, and the destination user, &lt;code&gt;DestinationUserIdentifier&lt;/code&gt;, together should not be larger than 20. Otherwise, an exception will be thrown.&lt;/p&gt; &lt;p&gt;You must use AWS Developer credentials to call this API.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoIdentity from 'amazon_cognito_identity';
let defaultClient = AmazonCognitoIdentity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoIdentity.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let mergeDeveloperIdentitiesInput = new AmazonCognitoIdentity.MergeDeveloperIdentitiesInput(); // MergeDeveloperIdentitiesInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.mergeDeveloperIdentities(xAmzTarget, mergeDeveloperIdentitiesInput, opts, (error, data, response) => {
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
 **mergeDeveloperIdentitiesInput** | [**MergeDeveloperIdentitiesInput**](MergeDeveloperIdentitiesInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**MergeDeveloperIdentitiesResponse**](MergeDeveloperIdentitiesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setIdentityPoolRoles

> setIdentityPoolRoles(xAmzTarget, setIdentityPoolRolesInput, opts)



&lt;p&gt;Sets the roles for an identity pool. These roles are used when making calls to &lt;a&gt;GetCredentialsForIdentity&lt;/a&gt; action.&lt;/p&gt; &lt;p&gt;You must use AWS Developer credentials to call this API.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoIdentity from 'amazon_cognito_identity';
let defaultClient = AmazonCognitoIdentity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoIdentity.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let setIdentityPoolRolesInput = new AmazonCognitoIdentity.SetIdentityPoolRolesInput(); // SetIdentityPoolRolesInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.setIdentityPoolRoles(xAmzTarget, setIdentityPoolRolesInput, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **setIdentityPoolRolesInput** | [**SetIdentityPoolRolesInput**](SetIdentityPoolRolesInput.md)|  | 
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


## setPrincipalTagAttributeMap

> SetPrincipalTagAttributeMapResponse setPrincipalTagAttributeMap(xAmzTarget, setPrincipalTagAttributeMapInput, opts)



You can use this operation to use default (username and clientID) attribute or custom attribute mappings.

### Example

```javascript
import AmazonCognitoIdentity from 'amazon_cognito_identity';
let defaultClient = AmazonCognitoIdentity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoIdentity.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let setPrincipalTagAttributeMapInput = new AmazonCognitoIdentity.SetPrincipalTagAttributeMapInput(); // SetPrincipalTagAttributeMapInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.setPrincipalTagAttributeMap(xAmzTarget, setPrincipalTagAttributeMapInput, opts, (error, data, response) => {
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
 **setPrincipalTagAttributeMapInput** | [**SetPrincipalTagAttributeMapInput**](SetPrincipalTagAttributeMapInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**SetPrincipalTagAttributeMapResponse**](SetPrincipalTagAttributeMapResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(xAmzTarget, tagResourceInput, opts)



&lt;p&gt;Assigns a set of tags to the specified Amazon Cognito identity pool. A tag is a label that you can use to categorize and manage identity pools in different ways, such as by purpose, owner, environment, or other criteria.&lt;/p&gt; &lt;p&gt;Each tag consists of a key and value, both of which you define. A key is a general category for more specific values. For example, if you have two versions of an identity pool, one for testing and another for production, you might assign an &lt;code&gt;Environment&lt;/code&gt; tag key to both identity pools. The value of this key might be &lt;code&gt;Test&lt;/code&gt; for one identity pool and &lt;code&gt;Production&lt;/code&gt; for the other.&lt;/p&gt; &lt;p&gt;Tags are useful for cost tracking and access control. You can activate your tags so that they appear on the Billing and Cost Management console, where you can track the costs associated with your identity pools. In an IAM policy, you can constrain permissions for identity pools based on specific tags or tag values.&lt;/p&gt; &lt;p&gt;You can use this action up to 5 times per second, per account. An identity pool can have as many as 50 tags.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoIdentity from 'amazon_cognito_identity';
let defaultClient = AmazonCognitoIdentity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoIdentity.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let tagResourceInput = new AmazonCognitoIdentity.TagResourceInput(); // TagResourceInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(xAmzTarget, tagResourceInput, opts, (error, data, response) => {
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
 **tagResourceInput** | [**TagResourceInput**](TagResourceInput.md)|  | 
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


## unlinkDeveloperIdentity

> unlinkDeveloperIdentity(xAmzTarget, unlinkDeveloperIdentityInput, opts)



&lt;p&gt;Unlinks a &lt;code&gt;DeveloperUserIdentifier&lt;/code&gt; from an existing identity. Unlinked developer users will be considered new identities next time they are seen. If, for a given Cognito identity, you remove all federated identities as well as the developer user identifier, the Cognito identity becomes inaccessible.&lt;/p&gt; &lt;p&gt;You must use AWS Developer credentials to call this API.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoIdentity from 'amazon_cognito_identity';
let defaultClient = AmazonCognitoIdentity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoIdentity.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let unlinkDeveloperIdentityInput = new AmazonCognitoIdentity.UnlinkDeveloperIdentityInput(); // UnlinkDeveloperIdentityInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.unlinkDeveloperIdentity(xAmzTarget, unlinkDeveloperIdentityInput, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **unlinkDeveloperIdentityInput** | [**UnlinkDeveloperIdentityInput**](UnlinkDeveloperIdentityInput.md)|  | 
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


## unlinkIdentity

> unlinkIdentity(xAmzTarget, unlinkIdentityInput, opts)



&lt;p&gt;Unlinks a federated identity from an existing account. Unlinked logins will be considered new identities next time they are seen. Removing the last linked login will make this identity inaccessible.&lt;/p&gt; &lt;p&gt;This is a public API. You do not need any credentials to call this API.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoIdentity from 'amazon_cognito_identity';
let defaultClient = AmazonCognitoIdentity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoIdentity.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let unlinkIdentityInput = new AmazonCognitoIdentity.UnlinkIdentityInput(); // UnlinkIdentityInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.unlinkIdentity(xAmzTarget, unlinkIdentityInput, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **unlinkIdentityInput** | [**UnlinkIdentityInput**](UnlinkIdentityInput.md)|  | 
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


## untagResource

> Object untagResource(xAmzTarget, untagResourceInput, opts)



Removes the specified tags from the specified Amazon Cognito identity pool. You can use this action up to 5 times per second, per account

### Example

```javascript
import AmazonCognitoIdentity from 'amazon_cognito_identity';
let defaultClient = AmazonCognitoIdentity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoIdentity.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let untagResourceInput = new AmazonCognitoIdentity.UntagResourceInput(); // UntagResourceInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(xAmzTarget, untagResourceInput, opts, (error, data, response) => {
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
 **untagResourceInput** | [**UntagResourceInput**](UntagResourceInput.md)|  | 
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


## updateIdentityPool

> IdentityPool updateIdentityPool(xAmzTarget, identityPool, opts)



&lt;p&gt;Updates an identity pool.&lt;/p&gt; &lt;p&gt;You must use AWS Developer credentials to call this API.&lt;/p&gt;

### Example

```javascript
import AmazonCognitoIdentity from 'amazon_cognito_identity';
let defaultClient = AmazonCognitoIdentity.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCognitoIdentity.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let identityPool = new AmazonCognitoIdentity.IdentityPool(); // IdentityPool | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateIdentityPool(xAmzTarget, identityPool, opts, (error, data, response) => {
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
 **identityPool** | [**IdentityPool**](IdentityPool.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**IdentityPool**](IdentityPool.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

