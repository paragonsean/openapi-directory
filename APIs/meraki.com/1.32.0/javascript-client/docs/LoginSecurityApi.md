# MerakiDashboardApi.LoginSecurityApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOrganizationLoginSecurity_1**](LoginSecurityApi.md#getOrganizationLoginSecurity_1) | **GET** /organizations/{organizationId}/loginSecurity | Returns the login security settings for an organization.
[**updateOrganizationLoginSecurity_1**](LoginSecurityApi.md#updateOrganizationLoginSecurity_1) | **PUT** /organizations/{organizationId}/loginSecurity | Update the login security settings for an organization



## getOrganizationLoginSecurity_1

> GetOrganizationLoginSecurity200Response getOrganizationLoginSecurity_1(organizationId)

Returns the login security settings for an organization.

Returns the login security settings for an organization.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.LoginSecurityApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationLoginSecurity_1(organizationId, (error, data, response) => {
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

[**GetOrganizationLoginSecurity200Response**](GetOrganizationLoginSecurity200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateOrganizationLoginSecurity_1

> GetOrganizationLoginSecurity200Response updateOrganizationLoginSecurity_1(organizationId, opts)

Update the login security settings for an organization

Update the login security settings for an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.LoginSecurityApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'updateOrganizationLoginSecurityRequest': new MerakiDashboardApi.UpdateOrganizationLoginSecurityRequest() // UpdateOrganizationLoginSecurityRequest | 
};
apiInstance.updateOrganizationLoginSecurity_1(organizationId, opts, (error, data, response) => {
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
 **updateOrganizationLoginSecurityRequest** | [**UpdateOrganizationLoginSecurityRequest**](UpdateOrganizationLoginSecurityRequest.md)|  | [optional] 

### Return type

[**GetOrganizationLoginSecurity200Response**](GetOrganizationLoginSecurity200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

