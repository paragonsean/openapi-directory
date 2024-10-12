# MerakiDashboardApi.AclsApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createOrganizationAdaptivePolicyAcl_2**](AclsApi.md#createOrganizationAdaptivePolicyAcl_2) | **POST** /organizations/{organizationId}/adaptivePolicy/acls | Creates new adaptive policy ACL
[**deleteOrganizationAdaptivePolicyAcl_2**](AclsApi.md#deleteOrganizationAdaptivePolicyAcl_2) | **DELETE** /organizations/{organizationId}/adaptivePolicy/acls/{aclId} | Deletes the specified adaptive policy ACL
[**getOrganizationAdaptivePolicyAcl_2**](AclsApi.md#getOrganizationAdaptivePolicyAcl_2) | **GET** /organizations/{organizationId}/adaptivePolicy/acls/{aclId} | Returns the adaptive policy ACL information
[**getOrganizationAdaptivePolicyAcls_2**](AclsApi.md#getOrganizationAdaptivePolicyAcls_2) | **GET** /organizations/{organizationId}/adaptivePolicy/acls | List adaptive policy ACLs in a organization
[**updateOrganizationAdaptivePolicyAcl_2**](AclsApi.md#updateOrganizationAdaptivePolicyAcl_2) | **PUT** /organizations/{organizationId}/adaptivePolicy/acls/{aclId} | Updates an adaptive policy ACL



## createOrganizationAdaptivePolicyAcl_2

> Object createOrganizationAdaptivePolicyAcl_2(organizationId, createOrganizationAdaptivePolicyAclRequest)

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

let apiInstance = new MerakiDashboardApi.AclsApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationAdaptivePolicyAclRequest = new MerakiDashboardApi.CreateOrganizationAdaptivePolicyAclRequest(); // CreateOrganizationAdaptivePolicyAclRequest | 
apiInstance.createOrganizationAdaptivePolicyAcl_2(organizationId, createOrganizationAdaptivePolicyAclRequest, (error, data, response) => {
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


## deleteOrganizationAdaptivePolicyAcl_2

> deleteOrganizationAdaptivePolicyAcl_2(organizationId, aclId)

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

let apiInstance = new MerakiDashboardApi.AclsApi();
let organizationId = "organizationId_example"; // String | 
let aclId = "aclId_example"; // String | 
apiInstance.deleteOrganizationAdaptivePolicyAcl_2(organizationId, aclId, (error, data, response) => {
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


## getOrganizationAdaptivePolicyAcl_2

> Object getOrganizationAdaptivePolicyAcl_2(organizationId, aclId)

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

let apiInstance = new MerakiDashboardApi.AclsApi();
let organizationId = "organizationId_example"; // String | 
let aclId = "aclId_example"; // String | 
apiInstance.getOrganizationAdaptivePolicyAcl_2(organizationId, aclId, (error, data, response) => {
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


## getOrganizationAdaptivePolicyAcls_2

> [Object] getOrganizationAdaptivePolicyAcls_2(organizationId)

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

let apiInstance = new MerakiDashboardApi.AclsApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationAdaptivePolicyAcls_2(organizationId, (error, data, response) => {
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


## updateOrganizationAdaptivePolicyAcl_2

> Object updateOrganizationAdaptivePolicyAcl_2(organizationId, aclId, opts)

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

let apiInstance = new MerakiDashboardApi.AclsApi();
let organizationId = "organizationId_example"; // String | 
let aclId = "aclId_example"; // String | 
let opts = {
  'updateOrganizationAdaptivePolicyAclRequest': new MerakiDashboardApi.UpdateOrganizationAdaptivePolicyAclRequest() // UpdateOrganizationAdaptivePolicyAclRequest | 
};
apiInstance.updateOrganizationAdaptivePolicyAcl_2(organizationId, aclId, opts, (error, data, response) => {
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

