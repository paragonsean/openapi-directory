# MerakiDashboardApi.AdminsApi

All URIs are relative to *https://api.meraki.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createOrganizationAdmin**](AdminsApi.md#createOrganizationAdmin) | **POST** /organizations/{organizationId}/admins | Create a new dashboard administrator
[**deleteOrganizationAdmin**](AdminsApi.md#deleteOrganizationAdmin) | **DELETE** /organizations/{organizationId}/admins/{adminId} | Revoke all access for a dashboard administrator within this organization
[**getOrganizationAdmins**](AdminsApi.md#getOrganizationAdmins) | **GET** /organizations/{organizationId}/admins | List the dashboard administrators in this organization
[**updateOrganizationAdmin**](AdminsApi.md#updateOrganizationAdmin) | **PUT** /organizations/{organizationId}/admins/{adminId} | Update an administrator



## createOrganizationAdmin

> Object createOrganizationAdmin(organizationId, createOrganizationAdminRequest)

Create a new dashboard administrator

Create a new dashboard administrator

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AdminsApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationAdminRequest = new MerakiDashboardApi.CreateOrganizationAdminRequest(); // CreateOrganizationAdminRequest | 
apiInstance.createOrganizationAdmin(organizationId, createOrganizationAdminRequest, (error, data, response) => {
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
 **createOrganizationAdminRequest** | [**CreateOrganizationAdminRequest**](CreateOrganizationAdminRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteOrganizationAdmin

> deleteOrganizationAdmin(organizationId, adminId)

Revoke all access for a dashboard administrator within this organization

Revoke all access for a dashboard administrator within this organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AdminsApi();
let organizationId = "organizationId_example"; // String | 
let adminId = "adminId_example"; // String | 
apiInstance.deleteOrganizationAdmin(organizationId, adminId, (error, data, response) => {
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
 **adminId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganizationAdmins

> [Object] getOrganizationAdmins(organizationId)

List the dashboard administrators in this organization

List the dashboard administrators in this organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AdminsApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationAdmins(organizationId, (error, data, response) => {
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


## updateOrganizationAdmin

> Object updateOrganizationAdmin(organizationId, adminId, opts)

Update an administrator

Update an administrator

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AdminsApi();
let organizationId = "organizationId_example"; // String | 
let adminId = "adminId_example"; // String | 
let opts = {
  'updateOrganizationAdminRequest': new MerakiDashboardApi.UpdateOrganizationAdminRequest() // UpdateOrganizationAdminRequest | 
};
apiInstance.updateOrganizationAdmin(organizationId, adminId, opts, (error, data, response) => {
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
 **adminId** | **String**|  | 
 **updateOrganizationAdminRequest** | [**UpdateOrganizationAdminRequest**](UpdateOrganizationAdminRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

