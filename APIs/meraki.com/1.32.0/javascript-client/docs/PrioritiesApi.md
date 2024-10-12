# MerakiDashboardApi.PrioritiesApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOrganizationBrandingPoliciesPriorities_2**](PrioritiesApi.md#getOrganizationBrandingPoliciesPriorities_2) | **GET** /organizations/{organizationId}/brandingPolicies/priorities | Return the branding policy IDs of an organization in priority order
[**updateOrganizationBrandingPoliciesPriorities_2**](PrioritiesApi.md#updateOrganizationBrandingPoliciesPriorities_2) | **PUT** /organizations/{organizationId}/brandingPolicies/priorities | Update the priority ordering of an organization&#39;s branding policies.



## getOrganizationBrandingPoliciesPriorities_2

> GetOrganizationBrandingPoliciesPriorities200Response getOrganizationBrandingPoliciesPriorities_2(organizationId)

Return the branding policy IDs of an organization in priority order

Return the branding policy IDs of an organization in priority order. IDs are ordered in ascending order of priority (IDs later in the array have higher priority).

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.PrioritiesApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationBrandingPoliciesPriorities_2(organizationId, (error, data, response) => {
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

[**GetOrganizationBrandingPoliciesPriorities200Response**](GetOrganizationBrandingPoliciesPriorities200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateOrganizationBrandingPoliciesPriorities_2

> GetOrganizationBrandingPoliciesPriorities200Response updateOrganizationBrandingPoliciesPriorities_2(organizationId, opts)

Update the priority ordering of an organization&#39;s branding policies.

Update the priority ordering of an organization&#39;s branding policies.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.PrioritiesApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'updateOrganizationBrandingPoliciesPrioritiesRequest': new MerakiDashboardApi.UpdateOrganizationBrandingPoliciesPrioritiesRequest() // UpdateOrganizationBrandingPoliciesPrioritiesRequest | 
};
apiInstance.updateOrganizationBrandingPoliciesPriorities_2(organizationId, opts, (error, data, response) => {
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
 **updateOrganizationBrandingPoliciesPrioritiesRequest** | [**UpdateOrganizationBrandingPoliciesPrioritiesRequest**](UpdateOrganizationBrandingPoliciesPrioritiesRequest.md)|  | [optional] 

### Return type

[**GetOrganizationBrandingPoliciesPriorities200Response**](GetOrganizationBrandingPoliciesPriorities200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

