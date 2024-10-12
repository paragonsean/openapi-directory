# MerakiDashboardApi.ConfigTemplatesApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createOrganizationConfigTemplate_1**](ConfigTemplatesApi.md#createOrganizationConfigTemplate_1) | **POST** /organizations/{organizationId}/configTemplates | Create a new configuration template
[**deleteOrganizationConfigTemplate_1**](ConfigTemplatesApi.md#deleteOrganizationConfigTemplate_1) | **DELETE** /organizations/{organizationId}/configTemplates/{configTemplateId} | Remove a configuration template
[**getOrganizationConfigTemplateSwitchProfilePort_1**](ConfigTemplatesApi.md#getOrganizationConfigTemplateSwitchProfilePort_1) | **GET** /organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports/{portId} | Return a switch profile port
[**getOrganizationConfigTemplateSwitchProfilePorts_1**](ConfigTemplatesApi.md#getOrganizationConfigTemplateSwitchProfilePorts_1) | **GET** /organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports | Return all the ports of a switch profile
[**getOrganizationConfigTemplateSwitchProfiles_1**](ConfigTemplatesApi.md#getOrganizationConfigTemplateSwitchProfiles_1) | **GET** /organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles | List the switch profiles for your switch template configuration
[**getOrganizationConfigTemplate_1**](ConfigTemplatesApi.md#getOrganizationConfigTemplate_1) | **GET** /organizations/{organizationId}/configTemplates/{configTemplateId} | Return a single configuration template
[**getOrganizationConfigTemplates_1**](ConfigTemplatesApi.md#getOrganizationConfigTemplates_1) | **GET** /organizations/{organizationId}/configTemplates | List the configuration templates for this organization
[**updateOrganizationConfigTemplateSwitchProfilePort_1**](ConfigTemplatesApi.md#updateOrganizationConfigTemplateSwitchProfilePort_1) | **PUT** /organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports/{portId} | Update a switch profile port
[**updateOrganizationConfigTemplate_1**](ConfigTemplatesApi.md#updateOrganizationConfigTemplate_1) | **PUT** /organizations/{organizationId}/configTemplates/{configTemplateId} | Update a configuration template



## createOrganizationConfigTemplate_1

> Object createOrganizationConfigTemplate_1(organizationId, createOrganizationConfigTemplateRequest)

Create a new configuration template

Create a new configuration template

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigTemplatesApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationConfigTemplateRequest = new MerakiDashboardApi.CreateOrganizationConfigTemplateRequest(); // CreateOrganizationConfigTemplateRequest | 
apiInstance.createOrganizationConfigTemplate_1(organizationId, createOrganizationConfigTemplateRequest, (error, data, response) => {
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
 **createOrganizationConfigTemplateRequest** | [**CreateOrganizationConfigTemplateRequest**](CreateOrganizationConfigTemplateRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteOrganizationConfigTemplate_1

> deleteOrganizationConfigTemplate_1(organizationId, configTemplateId)

Remove a configuration template

Remove a configuration template

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigTemplatesApi();
let organizationId = "organizationId_example"; // String | 
let configTemplateId = "configTemplateId_example"; // String | 
apiInstance.deleteOrganizationConfigTemplate_1(organizationId, configTemplateId, (error, data, response) => {
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
 **configTemplateId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganizationConfigTemplateSwitchProfilePort_1

> GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner getOrganizationConfigTemplateSwitchProfilePort_1(organizationId, configTemplateId, profileId, portId)

Return a switch profile port

Return a switch profile port

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigTemplatesApi();
let organizationId = "organizationId_example"; // String | 
let configTemplateId = "configTemplateId_example"; // String | 
let profileId = "profileId_example"; // String | 
let portId = "portId_example"; // String | 
apiInstance.getOrganizationConfigTemplateSwitchProfilePort_1(organizationId, configTemplateId, profileId, portId, (error, data, response) => {
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
 **configTemplateId** | **String**|  | 
 **profileId** | **String**|  | 
 **portId** | **String**|  | 

### Return type

[**GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner**](GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationConfigTemplateSwitchProfilePorts_1

> [GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner] getOrganizationConfigTemplateSwitchProfilePorts_1(organizationId, configTemplateId, profileId)

Return all the ports of a switch profile

Return all the ports of a switch profile

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigTemplatesApi();
let organizationId = "organizationId_example"; // String | 
let configTemplateId = "configTemplateId_example"; // String | 
let profileId = "profileId_example"; // String | 
apiInstance.getOrganizationConfigTemplateSwitchProfilePorts_1(organizationId, configTemplateId, profileId, (error, data, response) => {
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
 **configTemplateId** | **String**|  | 
 **profileId** | **String**|  | 

### Return type

[**[GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner]**](GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationConfigTemplateSwitchProfiles_1

> GetOrganizationConfigTemplateSwitchProfiles200Response getOrganizationConfigTemplateSwitchProfiles_1(organizationId, configTemplateId)

List the switch profiles for your switch template configuration

List the switch profiles for your switch template configuration

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigTemplatesApi();
let organizationId = "organizationId_example"; // String | 
let configTemplateId = "configTemplateId_example"; // String | 
apiInstance.getOrganizationConfigTemplateSwitchProfiles_1(organizationId, configTemplateId, (error, data, response) => {
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
 **configTemplateId** | **String**|  | 

### Return type

[**GetOrganizationConfigTemplateSwitchProfiles200Response**](GetOrganizationConfigTemplateSwitchProfiles200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationConfigTemplate_1

> Object getOrganizationConfigTemplate_1(organizationId, configTemplateId)

Return a single configuration template

Return a single configuration template

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigTemplatesApi();
let organizationId = "organizationId_example"; // String | 
let configTemplateId = "configTemplateId_example"; // String | 
apiInstance.getOrganizationConfigTemplate_1(organizationId, configTemplateId, (error, data, response) => {
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
 **configTemplateId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationConfigTemplates_1

> [Object] getOrganizationConfigTemplates_1(organizationId)

List the configuration templates for this organization

List the configuration templates for this organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigTemplatesApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationConfigTemplates_1(organizationId, (error, data, response) => {
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


## updateOrganizationConfigTemplateSwitchProfilePort_1

> GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner updateOrganizationConfigTemplateSwitchProfilePort_1(organizationId, configTemplateId, profileId, portId, opts)

Update a switch profile port

Update a switch profile port

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigTemplatesApi();
let organizationId = "organizationId_example"; // String | 
let configTemplateId = "configTemplateId_example"; // String | 
let profileId = "profileId_example"; // String | 
let portId = "portId_example"; // String | 
let opts = {
  'updateOrganizationConfigTemplateSwitchProfilePortRequest': new MerakiDashboardApi.UpdateOrganizationConfigTemplateSwitchProfilePortRequest() // UpdateOrganizationConfigTemplateSwitchProfilePortRequest | 
};
apiInstance.updateOrganizationConfigTemplateSwitchProfilePort_1(organizationId, configTemplateId, profileId, portId, opts, (error, data, response) => {
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
 **configTemplateId** | **String**|  | 
 **profileId** | **String**|  | 
 **portId** | **String**|  | 
 **updateOrganizationConfigTemplateSwitchProfilePortRequest** | [**UpdateOrganizationConfigTemplateSwitchProfilePortRequest**](UpdateOrganizationConfigTemplateSwitchProfilePortRequest.md)|  | [optional] 

### Return type

[**GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner**](GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationConfigTemplate_1

> Object updateOrganizationConfigTemplate_1(organizationId, configTemplateId, opts)

Update a configuration template

Update a configuration template

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ConfigTemplatesApi();
let organizationId = "organizationId_example"; // String | 
let configTemplateId = "configTemplateId_example"; // String | 
let opts = {
  'updateOrganizationConfigTemplateRequest': new MerakiDashboardApi.UpdateOrganizationConfigTemplateRequest() // UpdateOrganizationConfigTemplateRequest | 
};
apiInstance.updateOrganizationConfigTemplate_1(organizationId, configTemplateId, opts, (error, data, response) => {
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
 **configTemplateId** | **String**|  | 
 **updateOrganizationConfigTemplateRequest** | [**UpdateOrganizationConfigTemplateRequest**](UpdateOrganizationConfigTemplateRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

