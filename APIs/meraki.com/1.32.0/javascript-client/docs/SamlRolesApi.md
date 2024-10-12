# MerakiDashboardApi.SamlRolesApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createOrganizationSamlRole_1**](SamlRolesApi.md#createOrganizationSamlRole_1) | **POST** /organizations/{organizationId}/samlRoles | Create a SAML role
[**deleteOrganizationSamlRole_1**](SamlRolesApi.md#deleteOrganizationSamlRole_1) | **DELETE** /organizations/{organizationId}/samlRoles/{samlRoleId} | Remove a SAML role
[**getOrganizationSamlRole_1**](SamlRolesApi.md#getOrganizationSamlRole_1) | **GET** /organizations/{organizationId}/samlRoles/{samlRoleId} | Return a SAML role
[**getOrganizationSamlRoles_1**](SamlRolesApi.md#getOrganizationSamlRoles_1) | **GET** /organizations/{organizationId}/samlRoles | List the SAML roles for this organization
[**updateOrganizationSamlRole_1**](SamlRolesApi.md#updateOrganizationSamlRole_1) | **PUT** /organizations/{organizationId}/samlRoles/{samlRoleId} | Update a SAML role



## createOrganizationSamlRole_1

> Object createOrganizationSamlRole_1(organizationId, createOrganizationSamlRoleRequest)

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

let apiInstance = new MerakiDashboardApi.SamlRolesApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationSamlRoleRequest = new MerakiDashboardApi.CreateOrganizationSamlRoleRequest(); // CreateOrganizationSamlRoleRequest | 
apiInstance.createOrganizationSamlRole_1(organizationId, createOrganizationSamlRoleRequest, (error, data, response) => {
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


## deleteOrganizationSamlRole_1

> deleteOrganizationSamlRole_1(organizationId, samlRoleId)

Remove a SAML role

Remove a SAML role

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SamlRolesApi();
let organizationId = "organizationId_example"; // String | 
let samlRoleId = "samlRoleId_example"; // String | 
apiInstance.deleteOrganizationSamlRole_1(organizationId, samlRoleId, (error, data, response) => {
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
 **samlRoleId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganizationSamlRole_1

> Object getOrganizationSamlRole_1(organizationId, samlRoleId)

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

let apiInstance = new MerakiDashboardApi.SamlRolesApi();
let organizationId = "organizationId_example"; // String | 
let samlRoleId = "samlRoleId_example"; // String | 
apiInstance.getOrganizationSamlRole_1(organizationId, samlRoleId, (error, data, response) => {
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


## getOrganizationSamlRoles_1

> [Object] getOrganizationSamlRoles_1(organizationId)

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

let apiInstance = new MerakiDashboardApi.SamlRolesApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationSamlRoles_1(organizationId, (error, data, response) => {
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


## updateOrganizationSamlRole_1

> UpdateOrganizationSamlRole200Response updateOrganizationSamlRole_1(organizationId, samlRoleId, opts)

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

let apiInstance = new MerakiDashboardApi.SamlRolesApi();
let organizationId = "organizationId_example"; // String | 
let samlRoleId = "samlRoleId_example"; // String | 
let opts = {
  'updateOrganizationSamlRoleRequest': new MerakiDashboardApi.UpdateOrganizationSamlRoleRequest() // UpdateOrganizationSamlRoleRequest | 
};
apiInstance.updateOrganizationSamlRole_1(organizationId, samlRoleId, opts, (error, data, response) => {
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

[**UpdateOrganizationSamlRole200Response**](UpdateOrganizationSamlRole200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

