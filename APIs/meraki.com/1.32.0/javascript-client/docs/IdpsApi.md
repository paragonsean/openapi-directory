# MerakiDashboardApi.IdpsApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createOrganizationSamlIdp_2**](IdpsApi.md#createOrganizationSamlIdp_2) | **POST** /organizations/{organizationId}/saml/idps | Create a SAML IdP for your organization.
[**deleteOrganizationSamlIdp_2**](IdpsApi.md#deleteOrganizationSamlIdp_2) | **DELETE** /organizations/{organizationId}/saml/idps/{idpId} | Remove a SAML IdP in your organization.
[**getOrganizationSamlIdp_2**](IdpsApi.md#getOrganizationSamlIdp_2) | **GET** /organizations/{organizationId}/saml/idps/{idpId} | Get a SAML IdP from your organization.
[**getOrganizationSamlIdps_2**](IdpsApi.md#getOrganizationSamlIdps_2) | **GET** /organizations/{organizationId}/saml/idps | List the SAML IdPs in your organization.
[**updateOrganizationSamlIdp_2**](IdpsApi.md#updateOrganizationSamlIdp_2) | **PUT** /organizations/{organizationId}/saml/idps/{idpId} | Update a SAML IdP in your organization



## createOrganizationSamlIdp_2

> [GetOrganizationSamlIdps200ResponseInner] createOrganizationSamlIdp_2(organizationId, createOrganizationSamlIdpRequest)

Create a SAML IdP for your organization.

Create a SAML IdP for your organization.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.IdpsApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationSamlIdpRequest = new MerakiDashboardApi.CreateOrganizationSamlIdpRequest(); // CreateOrganizationSamlIdpRequest | 
apiInstance.createOrganizationSamlIdp_2(organizationId, createOrganizationSamlIdpRequest, (error, data, response) => {
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
 **createOrganizationSamlIdpRequest** | [**CreateOrganizationSamlIdpRequest**](CreateOrganizationSamlIdpRequest.md)|  | 

### Return type

[**[GetOrganizationSamlIdps200ResponseInner]**](GetOrganizationSamlIdps200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteOrganizationSamlIdp_2

> deleteOrganizationSamlIdp_2(organizationId, idpId)

Remove a SAML IdP in your organization.

Remove a SAML IdP in your organization.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.IdpsApi();
let organizationId = "organizationId_example"; // String | 
let idpId = "idpId_example"; // String | 
apiInstance.deleteOrganizationSamlIdp_2(organizationId, idpId, (error, data, response) => {
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
 **idpId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganizationSamlIdp_2

> GetOrganizationSamlIdps200ResponseInner getOrganizationSamlIdp_2(organizationId, idpId)

Get a SAML IdP from your organization.

Get a SAML IdP from your organization.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.IdpsApi();
let organizationId = "organizationId_example"; // String | 
let idpId = "idpId_example"; // String | 
apiInstance.getOrganizationSamlIdp_2(organizationId, idpId, (error, data, response) => {
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
 **idpId** | **String**|  | 

### Return type

[**GetOrganizationSamlIdps200ResponseInner**](GetOrganizationSamlIdps200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationSamlIdps_2

> [GetOrganizationSamlIdps200ResponseInner] getOrganizationSamlIdps_2(organizationId)

List the SAML IdPs in your organization.

List the SAML IdPs in your organization.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.IdpsApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationSamlIdps_2(organizationId, (error, data, response) => {
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

[**[GetOrganizationSamlIdps200ResponseInner]**](GetOrganizationSamlIdps200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateOrganizationSamlIdp_2

> [GetOrganizationSamlIdps200ResponseInner] updateOrganizationSamlIdp_2(organizationId, idpId, opts)

Update a SAML IdP in your organization

Update a SAML IdP in your organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.IdpsApi();
let organizationId = "organizationId_example"; // String | 
let idpId = "idpId_example"; // String | 
let opts = {
  'updateOrganizationSamlIdpRequest': new MerakiDashboardApi.UpdateOrganizationSamlIdpRequest() // UpdateOrganizationSamlIdpRequest | 
};
apiInstance.updateOrganizationSamlIdp_2(organizationId, idpId, opts, (error, data, response) => {
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
 **idpId** | **String**|  | 
 **updateOrganizationSamlIdpRequest** | [**UpdateOrganizationSamlIdpRequest**](UpdateOrganizationSamlIdpRequest.md)|  | [optional] 

### Return type

[**[GetOrganizationSamlIdps200ResponseInner]**](GetOrganizationSamlIdps200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

