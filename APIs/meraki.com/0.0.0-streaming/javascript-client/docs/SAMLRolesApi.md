# MerakiDashboardApi.SAMLRolesApi

All URIs are relative to *https://api.meraki.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createOrganizationSamlRole**](SAMLRolesApi.md#createOrganizationSamlRole) | **POST** /organizations/{organizationId}/samlRoles | Create a SAML role
[**getOrganizationSamlRole**](SAMLRolesApi.md#getOrganizationSamlRole) | **GET** /organizations/{organizationId}/samlRoles/{samlRoleId} | Return a SAML role
[**getOrganizationSamlRoles**](SAMLRolesApi.md#getOrganizationSamlRoles) | **GET** /organizations/{organizationId}/samlRoles | List the SAML roles for this organization
[**updateOrganizationSamlRole**](SAMLRolesApi.md#updateOrganizationSamlRole) | **PUT** /organizations/{organizationId}/samlRoles/{samlRoleId} | Update a SAML role



## createOrganizationSamlRole

> Object createOrganizationSamlRole(organizationId, createOrganizationSamlRoleRequest)

Create a SAML role

Create a SAML role

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SAMLRolesApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationSamlRoleRequest = new MerakiDashboardApi.CreateOrganizationSamlRoleRequest(); // CreateOrganizationSamlRoleRequest | 
apiInstance.createOrganizationSamlRole(organizationId, createOrganizationSamlRoleRequest, (error, data, response) => {
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
 **createOrganizationSamlRoleRequest** | [**CreateOrganizationSamlRoleRequest**](CreateOrganizationSamlRoleRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getOrganizationSamlRole

> Object getOrganizationSamlRole(organizationId, samlRoleId)

Return a SAML role

Return a SAML role

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SAMLRolesApi();
let organizationId = "organizationId_example"; // String | 
let samlRoleId = "samlRoleId_example"; // String | 
apiInstance.getOrganizationSamlRole(organizationId, samlRoleId, (error, data, response) => {
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
 **samlRoleId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationSamlRoles

> [Object] getOrganizationSamlRoles(organizationId)

List the SAML roles for this organization

List the SAML roles for this organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SAMLRolesApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationSamlRoles(organizationId, (error, data, response) => {
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


## updateOrganizationSamlRole

> Object updateOrganizationSamlRole(organizationId, samlRoleId, opts)

Update a SAML role

Update a SAML role

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SAMLRolesApi();
let organizationId = "organizationId_example"; // String | 
let samlRoleId = "samlRoleId_example"; // String | 
let opts = {
  'updateOrganizationSamlRoleRequest': new MerakiDashboardApi.UpdateOrganizationSamlRoleRequest() // UpdateOrganizationSamlRoleRequest | 
};
apiInstance.updateOrganizationSamlRole(organizationId, samlRoleId, opts, (error, data, response) => {
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
 **samlRoleId** | **String**|  | 
 **updateOrganizationSamlRoleRequest** | [**UpdateOrganizationSamlRoleRequest**](UpdateOrganizationSamlRoleRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

