# MerakiDashboardApi.AdaptivePolicyApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createOrganizationAdaptivePolicyAcl_1**](AdaptivePolicyApi.md#createOrganizationAdaptivePolicyAcl_1) | **POST** /organizations/{organizationId}/adaptivePolicy/acls | Creates new adaptive policy ACL
[**createOrganizationAdaptivePolicyGroup_1**](AdaptivePolicyApi.md#createOrganizationAdaptivePolicyGroup_1) | **POST** /organizations/{organizationId}/adaptivePolicy/groups | Creates a new adaptive policy group
[**createOrganizationAdaptivePolicyPolicy_1**](AdaptivePolicyApi.md#createOrganizationAdaptivePolicyPolicy_1) | **POST** /organizations/{organizationId}/adaptivePolicy/policies | Add an Adaptive Policy
[**deleteOrganizationAdaptivePolicyAcl_1**](AdaptivePolicyApi.md#deleteOrganizationAdaptivePolicyAcl_1) | **DELETE** /organizations/{organizationId}/adaptivePolicy/acls/{aclId} | Deletes the specified adaptive policy ACL
[**deleteOrganizationAdaptivePolicyGroup_1**](AdaptivePolicyApi.md#deleteOrganizationAdaptivePolicyGroup_1) | **DELETE** /organizations/{organizationId}/adaptivePolicy/groups/{id} | Deletes the specified adaptive policy group and any associated policies and references
[**deleteOrganizationAdaptivePolicyPolicy_1**](AdaptivePolicyApi.md#deleteOrganizationAdaptivePolicyPolicy_1) | **DELETE** /organizations/{organizationId}/adaptivePolicy/policies/{id} | Delete an Adaptive Policy
[**getOrganizationAdaptivePolicyAcl_1**](AdaptivePolicyApi.md#getOrganizationAdaptivePolicyAcl_1) | **GET** /organizations/{organizationId}/adaptivePolicy/acls/{aclId} | Returns the adaptive policy ACL information
[**getOrganizationAdaptivePolicyAcls_1**](AdaptivePolicyApi.md#getOrganizationAdaptivePolicyAcls_1) | **GET** /organizations/{organizationId}/adaptivePolicy/acls | List adaptive policy ACLs in a organization
[**getOrganizationAdaptivePolicyGroup_1**](AdaptivePolicyApi.md#getOrganizationAdaptivePolicyGroup_1) | **GET** /organizations/{organizationId}/adaptivePolicy/groups/{id} | Returns an adaptive policy group
[**getOrganizationAdaptivePolicyGroups_1**](AdaptivePolicyApi.md#getOrganizationAdaptivePolicyGroups_1) | **GET** /organizations/{organizationId}/adaptivePolicy/groups | List adaptive policy groups in a organization
[**getOrganizationAdaptivePolicyOverview_1**](AdaptivePolicyApi.md#getOrganizationAdaptivePolicyOverview_1) | **GET** /organizations/{organizationId}/adaptivePolicy/overview | Returns adaptive policy aggregate statistics for an organization
[**getOrganizationAdaptivePolicyPolicies_1**](AdaptivePolicyApi.md#getOrganizationAdaptivePolicyPolicies_1) | **GET** /organizations/{organizationId}/adaptivePolicy/policies | List adaptive policies in an organization
[**getOrganizationAdaptivePolicyPolicy_1**](AdaptivePolicyApi.md#getOrganizationAdaptivePolicyPolicy_1) | **GET** /organizations/{organizationId}/adaptivePolicy/policies/{id} | Return an adaptive policy
[**getOrganizationAdaptivePolicySettings_1**](AdaptivePolicyApi.md#getOrganizationAdaptivePolicySettings_1) | **GET** /organizations/{organizationId}/adaptivePolicy/settings | Returns global adaptive policy settings in an organization
[**updateOrganizationAdaptivePolicyAcl_1**](AdaptivePolicyApi.md#updateOrganizationAdaptivePolicyAcl_1) | **PUT** /organizations/{organizationId}/adaptivePolicy/acls/{aclId} | Updates an adaptive policy ACL
[**updateOrganizationAdaptivePolicyGroup_1**](AdaptivePolicyApi.md#updateOrganizationAdaptivePolicyGroup_1) | **PUT** /organizations/{organizationId}/adaptivePolicy/groups/{id} | Updates an adaptive policy group
[**updateOrganizationAdaptivePolicyPolicy_1**](AdaptivePolicyApi.md#updateOrganizationAdaptivePolicyPolicy_1) | **PUT** /organizations/{organizationId}/adaptivePolicy/policies/{id} | Update an Adaptive Policy
[**updateOrganizationAdaptivePolicySettings_1**](AdaptivePolicyApi.md#updateOrganizationAdaptivePolicySettings_1) | **PUT** /organizations/{organizationId}/adaptivePolicy/settings | Update global adaptive policy settings



## createOrganizationAdaptivePolicyAcl_1

> Object createOrganizationAdaptivePolicyAcl_1(organizationId, createOrganizationAdaptivePolicyAclRequest)

Creates new adaptive policy ACL

Creates new adaptive policy ACL

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AdaptivePolicyApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationAdaptivePolicyAclRequest = new MerakiDashboardApi.CreateOrganizationAdaptivePolicyAclRequest(); // CreateOrganizationAdaptivePolicyAclRequest | 
apiInstance.createOrganizationAdaptivePolicyAcl_1(organizationId, createOrganizationAdaptivePolicyAclRequest, (error, data, response) => {
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
 **organizationId** | **String**|  | 
 **createOrganizationAdaptivePolicyAclRequest** | [**CreateOrganizationAdaptivePolicyAclRequest**](CreateOrganizationAdaptivePolicyAclRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOrganizationAdaptivePolicyGroup_1

> Object createOrganizationAdaptivePolicyGroup_1(organizationId, createOrganizationAdaptivePolicyGroupRequest)

Creates a new adaptive policy group

Creates a new adaptive policy group

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AdaptivePolicyApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationAdaptivePolicyGroupRequest = new MerakiDashboardApi.CreateOrganizationAdaptivePolicyGroupRequest(); // CreateOrganizationAdaptivePolicyGroupRequest | 
apiInstance.createOrganizationAdaptivePolicyGroup_1(organizationId, createOrganizationAdaptivePolicyGroupRequest, (error, data, response) => {
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
 **organizationId** | **String**|  | 
 **createOrganizationAdaptivePolicyGroupRequest** | [**CreateOrganizationAdaptivePolicyGroupRequest**](CreateOrganizationAdaptivePolicyGroupRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOrganizationAdaptivePolicyPolicy_1

> Object createOrganizationAdaptivePolicyPolicy_1(organizationId, createOrganizationAdaptivePolicyPolicyRequest)

Add an Adaptive Policy

Add an Adaptive Policy

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AdaptivePolicyApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationAdaptivePolicyPolicyRequest = new MerakiDashboardApi.CreateOrganizationAdaptivePolicyPolicyRequest(); // CreateOrganizationAdaptivePolicyPolicyRequest | 
apiInstance.createOrganizationAdaptivePolicyPolicy_1(organizationId, createOrganizationAdaptivePolicyPolicyRequest, (error, data, response) => {
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
 **organizationId** | **String**|  | 
 **createOrganizationAdaptivePolicyPolicyRequest** | [**CreateOrganizationAdaptivePolicyPolicyRequest**](CreateOrganizationAdaptivePolicyPolicyRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteOrganizationAdaptivePolicyAcl_1

> deleteOrganizationAdaptivePolicyAcl_1(organizationId, aclId)

Deletes the specified adaptive policy ACL

Deletes the specified adaptive policy ACL. Note this adaptive policy ACL will also be removed from policies using it.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AdaptivePolicyApi();
let organizationId = "organizationId_example"; // String | 
let aclId = "aclId_example"; // String | 
apiInstance.deleteOrganizationAdaptivePolicyAcl_1(organizationId, aclId, (error, data, response) => {
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
 **organizationId** | **String**|  | 
 **aclId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganizationAdaptivePolicyGroup_1

> deleteOrganizationAdaptivePolicyGroup_1(organizationId, id)

Deletes the specified adaptive policy group and any associated policies and references

Deletes the specified adaptive policy group and any associated policies and references

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AdaptivePolicyApi();
let organizationId = "organizationId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.deleteOrganizationAdaptivePolicyGroup_1(organizationId, id, (error, data, response) => {
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
 **organizationId** | **String**|  | 
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganizationAdaptivePolicyPolicy_1

> deleteOrganizationAdaptivePolicyPolicy_1(organizationId, id)

Delete an Adaptive Policy

Delete an Adaptive Policy

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AdaptivePolicyApi();
let organizationId = "organizationId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.deleteOrganizationAdaptivePolicyPolicy_1(organizationId, id, (error, data, response) => {
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
 **organizationId** | **String**|  | 
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganizationAdaptivePolicyAcl_1

> Object getOrganizationAdaptivePolicyAcl_1(organizationId, aclId)

Returns the adaptive policy ACL information

Returns the adaptive policy ACL information

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AdaptivePolicyApi();
let organizationId = "organizationId_example"; // String | 
let aclId = "aclId_example"; // String | 
apiInstance.getOrganizationAdaptivePolicyAcl_1(organizationId, aclId, (error, data, response) => {
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
 **organizationId** | **String**|  | 
 **aclId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationAdaptivePolicyAcls_1

> [Object] getOrganizationAdaptivePolicyAcls_1(organizationId)

List adaptive policy ACLs in a organization

List adaptive policy ACLs in a organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AdaptivePolicyApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationAdaptivePolicyAcls_1(organizationId, (error, data, response) => {
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
 **organizationId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationAdaptivePolicyGroup_1

> Object getOrganizationAdaptivePolicyGroup_1(organizationId, id)

Returns an adaptive policy group

Returns an adaptive policy group

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AdaptivePolicyApi();
let organizationId = "organizationId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.getOrganizationAdaptivePolicyGroup_1(organizationId, id, (error, data, response) => {
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
 **organizationId** | **String**|  | 
 **id** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationAdaptivePolicyGroups_1

> [Object] getOrganizationAdaptivePolicyGroups_1(organizationId)

List adaptive policy groups in a organization

List adaptive policy groups in a organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AdaptivePolicyApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationAdaptivePolicyGroups_1(organizationId, (error, data, response) => {
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
 **organizationId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationAdaptivePolicyOverview_1

> GetOrganizationAdaptivePolicyOverview200Response getOrganizationAdaptivePolicyOverview_1(organizationId)

Returns adaptive policy aggregate statistics for an organization

Returns adaptive policy aggregate statistics for an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AdaptivePolicyApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationAdaptivePolicyOverview_1(organizationId, (error, data, response) => {
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
 **organizationId** | **String**|  | 

### Return type

[**GetOrganizationAdaptivePolicyOverview200Response**](GetOrganizationAdaptivePolicyOverview200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationAdaptivePolicyPolicies_1

> [Object] getOrganizationAdaptivePolicyPolicies_1(organizationId)

List adaptive policies in an organization

List adaptive policies in an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AdaptivePolicyApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationAdaptivePolicyPolicies_1(organizationId, (error, data, response) => {
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
 **organizationId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationAdaptivePolicyPolicy_1

> Object getOrganizationAdaptivePolicyPolicy_1(organizationId, id)

Return an adaptive policy

Return an adaptive policy

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AdaptivePolicyApi();
let organizationId = "organizationId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.getOrganizationAdaptivePolicyPolicy_1(organizationId, id, (error, data, response) => {
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
 **organizationId** | **String**|  | 
 **id** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationAdaptivePolicySettings_1

> Object getOrganizationAdaptivePolicySettings_1(organizationId)

Returns global adaptive policy settings in an organization

Returns global adaptive policy settings in an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AdaptivePolicyApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationAdaptivePolicySettings_1(organizationId, (error, data, response) => {
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
 **organizationId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateOrganizationAdaptivePolicyAcl_1

> Object updateOrganizationAdaptivePolicyAcl_1(organizationId, aclId, opts)

Updates an adaptive policy ACL

Updates an adaptive policy ACL

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AdaptivePolicyApi();
let organizationId = "organizationId_example"; // String | 
let aclId = "aclId_example"; // String | 
let opts = {
  'updateOrganizationAdaptivePolicyAclRequest': new MerakiDashboardApi.UpdateOrganizationAdaptivePolicyAclRequest() // UpdateOrganizationAdaptivePolicyAclRequest | 
};
apiInstance.updateOrganizationAdaptivePolicyAcl_1(organizationId, aclId, opts, (error, data, response) => {
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
 **organizationId** | **String**|  | 
 **aclId** | **String**|  | 
 **updateOrganizationAdaptivePolicyAclRequest** | [**UpdateOrganizationAdaptivePolicyAclRequest**](UpdateOrganizationAdaptivePolicyAclRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationAdaptivePolicyGroup_1

> Object updateOrganizationAdaptivePolicyGroup_1(organizationId, id, opts)

Updates an adaptive policy group

Updates an adaptive policy group. If updating \&quot;Infrastructure\&quot;, only the SGT is allowed. Cannot update \&quot;Unknown\&quot;.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AdaptivePolicyApi();
let organizationId = "organizationId_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'updateOrganizationAdaptivePolicyGroupRequest': new MerakiDashboardApi.UpdateOrganizationAdaptivePolicyGroupRequest() // UpdateOrganizationAdaptivePolicyGroupRequest | 
};
apiInstance.updateOrganizationAdaptivePolicyGroup_1(organizationId, id, opts, (error, data, response) => {
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
 **organizationId** | **String**|  | 
 **id** | **String**|  | 
 **updateOrganizationAdaptivePolicyGroupRequest** | [**UpdateOrganizationAdaptivePolicyGroupRequest**](UpdateOrganizationAdaptivePolicyGroupRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationAdaptivePolicyPolicy_1

> Object updateOrganizationAdaptivePolicyPolicy_1(organizationId, id, opts)

Update an Adaptive Policy

Update an Adaptive Policy

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AdaptivePolicyApi();
let organizationId = "organizationId_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'updateOrganizationAdaptivePolicyPolicyRequest': new MerakiDashboardApi.UpdateOrganizationAdaptivePolicyPolicyRequest() // UpdateOrganizationAdaptivePolicyPolicyRequest | 
};
apiInstance.updateOrganizationAdaptivePolicyPolicy_1(organizationId, id, opts, (error, data, response) => {
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
 **organizationId** | **String**|  | 
 **id** | **String**|  | 
 **updateOrganizationAdaptivePolicyPolicyRequest** | [**UpdateOrganizationAdaptivePolicyPolicyRequest**](UpdateOrganizationAdaptivePolicyPolicyRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationAdaptivePolicySettings_1

> Object updateOrganizationAdaptivePolicySettings_1(organizationId, opts)

Update global adaptive policy settings

Update global adaptive policy settings

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AdaptivePolicyApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'updateOrganizationAdaptivePolicySettingsRequest': new MerakiDashboardApi.UpdateOrganizationAdaptivePolicySettingsRequest() // UpdateOrganizationAdaptivePolicySettingsRequest | 
};
apiInstance.updateOrganizationAdaptivePolicySettings_1(organizationId, opts, (error, data, response) => {
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
 **organizationId** | **String**|  | 
 **updateOrganizationAdaptivePolicySettingsRequest** | [**UpdateOrganizationAdaptivePolicySettingsRequest**](UpdateOrganizationAdaptivePolicySettingsRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

