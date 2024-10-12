# AmazonManagedGrafana.DefaultApi

All URIs are relative to *http://grafana.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associateLicense**](DefaultApi.md#associateLicense) | **POST** /workspaces/{workspaceId}/licenses/{licenseType} | 
[**createWorkspace**](DefaultApi.md#createWorkspace) | **POST** /workspaces | 
[**createWorkspaceApiKey**](DefaultApi.md#createWorkspaceApiKey) | **POST** /workspaces/{workspaceId}/apikeys | 
[**deleteWorkspace**](DefaultApi.md#deleteWorkspace) | **DELETE** /workspaces/{workspaceId} | 
[**deleteWorkspaceApiKey**](DefaultApi.md#deleteWorkspaceApiKey) | **DELETE** /workspaces/{workspaceId}/apikeys/{keyName} | 
[**describeWorkspace**](DefaultApi.md#describeWorkspace) | **GET** /workspaces/{workspaceId} | 
[**describeWorkspaceAuthentication**](DefaultApi.md#describeWorkspaceAuthentication) | **GET** /workspaces/{workspaceId}/authentication | 
[**describeWorkspaceConfiguration**](DefaultApi.md#describeWorkspaceConfiguration) | **GET** /workspaces/{workspaceId}/configuration | 
[**disassociateLicense**](DefaultApi.md#disassociateLicense) | **DELETE** /workspaces/{workspaceId}/licenses/{licenseType} | 
[**listPermissions**](DefaultApi.md#listPermissions) | **GET** /workspaces/{workspaceId}/permissions | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} | 
[**listVersions**](DefaultApi.md#listVersions) | **GET** /versions | 
[**listWorkspaces**](DefaultApi.md#listWorkspaces) | **GET** /workspaces | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys | 
[**updatePermissions**](DefaultApi.md#updatePermissions) | **PATCH** /workspaces/{workspaceId}/permissions | 
[**updateWorkspace**](DefaultApi.md#updateWorkspace) | **PUT** /workspaces/{workspaceId} | 
[**updateWorkspaceAuthentication**](DefaultApi.md#updateWorkspaceAuthentication) | **POST** /workspaces/{workspaceId}/authentication | 
[**updateWorkspaceConfiguration**](DefaultApi.md#updateWorkspaceConfiguration) | **PUT** /workspaces/{workspaceId}/configuration | 



## associateLicense

> AssociateLicenseResponse associateLicense(licenseType, workspaceId, opts)



Assigns a Grafana Enterprise license to a workspace. Upgrading to Grafana Enterprise incurs additional fees. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/grafana/latest/userguide/upgrade-to-Grafana-Enterprise.html\&quot;&gt;Upgrade a workspace to Grafana Enterprise&lt;/a&gt;.

### Example

```javascript
import AmazonManagedGrafana from 'amazon_managed_grafana';
let defaultClient = AmazonManagedGrafana.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonManagedGrafana.DefaultApi();
let licenseType = "licenseType_example"; // String | The type of license to associate with the workspace.
let workspaceId = "workspaceId_example"; // String | The ID of the workspace to associate the license with.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateLicense(licenseType, workspaceId, opts, (error, data, response) => {
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
 **licenseType** | **String**| The type of license to associate with the workspace. | 
 **workspaceId** | **String**| The ID of the workspace to associate the license with. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AssociateLicenseResponse**](AssociateLicenseResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createWorkspace

> CreateWorkspaceResponse createWorkspace(createWorkspaceRequest, opts)



&lt;p&gt;Creates a &lt;i&gt;workspace&lt;/i&gt;. In a workspace, you can create Grafana dashboards and visualizations to analyze your metrics, logs, and traces. You don&#39;t have to build, package, or deploy any hardware to run the Grafana server.&lt;/p&gt; &lt;p&gt;Don&#39;t use &lt;code&gt;CreateWorkspace&lt;/code&gt; to modify an existing workspace. Instead, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdateWorkspace.html\&quot;&gt;UpdateWorkspace&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonManagedGrafana from 'amazon_managed_grafana';
let defaultClient = AmazonManagedGrafana.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonManagedGrafana.DefaultApi();
let createWorkspaceRequest = new AmazonManagedGrafana.CreateWorkspaceRequest(); // CreateWorkspaceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createWorkspace(createWorkspaceRequest, opts, (error, data, response) => {
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
 **createWorkspaceRequest** | [**CreateWorkspaceRequest**](CreateWorkspaceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateWorkspaceResponse**](CreateWorkspaceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createWorkspaceApiKey

> CreateWorkspaceApiKeyResponse createWorkspaceApiKey(workspaceId, createWorkspaceApiKeyRequest, opts)



Creates a Grafana API key for the workspace. This key can be used to authenticate requests sent to the workspace&#39;s HTTP API. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/grafana/latest/userguide/Using-Grafana-APIs.html\&quot;&gt;https://docs.aws.amazon.com/grafana/latest/userguide/Using-Grafana-APIs.html&lt;/a&gt; for available APIs and example requests.

### Example

```javascript
import AmazonManagedGrafana from 'amazon_managed_grafana';
let defaultClient = AmazonManagedGrafana.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonManagedGrafana.DefaultApi();
let workspaceId = "workspaceId_example"; // String | The ID of the workspace to create an API key.
let createWorkspaceApiKeyRequest = new AmazonManagedGrafana.CreateWorkspaceApiKeyRequest(); // CreateWorkspaceApiKeyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createWorkspaceApiKey(workspaceId, createWorkspaceApiKeyRequest, opts, (error, data, response) => {
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
 **workspaceId** | **String**| The ID of the workspace to create an API key. | 
 **createWorkspaceApiKeyRequest** | [**CreateWorkspaceApiKeyRequest**](CreateWorkspaceApiKeyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateWorkspaceApiKeyResponse**](CreateWorkspaceApiKeyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteWorkspace

> DeleteWorkspaceResponse deleteWorkspace(workspaceId, opts)



Deletes an Amazon Managed Grafana workspace.

### Example

```javascript
import AmazonManagedGrafana from 'amazon_managed_grafana';
let defaultClient = AmazonManagedGrafana.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonManagedGrafana.DefaultApi();
let workspaceId = "workspaceId_example"; // String | The ID of the workspace to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteWorkspace(workspaceId, opts, (error, data, response) => {
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
 **workspaceId** | **String**| The ID of the workspace to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteWorkspaceResponse**](DeleteWorkspaceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteWorkspaceApiKey

> DeleteWorkspaceApiKeyResponse deleteWorkspaceApiKey(keyName, workspaceId, opts)



Deletes a Grafana API key for the workspace.

### Example

```javascript
import AmazonManagedGrafana from 'amazon_managed_grafana';
let defaultClient = AmazonManagedGrafana.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonManagedGrafana.DefaultApi();
let keyName = "keyName_example"; // String | The name of the API key to delete.
let workspaceId = "workspaceId_example"; // String | The ID of the workspace to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteWorkspaceApiKey(keyName, workspaceId, opts, (error, data, response) => {
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
 **keyName** | **String**| The name of the API key to delete. | 
 **workspaceId** | **String**| The ID of the workspace to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteWorkspaceApiKeyResponse**](DeleteWorkspaceApiKeyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeWorkspace

> DescribeWorkspaceResponse describeWorkspace(workspaceId, opts)



Displays information about one Amazon Managed Grafana workspace.

### Example

```javascript
import AmazonManagedGrafana from 'amazon_managed_grafana';
let defaultClient = AmazonManagedGrafana.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonManagedGrafana.DefaultApi();
let workspaceId = "workspaceId_example"; // String | The ID of the workspace to display information about.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeWorkspace(workspaceId, opts, (error, data, response) => {
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
 **workspaceId** | **String**| The ID of the workspace to display information about. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeWorkspaceResponse**](DescribeWorkspaceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeWorkspaceAuthentication

> DescribeWorkspaceAuthenticationResponse describeWorkspaceAuthentication(workspaceId, opts)



Displays information about the authentication methods used in one Amazon Managed Grafana workspace.

### Example

```javascript
import AmazonManagedGrafana from 'amazon_managed_grafana';
let defaultClient = AmazonManagedGrafana.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonManagedGrafana.DefaultApi();
let workspaceId = "workspaceId_example"; // String | The ID of the workspace to return authentication information about.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeWorkspaceAuthentication(workspaceId, opts, (error, data, response) => {
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
 **workspaceId** | **String**| The ID of the workspace to return authentication information about. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeWorkspaceAuthenticationResponse**](DescribeWorkspaceAuthenticationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeWorkspaceConfiguration

> DescribeWorkspaceConfigurationResponse describeWorkspaceConfiguration(workspaceId, opts)



Gets the current configuration string for the given workspace.

### Example

```javascript
import AmazonManagedGrafana from 'amazon_managed_grafana';
let defaultClient = AmazonManagedGrafana.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonManagedGrafana.DefaultApi();
let workspaceId = "workspaceId_example"; // String | The ID of the workspace to get configuration information for.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeWorkspaceConfiguration(workspaceId, opts, (error, data, response) => {
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
 **workspaceId** | **String**| The ID of the workspace to get configuration information for. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeWorkspaceConfigurationResponse**](DescribeWorkspaceConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disassociateLicense

> DisassociateLicenseResponse disassociateLicense(licenseType, workspaceId, opts)



Removes the Grafana Enterprise license from a workspace.

### Example

```javascript
import AmazonManagedGrafana from 'amazon_managed_grafana';
let defaultClient = AmazonManagedGrafana.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonManagedGrafana.DefaultApi();
let licenseType = "licenseType_example"; // String | The type of license to remove from the workspace.
let workspaceId = "workspaceId_example"; // String | The ID of the workspace to remove the Grafana Enterprise license from.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateLicense(licenseType, workspaceId, opts, (error, data, response) => {
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
 **licenseType** | **String**| The type of license to remove from the workspace. | 
 **workspaceId** | **String**| The ID of the workspace to remove the Grafana Enterprise license from. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DisassociateLicenseResponse**](DisassociateLicenseResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPermissions

> ListPermissionsResponse listPermissions(workspaceId, opts)



Lists the users and groups who have the Grafana &lt;code&gt;Admin&lt;/code&gt; and &lt;code&gt;Editor&lt;/code&gt; roles in this workspace. If you use this operation without specifying &lt;code&gt;userId&lt;/code&gt; or &lt;code&gt;groupId&lt;/code&gt;, the operation returns the roles of all users and groups. If you specify a &lt;code&gt;userId&lt;/code&gt; or a &lt;code&gt;groupId&lt;/code&gt;, only the roles for that user or group are returned. If you do this, you can specify only one &lt;code&gt;userId&lt;/code&gt; or one &lt;code&gt;groupId&lt;/code&gt;.

### Example

```javascript
import AmazonManagedGrafana from 'amazon_managed_grafana';
let defaultClient = AmazonManagedGrafana.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonManagedGrafana.DefaultApi();
let workspaceId = "workspaceId_example"; // String | The ID of the workspace to list permissions for. This parameter is required.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'groupId': "groupId_example", // String | (Optional) Limits the results to only the group that matches this ID.
  'maxResults': 56, // Number | The maximum number of results to include in the response.
  'nextToken': "nextToken_example", // String | The token to use when requesting the next set of results. You received this token from a previous <code>ListPermissions</code> operation.
  'userId': "userId_example", // String | (Optional) Limits the results to only the user that matches this ID.
  'userType': "userType_example" // String | (Optional) If you specify <code>SSO_USER</code>, then only the permissions of IAM Identity Center users are returned. If you specify <code>SSO_GROUP</code>, only the permissions of IAM Identity Center groups are returned.
};
apiInstance.listPermissions(workspaceId, opts, (error, data, response) => {
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
 **workspaceId** | **String**| The ID of the workspace to list permissions for. This parameter is required. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **groupId** | **String**| (Optional) Limits the results to only the group that matches this ID. | [optional] 
 **maxResults** | **Number**| The maximum number of results to include in the response. | [optional] 
 **nextToken** | **String**| The token to use when requesting the next set of results. You received this token from a previous &lt;code&gt;ListPermissions&lt;/code&gt; operation. | [optional] 
 **userId** | **String**| (Optional) Limits the results to only the user that matches this ID. | [optional] 
 **userType** | **String**| (Optional) If you specify &lt;code&gt;SSO_USER&lt;/code&gt;, then only the permissions of IAM Identity Center users are returned. If you specify &lt;code&gt;SSO_GROUP&lt;/code&gt;, only the permissions of IAM Identity Center groups are returned. | [optional] 

### Return type

[**ListPermissionsResponse**](ListPermissionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



The &lt;code&gt;ListTagsForResource&lt;/code&gt; operation returns the tags that are associated with the Amazon Managed Service for Grafana resource specified by the &lt;code&gt;resourceArn&lt;/code&gt;. Currently, the only resource that can be tagged is a workspace. 

### Example

```javascript
import AmazonManagedGrafana from 'amazon_managed_grafana';
let defaultClient = AmazonManagedGrafana.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonManagedGrafana.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the resource the list of tags are associated with.
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
 **resourceArn** | **String**| The ARN of the resource the list of tags are associated with. | 
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


## listVersions

> ListVersionsResponse listVersions(opts)



Lists available versions of Grafana. These are available when calling &lt;code&gt;CreateWorkspace&lt;/code&gt;. Optionally, include a workspace to list the versions to which it can be upgraded.

### Example

```javascript
import AmazonManagedGrafana from 'amazon_managed_grafana';
let defaultClient = AmazonManagedGrafana.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonManagedGrafana.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to include in the response.
  'nextToken': "nextToken_example", // String | The token to use when requesting the next set of results. You receive this token from a previous <code>ListVersions</code> operation.
  'workspaceId': "workspaceId_example" // String | The ID of the workspace to list the available upgrade versions. If not included, lists all versions of Grafana that are supported for <code>CreateWorkspace</code>.
};
apiInstance.listVersions(opts, (error, data, response) => {
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
 **maxResults** | **Number**| The maximum number of results to include in the response. | [optional] 
 **nextToken** | **String**| The token to use when requesting the next set of results. You receive this token from a previous &lt;code&gt;ListVersions&lt;/code&gt; operation. | [optional] 
 **workspaceId** | **String**| The ID of the workspace to list the available upgrade versions. If not included, lists all versions of Grafana that are supported for &lt;code&gt;CreateWorkspace&lt;/code&gt;. | [optional] 

### Return type

[**ListVersionsResponse**](ListVersionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listWorkspaces

> ListWorkspacesResponse listWorkspaces(opts)



Returns a list of Amazon Managed Grafana workspaces in the account, with some information about each workspace. For more complete information about one workspace, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AAMG/latest/APIReference/API_DescribeWorkspace.html\&quot;&gt;DescribeWorkspace&lt;/a&gt;.

### Example

```javascript
import AmazonManagedGrafana from 'amazon_managed_grafana';
let defaultClient = AmazonManagedGrafana.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonManagedGrafana.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of workspaces to include in the results.
  'nextToken': "nextToken_example" // String | The token for the next set of workspaces to return. (You receive this token from a previous <code>ListWorkspaces</code> operation.)
};
apiInstance.listWorkspaces(opts, (error, data, response) => {
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
 **maxResults** | **Number**| The maximum number of workspaces to include in the results. | [optional] 
 **nextToken** | **String**| The token for the next set of workspaces to return. (You receive this token from a previous &lt;code&gt;ListWorkspaces&lt;/code&gt; operation.) | [optional] 

### Return type

[**ListWorkspacesResponse**](ListWorkspacesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



&lt;p&gt;The &lt;code&gt;TagResource&lt;/code&gt; operation associates tags with an Amazon Managed Grafana resource. Currently, the only resource that can be tagged is workspaces. &lt;/p&gt; &lt;p&gt;If you specify a new tag key for the resource, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.&lt;/p&gt;

### Example

```javascript
import AmazonManagedGrafana from 'amazon_managed_grafana';
let defaultClient = AmazonManagedGrafana.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonManagedGrafana.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the resource the tag is associated with.
let tagResourceRequest = new AmazonManagedGrafana.TagResourceRequest(); // TagResourceRequest | 
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
 **resourceArn** | **String**| The ARN of the resource the tag is associated with. | 
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



The &lt;code&gt;UntagResource&lt;/code&gt; operation removes the association of the tag with the Amazon Managed Grafana resource. 

### Example

```javascript
import AmazonManagedGrafana from 'amazon_managed_grafana';
let defaultClient = AmazonManagedGrafana.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonManagedGrafana.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the resource the tag association is removed from. 
let tagKeys = ["null"]; // [String] | The key values of the tag to be removed from the resource.
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
 **resourceArn** | **String**| The ARN of the resource the tag association is removed from.  | 
 **tagKeys** | [**[String]**](String.md)| The key values of the tag to be removed from the resource. | 
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


## updatePermissions

> UpdatePermissionsResponse updatePermissions(workspaceId, updatePermissionsRequest, opts)



Updates which users in a workspace have the Grafana &lt;code&gt;Admin&lt;/code&gt; or &lt;code&gt;Editor&lt;/code&gt; roles.

### Example

```javascript
import AmazonManagedGrafana from 'amazon_managed_grafana';
let defaultClient = AmazonManagedGrafana.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonManagedGrafana.DefaultApi();
let workspaceId = "workspaceId_example"; // String | The ID of the workspace to update.
let updatePermissionsRequest = new AmazonManagedGrafana.UpdatePermissionsRequest(); // UpdatePermissionsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updatePermissions(workspaceId, updatePermissionsRequest, opts, (error, data, response) => {
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
 **workspaceId** | **String**| The ID of the workspace to update. | 
 **updatePermissionsRequest** | [**UpdatePermissionsRequest**](UpdatePermissionsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdatePermissionsResponse**](UpdatePermissionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateWorkspace

> UpdateWorkspaceResponse updateWorkspace(workspaceId, updateWorkspaceRequest, opts)



&lt;p&gt;Modifies an existing Amazon Managed Grafana workspace. If you use this operation and omit any optional parameters, the existing values of those parameters are not changed.&lt;/p&gt; &lt;p&gt;To modify the user authentication methods that the workspace uses, such as SAML or IAM Identity Center, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdateWorkspaceAuthentication.html\&quot;&gt;UpdateWorkspaceAuthentication&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To modify which users in the workspace have the &lt;code&gt;Admin&lt;/code&gt; and &lt;code&gt;Editor&lt;/code&gt; Grafana roles, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdatePermissions.html\&quot;&gt;UpdatePermissions&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonManagedGrafana from 'amazon_managed_grafana';
let defaultClient = AmazonManagedGrafana.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonManagedGrafana.DefaultApi();
let workspaceId = "workspaceId_example"; // String | The ID of the workspace to update.
let updateWorkspaceRequest = new AmazonManagedGrafana.UpdateWorkspaceRequest(); // UpdateWorkspaceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateWorkspace(workspaceId, updateWorkspaceRequest, opts, (error, data, response) => {
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
 **workspaceId** | **String**| The ID of the workspace to update. | 
 **updateWorkspaceRequest** | [**UpdateWorkspaceRequest**](UpdateWorkspaceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateWorkspaceResponse**](UpdateWorkspaceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateWorkspaceAuthentication

> UpdateWorkspaceAuthenticationResponse updateWorkspaceAuthentication(workspaceId, updateWorkspaceAuthenticationRequest, opts)



&lt;p&gt;Use this operation to define the identity provider (IdP) that this workspace authenticates users from, using SAML. You can also map SAML assertion attributes to workspace user information and define which groups in the assertion attribute are to have the &lt;code&gt;Admin&lt;/code&gt; and &lt;code&gt;Editor&lt;/code&gt; roles in the workspace.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Changes to the authentication method for a workspace may take a few minutes to take effect.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonManagedGrafana from 'amazon_managed_grafana';
let defaultClient = AmazonManagedGrafana.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonManagedGrafana.DefaultApi();
let workspaceId = "workspaceId_example"; // String | The ID of the workspace to update the authentication for.
let updateWorkspaceAuthenticationRequest = new AmazonManagedGrafana.UpdateWorkspaceAuthenticationRequest(); // UpdateWorkspaceAuthenticationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateWorkspaceAuthentication(workspaceId, updateWorkspaceAuthenticationRequest, opts, (error, data, response) => {
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
 **workspaceId** | **String**| The ID of the workspace to update the authentication for. | 
 **updateWorkspaceAuthenticationRequest** | [**UpdateWorkspaceAuthenticationRequest**](UpdateWorkspaceAuthenticationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateWorkspaceAuthenticationResponse**](UpdateWorkspaceAuthenticationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateWorkspaceConfiguration

> Object updateWorkspaceConfiguration(workspaceId, updateWorkspaceConfigurationRequest, opts)



Updates the configuration string for the given workspace

### Example

```javascript
import AmazonManagedGrafana from 'amazon_managed_grafana';
let defaultClient = AmazonManagedGrafana.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonManagedGrafana.DefaultApi();
let workspaceId = "workspaceId_example"; // String | The ID of the workspace to update.
let updateWorkspaceConfigurationRequest = new AmazonManagedGrafana.UpdateWorkspaceConfigurationRequest(); // UpdateWorkspaceConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateWorkspaceConfiguration(workspaceId, updateWorkspaceConfigurationRequest, opts, (error, data, response) => {
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
 **workspaceId** | **String**| The ID of the workspace to update. | 
 **updateWorkspaceConfigurationRequest** | [**UpdateWorkspaceConfigurationRequest**](UpdateWorkspaceConfigurationRequest.md)|  | 
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

