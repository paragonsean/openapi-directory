# OpenSearchServiceServerless.DefaultApi

All URIs are relative to *http://aoss.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batchGetCollection**](DefaultApi.md#batchGetCollection) | **POST** /#X-Amz-Target&#x3D;OpenSearchServerless.BatchGetCollection | 
[**batchGetVpcEndpoint**](DefaultApi.md#batchGetVpcEndpoint) | **POST** /#X-Amz-Target&#x3D;OpenSearchServerless.BatchGetVpcEndpoint | 
[**createAccessPolicy**](DefaultApi.md#createAccessPolicy) | **POST** /#X-Amz-Target&#x3D;OpenSearchServerless.CreateAccessPolicy | 
[**createCollection**](DefaultApi.md#createCollection) | **POST** /#X-Amz-Target&#x3D;OpenSearchServerless.CreateCollection | 
[**createSecurityConfig**](DefaultApi.md#createSecurityConfig) | **POST** /#X-Amz-Target&#x3D;OpenSearchServerless.CreateSecurityConfig | 
[**createSecurityPolicy**](DefaultApi.md#createSecurityPolicy) | **POST** /#X-Amz-Target&#x3D;OpenSearchServerless.CreateSecurityPolicy | 
[**createVpcEndpoint**](DefaultApi.md#createVpcEndpoint) | **POST** /#X-Amz-Target&#x3D;OpenSearchServerless.CreateVpcEndpoint | 
[**deleteAccessPolicy**](DefaultApi.md#deleteAccessPolicy) | **POST** /#X-Amz-Target&#x3D;OpenSearchServerless.DeleteAccessPolicy | 
[**deleteCollection**](DefaultApi.md#deleteCollection) | **POST** /#X-Amz-Target&#x3D;OpenSearchServerless.DeleteCollection | 
[**deleteSecurityConfig**](DefaultApi.md#deleteSecurityConfig) | **POST** /#X-Amz-Target&#x3D;OpenSearchServerless.DeleteSecurityConfig | 
[**deleteSecurityPolicy**](DefaultApi.md#deleteSecurityPolicy) | **POST** /#X-Amz-Target&#x3D;OpenSearchServerless.DeleteSecurityPolicy | 
[**deleteVpcEndpoint**](DefaultApi.md#deleteVpcEndpoint) | **POST** /#X-Amz-Target&#x3D;OpenSearchServerless.DeleteVpcEndpoint | 
[**getAccessPolicy**](DefaultApi.md#getAccessPolicy) | **POST** /#X-Amz-Target&#x3D;OpenSearchServerless.GetAccessPolicy | 
[**getAccountSettings**](DefaultApi.md#getAccountSettings) | **POST** /#X-Amz-Target&#x3D;OpenSearchServerless.GetAccountSettings | 
[**getPoliciesStats**](DefaultApi.md#getPoliciesStats) | **POST** /#X-Amz-Target&#x3D;OpenSearchServerless.GetPoliciesStats | 
[**getSecurityConfig**](DefaultApi.md#getSecurityConfig) | **POST** /#X-Amz-Target&#x3D;OpenSearchServerless.GetSecurityConfig | 
[**getSecurityPolicy**](DefaultApi.md#getSecurityPolicy) | **POST** /#X-Amz-Target&#x3D;OpenSearchServerless.GetSecurityPolicy | 
[**listAccessPolicies**](DefaultApi.md#listAccessPolicies) | **POST** /#X-Amz-Target&#x3D;OpenSearchServerless.ListAccessPolicies | 
[**listCollections**](DefaultApi.md#listCollections) | **POST** /#X-Amz-Target&#x3D;OpenSearchServerless.ListCollections | 
[**listSecurityConfigs**](DefaultApi.md#listSecurityConfigs) | **POST** /#X-Amz-Target&#x3D;OpenSearchServerless.ListSecurityConfigs | 
[**listSecurityPolicies**](DefaultApi.md#listSecurityPolicies) | **POST** /#X-Amz-Target&#x3D;OpenSearchServerless.ListSecurityPolicies | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **POST** /#X-Amz-Target&#x3D;OpenSearchServerless.ListTagsForResource | 
[**listVpcEndpoints**](DefaultApi.md#listVpcEndpoints) | **POST** /#X-Amz-Target&#x3D;OpenSearchServerless.ListVpcEndpoints | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /#X-Amz-Target&#x3D;OpenSearchServerless.TagResource | 
[**untagResource**](DefaultApi.md#untagResource) | **POST** /#X-Amz-Target&#x3D;OpenSearchServerless.UntagResource | 
[**updateAccessPolicy**](DefaultApi.md#updateAccessPolicy) | **POST** /#X-Amz-Target&#x3D;OpenSearchServerless.UpdateAccessPolicy | 
[**updateAccountSettings**](DefaultApi.md#updateAccountSettings) | **POST** /#X-Amz-Target&#x3D;OpenSearchServerless.UpdateAccountSettings | 
[**updateCollection**](DefaultApi.md#updateCollection) | **POST** /#X-Amz-Target&#x3D;OpenSearchServerless.UpdateCollection | 
[**updateSecurityConfig**](DefaultApi.md#updateSecurityConfig) | **POST** /#X-Amz-Target&#x3D;OpenSearchServerless.UpdateSecurityConfig | 
[**updateSecurityPolicy**](DefaultApi.md#updateSecurityPolicy) | **POST** /#X-Amz-Target&#x3D;OpenSearchServerless.UpdateSecurityPolicy | 
[**updateVpcEndpoint**](DefaultApi.md#updateVpcEndpoint) | **POST** /#X-Amz-Target&#x3D;OpenSearchServerless.UpdateVpcEndpoint | 



## batchGetCollection

> BatchGetCollectionResponse batchGetCollection(xAmzTarget, batchGetCollectionRequest, opts)



Returns attributes for one or more collections, including the collection endpoint and the OpenSearch Dashboards endpoint. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html\&quot;&gt;Creating and managing Amazon OpenSearch Serverless collections&lt;/a&gt;.

### Example

```javascript
import OpenSearchServiceServerless from 'open_search_service_serverless';
let defaultClient = OpenSearchServiceServerless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new OpenSearchServiceServerless.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let batchGetCollectionRequest = new OpenSearchServiceServerless.BatchGetCollectionRequest(); // BatchGetCollectionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchGetCollection(xAmzTarget, batchGetCollectionRequest, opts, (error, data, response) => {
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
 **batchGetCollectionRequest** | [**BatchGetCollectionRequest**](BatchGetCollectionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchGetCollectionResponse**](BatchGetCollectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchGetVpcEndpoint

> BatchGetVpcEndpointResponse batchGetVpcEndpoint(xAmzTarget, batchGetVpcEndpointRequest, opts)



Returns attributes for one or more VPC endpoints associated with the current account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html\&quot;&gt;Access Amazon OpenSearch Serverless using an interface endpoint&lt;/a&gt;.

### Example

```javascript
import OpenSearchServiceServerless from 'open_search_service_serverless';
let defaultClient = OpenSearchServiceServerless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new OpenSearchServiceServerless.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let batchGetVpcEndpointRequest = new OpenSearchServiceServerless.BatchGetVpcEndpointRequest(); // BatchGetVpcEndpointRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchGetVpcEndpoint(xAmzTarget, batchGetVpcEndpointRequest, opts, (error, data, response) => {
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
 **batchGetVpcEndpointRequest** | [**BatchGetVpcEndpointRequest**](BatchGetVpcEndpointRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchGetVpcEndpointResponse**](BatchGetVpcEndpointResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAccessPolicy

> CreateAccessPolicyResponse createAccessPolicy(xAmzTarget, createAccessPolicyRequest, opts)



Creates a data access policy for OpenSearch Serverless. Access policies limit access to collections and the resources within them, and allow a user to access that data irrespective of the access mechanism or network source. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html\&quot;&gt;Data access control for Amazon OpenSearch Serverless&lt;/a&gt;.

### Example

```javascript
import OpenSearchServiceServerless from 'open_search_service_serverless';
let defaultClient = OpenSearchServiceServerless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new OpenSearchServiceServerless.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createAccessPolicyRequest = new OpenSearchServiceServerless.CreateAccessPolicyRequest(); // CreateAccessPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createAccessPolicy(xAmzTarget, createAccessPolicyRequest, opts, (error, data, response) => {
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
 **createAccessPolicyRequest** | [**CreateAccessPolicyRequest**](CreateAccessPolicyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateAccessPolicyResponse**](CreateAccessPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createCollection

> CreateCollectionResponse createCollection(xAmzTarget, createCollectionRequest, opts)



Creates a new OpenSearch Serverless collection. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html\&quot;&gt;Creating and managing Amazon OpenSearch Serverless collections&lt;/a&gt;.

### Example

```javascript
import OpenSearchServiceServerless from 'open_search_service_serverless';
let defaultClient = OpenSearchServiceServerless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new OpenSearchServiceServerless.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createCollectionRequest = new OpenSearchServiceServerless.CreateCollectionRequest(); // CreateCollectionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createCollection(xAmzTarget, createCollectionRequest, opts, (error, data, response) => {
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
 **createCollectionRequest** | [**CreateCollectionRequest**](CreateCollectionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateCollectionResponse**](CreateCollectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSecurityConfig

> CreateSecurityConfigResponse createSecurityConfig(xAmzTarget, createSecurityConfigRequest, opts)



Specifies a security configuration for OpenSearch Serverless. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html\&quot;&gt;SAML authentication for Amazon OpenSearch Serverless&lt;/a&gt;. 

### Example

```javascript
import OpenSearchServiceServerless from 'open_search_service_serverless';
let defaultClient = OpenSearchServiceServerless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new OpenSearchServiceServerless.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createSecurityConfigRequest = new OpenSearchServiceServerless.CreateSecurityConfigRequest(); // CreateSecurityConfigRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createSecurityConfig(xAmzTarget, createSecurityConfigRequest, opts, (error, data, response) => {
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
 **createSecurityConfigRequest** | [**CreateSecurityConfigRequest**](CreateSecurityConfigRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateSecurityConfigResponse**](CreateSecurityConfigResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSecurityPolicy

> CreateSecurityPolicyResponse createSecurityPolicy(xAmzTarget, createSecurityPolicyRequest, opts)



Creates a security policy to be used by one or more OpenSearch Serverless collections. Security policies provide access to a collection and its OpenSearch Dashboards endpoint from public networks or specific VPC endpoints. They also allow you to secure a collection with a KMS encryption key. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-network.html\&quot;&gt;Network access for Amazon OpenSearch Serverless&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-encryption.html\&quot;&gt;Encryption at rest for Amazon OpenSearch Serverless&lt;/a&gt;.

### Example

```javascript
import OpenSearchServiceServerless from 'open_search_service_serverless';
let defaultClient = OpenSearchServiceServerless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new OpenSearchServiceServerless.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createSecurityPolicyRequest = new OpenSearchServiceServerless.CreateSecurityPolicyRequest(); // CreateSecurityPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createSecurityPolicy(xAmzTarget, createSecurityPolicyRequest, opts, (error, data, response) => {
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
 **createSecurityPolicyRequest** | [**CreateSecurityPolicyRequest**](CreateSecurityPolicyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateSecurityPolicyResponse**](CreateSecurityPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createVpcEndpoint

> CreateVpcEndpointResponse createVpcEndpoint(xAmzTarget, createVpcEndpointRequest, opts)



Creates an OpenSearch Serverless-managed interface VPC endpoint. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html\&quot;&gt;Access Amazon OpenSearch Serverless using an interface endpoint&lt;/a&gt;.

### Example

```javascript
import OpenSearchServiceServerless from 'open_search_service_serverless';
let defaultClient = OpenSearchServiceServerless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new OpenSearchServiceServerless.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createVpcEndpointRequest = new OpenSearchServiceServerless.CreateVpcEndpointRequest(); // CreateVpcEndpointRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createVpcEndpoint(xAmzTarget, createVpcEndpointRequest, opts, (error, data, response) => {
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
 **createVpcEndpointRequest** | [**CreateVpcEndpointRequest**](CreateVpcEndpointRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateVpcEndpointResponse**](CreateVpcEndpointResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAccessPolicy

> Object deleteAccessPolicy(xAmzTarget, deleteAccessPolicyRequest, opts)



Deletes an OpenSearch Serverless access policy. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html\&quot;&gt;Data access control for Amazon OpenSearch Serverless&lt;/a&gt;.

### Example

```javascript
import OpenSearchServiceServerless from 'open_search_service_serverless';
let defaultClient = OpenSearchServiceServerless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new OpenSearchServiceServerless.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteAccessPolicyRequest = new OpenSearchServiceServerless.DeleteAccessPolicyRequest(); // DeleteAccessPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAccessPolicy(xAmzTarget, deleteAccessPolicyRequest, opts, (error, data, response) => {
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
 **deleteAccessPolicyRequest** | [**DeleteAccessPolicyRequest**](DeleteAccessPolicyRequest.md)|  | 
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


## deleteCollection

> DeleteCollectionResponse deleteCollection(xAmzTarget, deleteCollectionRequest, opts)



Deletes an OpenSearch Serverless collection. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html\&quot;&gt;Creating and managing Amazon OpenSearch Serverless collections&lt;/a&gt;.

### Example

```javascript
import OpenSearchServiceServerless from 'open_search_service_serverless';
let defaultClient = OpenSearchServiceServerless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new OpenSearchServiceServerless.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteCollectionRequest = new OpenSearchServiceServerless.DeleteCollectionRequest(); // DeleteCollectionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteCollection(xAmzTarget, deleteCollectionRequest, opts, (error, data, response) => {
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
 **deleteCollectionRequest** | [**DeleteCollectionRequest**](DeleteCollectionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteCollectionResponse**](DeleteCollectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteSecurityConfig

> Object deleteSecurityConfig(xAmzTarget, deleteSecurityConfigRequest, opts)



Deletes a security configuration for OpenSearch Serverless. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html\&quot;&gt;SAML authentication for Amazon OpenSearch Serverless&lt;/a&gt;.

### Example

```javascript
import OpenSearchServiceServerless from 'open_search_service_serverless';
let defaultClient = OpenSearchServiceServerless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new OpenSearchServiceServerless.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteSecurityConfigRequest = new OpenSearchServiceServerless.DeleteSecurityConfigRequest(); // DeleteSecurityConfigRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteSecurityConfig(xAmzTarget, deleteSecurityConfigRequest, opts, (error, data, response) => {
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
 **deleteSecurityConfigRequest** | [**DeleteSecurityConfigRequest**](DeleteSecurityConfigRequest.md)|  | 
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


## deleteSecurityPolicy

> Object deleteSecurityPolicy(xAmzTarget, deleteSecurityPolicyRequest, opts)



Deletes an OpenSearch Serverless security policy.

### Example

```javascript
import OpenSearchServiceServerless from 'open_search_service_serverless';
let defaultClient = OpenSearchServiceServerless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new OpenSearchServiceServerless.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteSecurityPolicyRequest = new OpenSearchServiceServerless.DeleteSecurityPolicyRequest(); // DeleteSecurityPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteSecurityPolicy(xAmzTarget, deleteSecurityPolicyRequest, opts, (error, data, response) => {
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
 **deleteSecurityPolicyRequest** | [**DeleteSecurityPolicyRequest**](DeleteSecurityPolicyRequest.md)|  | 
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


## deleteVpcEndpoint

> DeleteVpcEndpointResponse deleteVpcEndpoint(xAmzTarget, deleteVpcEndpointRequest, opts)



Deletes an OpenSearch Serverless-managed interface endpoint. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html\&quot;&gt;Access Amazon OpenSearch Serverless using an interface endpoint&lt;/a&gt;.

### Example

```javascript
import OpenSearchServiceServerless from 'open_search_service_serverless';
let defaultClient = OpenSearchServiceServerless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new OpenSearchServiceServerless.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteVpcEndpointRequest = new OpenSearchServiceServerless.DeleteVpcEndpointRequest(); // DeleteVpcEndpointRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteVpcEndpoint(xAmzTarget, deleteVpcEndpointRequest, opts, (error, data, response) => {
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
 **deleteVpcEndpointRequest** | [**DeleteVpcEndpointRequest**](DeleteVpcEndpointRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteVpcEndpointResponse**](DeleteVpcEndpointResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAccessPolicy

> GetAccessPolicyResponse getAccessPolicy(xAmzTarget, getAccessPolicyRequest, opts)



Returns an OpenSearch Serverless access policy. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html\&quot;&gt;Data access control for Amazon OpenSearch Serverless&lt;/a&gt;.

### Example

```javascript
import OpenSearchServiceServerless from 'open_search_service_serverless';
let defaultClient = OpenSearchServiceServerless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new OpenSearchServiceServerless.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getAccessPolicyRequest = new OpenSearchServiceServerless.GetAccessPolicyRequest(); // GetAccessPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAccessPolicy(xAmzTarget, getAccessPolicyRequest, opts, (error, data, response) => {
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
 **getAccessPolicyRequest** | [**GetAccessPolicyRequest**](GetAccessPolicyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAccessPolicyResponse**](GetAccessPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAccountSettings

> GetAccountSettingsResponse getAccountSettings(xAmzTarget, body, opts)



Returns account-level settings related to OpenSearch Serverless.

### Example

```javascript
import OpenSearchServiceServerless from 'open_search_service_serverless';
let defaultClient = OpenSearchServiceServerless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new OpenSearchServiceServerless.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let body = {key: null}; // Object | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAccountSettings(xAmzTarget, body, opts, (error, data, response) => {
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
 **body** | **Object**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAccountSettingsResponse**](GetAccountSettingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getPoliciesStats

> GetPoliciesStatsResponse getPoliciesStats(xAmzTarget, body, opts)



Returns statistical information about your OpenSearch Serverless access policies, security configurations, and security policies.

### Example

```javascript
import OpenSearchServiceServerless from 'open_search_service_serverless';
let defaultClient = OpenSearchServiceServerless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new OpenSearchServiceServerless.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let body = {key: null}; // Object | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getPoliciesStats(xAmzTarget, body, opts, (error, data, response) => {
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
 **body** | **Object**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetPoliciesStatsResponse**](GetPoliciesStatsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getSecurityConfig

> GetSecurityConfigResponse getSecurityConfig(xAmzTarget, getSecurityConfigRequest, opts)



Returns information about an OpenSearch Serverless security configuration. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html\&quot;&gt;SAML authentication for Amazon OpenSearch Serverless&lt;/a&gt;.

### Example

```javascript
import OpenSearchServiceServerless from 'open_search_service_serverless';
let defaultClient = OpenSearchServiceServerless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new OpenSearchServiceServerless.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getSecurityConfigRequest = new OpenSearchServiceServerless.GetSecurityConfigRequest(); // GetSecurityConfigRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSecurityConfig(xAmzTarget, getSecurityConfigRequest, opts, (error, data, response) => {
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
 **getSecurityConfigRequest** | [**GetSecurityConfigRequest**](GetSecurityConfigRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSecurityConfigResponse**](GetSecurityConfigResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getSecurityPolicy

> GetSecurityPolicyResponse getSecurityPolicy(xAmzTarget, getSecurityPolicyRequest, opts)



Returns information about a configured OpenSearch Serverless security policy. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-network.html\&quot;&gt;Network access for Amazon OpenSearch Serverless&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-encryption.html\&quot;&gt;Encryption at rest for Amazon OpenSearch Serverless&lt;/a&gt;.

### Example

```javascript
import OpenSearchServiceServerless from 'open_search_service_serverless';
let defaultClient = OpenSearchServiceServerless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new OpenSearchServiceServerless.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getSecurityPolicyRequest = new OpenSearchServiceServerless.GetSecurityPolicyRequest(); // GetSecurityPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSecurityPolicy(xAmzTarget, getSecurityPolicyRequest, opts, (error, data, response) => {
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
 **getSecurityPolicyRequest** | [**GetSecurityPolicyRequest**](GetSecurityPolicyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSecurityPolicyResponse**](GetSecurityPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listAccessPolicies

> ListAccessPoliciesResponse listAccessPolicies(xAmzTarget, listAccessPoliciesRequest, opts)



Returns information about a list of OpenSearch Serverless access policies.

### Example

```javascript
import OpenSearchServiceServerless from 'open_search_service_serverless';
let defaultClient = OpenSearchServiceServerless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new OpenSearchServiceServerless.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listAccessPoliciesRequest = new OpenSearchServiceServerless.ListAccessPoliciesRequest(); // ListAccessPoliciesRequest | 
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
apiInstance.listAccessPolicies(xAmzTarget, listAccessPoliciesRequest, opts, (error, data, response) => {
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
 **listAccessPoliciesRequest** | [**ListAccessPoliciesRequest**](ListAccessPoliciesRequest.md)|  | 
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

[**ListAccessPoliciesResponse**](ListAccessPoliciesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listCollections

> ListCollectionsResponse listCollections(xAmzTarget, listCollectionsRequest, opts)



&lt;p&gt;Lists all OpenSearch Serverless collections. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html\&quot;&gt;Creating and managing Amazon OpenSearch Serverless collections&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Make sure to include an empty request body {} if you don&#39;t include any collection filters in the request.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import OpenSearchServiceServerless from 'open_search_service_serverless';
let defaultClient = OpenSearchServiceServerless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new OpenSearchServiceServerless.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listCollectionsRequest = new OpenSearchServiceServerless.ListCollectionsRequest(); // ListCollectionsRequest | 
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
apiInstance.listCollections(xAmzTarget, listCollectionsRequest, opts, (error, data, response) => {
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
 **listCollectionsRequest** | [**ListCollectionsRequest**](ListCollectionsRequest.md)|  | 
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

[**ListCollectionsResponse**](ListCollectionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listSecurityConfigs

> ListSecurityConfigsResponse listSecurityConfigs(xAmzTarget, listSecurityConfigsRequest, opts)



Returns information about configured OpenSearch Serverless security configurations. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html\&quot;&gt;SAML authentication for Amazon OpenSearch Serverless&lt;/a&gt;.

### Example

```javascript
import OpenSearchServiceServerless from 'open_search_service_serverless';
let defaultClient = OpenSearchServiceServerless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new OpenSearchServiceServerless.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listSecurityConfigsRequest = new OpenSearchServiceServerless.ListSecurityConfigsRequest(); // ListSecurityConfigsRequest | 
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
apiInstance.listSecurityConfigs(xAmzTarget, listSecurityConfigsRequest, opts, (error, data, response) => {
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
 **listSecurityConfigsRequest** | [**ListSecurityConfigsRequest**](ListSecurityConfigsRequest.md)|  | 
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

[**ListSecurityConfigsResponse**](ListSecurityConfigsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listSecurityPolicies

> ListSecurityPoliciesResponse listSecurityPolicies(xAmzTarget, listSecurityPoliciesRequest, opts)



Returns information about configured OpenSearch Serverless security policies.

### Example

```javascript
import OpenSearchServiceServerless from 'open_search_service_serverless';
let defaultClient = OpenSearchServiceServerless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new OpenSearchServiceServerless.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listSecurityPoliciesRequest = new OpenSearchServiceServerless.ListSecurityPoliciesRequest(); // ListSecurityPoliciesRequest | 
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
apiInstance.listSecurityPolicies(xAmzTarget, listSecurityPoliciesRequest, opts, (error, data, response) => {
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
 **listSecurityPoliciesRequest** | [**ListSecurityPoliciesRequest**](ListSecurityPoliciesRequest.md)|  | 
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

[**ListSecurityPoliciesResponse**](ListSecurityPoliciesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(xAmzTarget, listTagsForResourceRequest, opts)



Returns the tags for an OpenSearch Serverless resource. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/tag-collection.html\&quot;&gt;Tagging Amazon OpenSearch Serverless collections&lt;/a&gt;.

### Example

```javascript
import OpenSearchServiceServerless from 'open_search_service_serverless';
let defaultClient = OpenSearchServiceServerless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new OpenSearchServiceServerless.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listTagsForResourceRequest = new OpenSearchServiceServerless.ListTagsForResourceRequest(); // ListTagsForResourceRequest | 
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


## listVpcEndpoints

> ListVpcEndpointsResponse listVpcEndpoints(xAmzTarget, listVpcEndpointsRequest, opts)



Returns the OpenSearch Serverless-managed interface VPC endpoints associated with the current account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html\&quot;&gt;Access Amazon OpenSearch Serverless using an interface endpoint&lt;/a&gt;.

### Example

```javascript
import OpenSearchServiceServerless from 'open_search_service_serverless';
let defaultClient = OpenSearchServiceServerless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new OpenSearchServiceServerless.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listVpcEndpointsRequest = new OpenSearchServiceServerless.ListVpcEndpointsRequest(); // ListVpcEndpointsRequest | 
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
apiInstance.listVpcEndpoints(xAmzTarget, listVpcEndpointsRequest, opts, (error, data, response) => {
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
 **listVpcEndpointsRequest** | [**ListVpcEndpointsRequest**](ListVpcEndpointsRequest.md)|  | 
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

[**ListVpcEndpointsResponse**](ListVpcEndpointsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(xAmzTarget, tagResourceRequest, opts)



Associates tags with an OpenSearch Serverless resource. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/tag-collection.html\&quot;&gt;Tagging Amazon OpenSearch Serverless collections&lt;/a&gt;.

### Example

```javascript
import OpenSearchServiceServerless from 'open_search_service_serverless';
let defaultClient = OpenSearchServiceServerless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new OpenSearchServiceServerless.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let tagResourceRequest = new OpenSearchServiceServerless.TagResourceRequest(); // TagResourceRequest | 
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



Removes a tag or set of tags from an OpenSearch Serverless resource. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/tag-collection.html\&quot;&gt;Tagging Amazon OpenSearch Serverless collections&lt;/a&gt;.

### Example

```javascript
import OpenSearchServiceServerless from 'open_search_service_serverless';
let defaultClient = OpenSearchServiceServerless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new OpenSearchServiceServerless.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let untagResourceRequest = new OpenSearchServiceServerless.UntagResourceRequest(); // UntagResourceRequest | 
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


## updateAccessPolicy

> UpdateAccessPolicyResponse updateAccessPolicy(xAmzTarget, updateAccessPolicyRequest, opts)



Updates an OpenSearch Serverless access policy. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html\&quot;&gt;Data access control for Amazon OpenSearch Serverless&lt;/a&gt;.

### Example

```javascript
import OpenSearchServiceServerless from 'open_search_service_serverless';
let defaultClient = OpenSearchServiceServerless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new OpenSearchServiceServerless.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateAccessPolicyRequest = new OpenSearchServiceServerless.UpdateAccessPolicyRequest(); // UpdateAccessPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAccessPolicy(xAmzTarget, updateAccessPolicyRequest, opts, (error, data, response) => {
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
 **updateAccessPolicyRequest** | [**UpdateAccessPolicyRequest**](UpdateAccessPolicyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateAccessPolicyResponse**](UpdateAccessPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateAccountSettings

> UpdateAccountSettingsResponse updateAccountSettings(xAmzTarget, updateAccountSettingsRequest, opts)



Update the OpenSearch Serverless settings for the current Amazon Web Services account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-scaling.html\&quot;&gt;Managing capacity limits for Amazon OpenSearch Serverless&lt;/a&gt;.

### Example

```javascript
import OpenSearchServiceServerless from 'open_search_service_serverless';
let defaultClient = OpenSearchServiceServerless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new OpenSearchServiceServerless.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateAccountSettingsRequest = new OpenSearchServiceServerless.UpdateAccountSettingsRequest(); // UpdateAccountSettingsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAccountSettings(xAmzTarget, updateAccountSettingsRequest, opts, (error, data, response) => {
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
 **updateAccountSettingsRequest** | [**UpdateAccountSettingsRequest**](UpdateAccountSettingsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateAccountSettingsResponse**](UpdateAccountSettingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateCollection

> UpdateCollectionResponse updateCollection(xAmzTarget, updateCollectionRequest, opts)



Updates an OpenSearch Serverless collection.

### Example

```javascript
import OpenSearchServiceServerless from 'open_search_service_serverless';
let defaultClient = OpenSearchServiceServerless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new OpenSearchServiceServerless.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateCollectionRequest = new OpenSearchServiceServerless.UpdateCollectionRequest(); // UpdateCollectionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateCollection(xAmzTarget, updateCollectionRequest, opts, (error, data, response) => {
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
 **updateCollectionRequest** | [**UpdateCollectionRequest**](UpdateCollectionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateCollectionResponse**](UpdateCollectionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSecurityConfig

> UpdateSecurityConfigResponse updateSecurityConfig(xAmzTarget, updateSecurityConfigRequest, opts)



Updates a security configuration for OpenSearch Serverless. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html\&quot;&gt;SAML authentication for Amazon OpenSearch Serverless&lt;/a&gt;.

### Example

```javascript
import OpenSearchServiceServerless from 'open_search_service_serverless';
let defaultClient = OpenSearchServiceServerless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new OpenSearchServiceServerless.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateSecurityConfigRequest = new OpenSearchServiceServerless.UpdateSecurityConfigRequest(); // UpdateSecurityConfigRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateSecurityConfig(xAmzTarget, updateSecurityConfigRequest, opts, (error, data, response) => {
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
 **updateSecurityConfigRequest** | [**UpdateSecurityConfigRequest**](UpdateSecurityConfigRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateSecurityConfigResponse**](UpdateSecurityConfigResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSecurityPolicy

> UpdateSecurityPolicyResponse updateSecurityPolicy(xAmzTarget, updateSecurityPolicyRequest, opts)



Updates an OpenSearch Serverless security policy. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-network.html\&quot;&gt;Network access for Amazon OpenSearch Serverless&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-encryption.html\&quot;&gt;Encryption at rest for Amazon OpenSearch Serverless&lt;/a&gt;.

### Example

```javascript
import OpenSearchServiceServerless from 'open_search_service_serverless';
let defaultClient = OpenSearchServiceServerless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new OpenSearchServiceServerless.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateSecurityPolicyRequest = new OpenSearchServiceServerless.UpdateSecurityPolicyRequest(); // UpdateSecurityPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateSecurityPolicy(xAmzTarget, updateSecurityPolicyRequest, opts, (error, data, response) => {
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
 **updateSecurityPolicyRequest** | [**UpdateSecurityPolicyRequest**](UpdateSecurityPolicyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateSecurityPolicyResponse**](UpdateSecurityPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateVpcEndpoint

> UpdateVpcEndpointResponse updateVpcEndpoint(xAmzTarget, updateVpcEndpointRequest, opts)



Updates an OpenSearch Serverless-managed interface endpoint. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html\&quot;&gt;Access Amazon OpenSearch Serverless using an interface endpoint&lt;/a&gt;.

### Example

```javascript
import OpenSearchServiceServerless from 'open_search_service_serverless';
let defaultClient = OpenSearchServiceServerless.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new OpenSearchServiceServerless.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateVpcEndpointRequest = new OpenSearchServiceServerless.UpdateVpcEndpointRequest(); // UpdateVpcEndpointRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateVpcEndpoint(xAmzTarget, updateVpcEndpointRequest, opts, (error, data, response) => {
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
 **updateVpcEndpointRequest** | [**UpdateVpcEndpointRequest**](UpdateVpcEndpointRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateVpcEndpointResponse**](UpdateVpcEndpointResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

