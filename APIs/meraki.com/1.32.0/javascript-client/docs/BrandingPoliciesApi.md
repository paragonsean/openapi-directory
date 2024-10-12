# MerakiDashboardApi.BrandingPoliciesApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createOrganizationBrandingPolicy_1**](BrandingPoliciesApi.md#createOrganizationBrandingPolicy_1) | **POST** /organizations/{organizationId}/brandingPolicies | Add a new branding policy to an organization
[**deleteOrganizationBrandingPolicy_1**](BrandingPoliciesApi.md#deleteOrganizationBrandingPolicy_1) | **DELETE** /organizations/{organizationId}/brandingPolicies/{brandingPolicyId} | Delete a branding policy
[**getOrganizationBrandingPoliciesPriorities_1**](BrandingPoliciesApi.md#getOrganizationBrandingPoliciesPriorities_1) | **GET** /organizations/{organizationId}/brandingPolicies/priorities | Return the branding policy IDs of an organization in priority order
[**getOrganizationBrandingPolicies_1**](BrandingPoliciesApi.md#getOrganizationBrandingPolicies_1) | **GET** /organizations/{organizationId}/brandingPolicies | List the branding policies of an organization
[**getOrganizationBrandingPolicy_1**](BrandingPoliciesApi.md#getOrganizationBrandingPolicy_1) | **GET** /organizations/{organizationId}/brandingPolicies/{brandingPolicyId} | Return a branding policy
[**updateOrganizationBrandingPoliciesPriorities_1**](BrandingPoliciesApi.md#updateOrganizationBrandingPoliciesPriorities_1) | **PUT** /organizations/{organizationId}/brandingPolicies/priorities | Update the priority ordering of an organization&#39;s branding policies.
[**updateOrganizationBrandingPolicy_1**](BrandingPoliciesApi.md#updateOrganizationBrandingPolicy_1) | **PUT** /organizations/{organizationId}/brandingPolicies/{brandingPolicyId} | Update a branding policy



## createOrganizationBrandingPolicy_1

> CreateOrganizationBrandingPolicy201Response createOrganizationBrandingPolicy_1(organizationId, opts)

Add a new branding policy to an organization

Add a new branding policy to an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.BrandingPoliciesApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'createOrganizationBrandingPolicyRequest': new MerakiDashboardApi.CreateOrganizationBrandingPolicyRequest() // CreateOrganizationBrandingPolicyRequest | 
};
apiInstance.createOrganizationBrandingPolicy_1(organizationId, opts, (error, data, response) => {
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
 **createOrganizationBrandingPolicyRequest** | [**CreateOrganizationBrandingPolicyRequest**](CreateOrganizationBrandingPolicyRequest.md)|  | [optional] 

### Return type

[**CreateOrganizationBrandingPolicy201Response**](CreateOrganizationBrandingPolicy201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteOrganizationBrandingPolicy_1

> deleteOrganizationBrandingPolicy_1(organizationId, brandingPolicyId)

Delete a branding policy

Delete a branding policy

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.BrandingPoliciesApi();
let organizationId = "organizationId_example"; // String | 
let brandingPolicyId = "brandingPolicyId_example"; // String | 
apiInstance.deleteOrganizationBrandingPolicy_1(organizationId, brandingPolicyId, (error, data, response) => {
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
 **brandingPolicyId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganizationBrandingPoliciesPriorities_1

> GetOrganizationBrandingPoliciesPriorities200Response getOrganizationBrandingPoliciesPriorities_1(organizationId)

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

let apiInstance = new MerakiDashboardApi.BrandingPoliciesApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationBrandingPoliciesPriorities_1(organizationId, (error, data, response) => {
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


## getOrganizationBrandingPolicies_1

> [GetOrganizationBrandingPolicies200ResponseInner] getOrganizationBrandingPolicies_1(organizationId)

List the branding policies of an organization

List the branding policies of an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.BrandingPoliciesApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationBrandingPolicies_1(organizationId, (error, data, response) => {
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

[**[GetOrganizationBrandingPolicies200ResponseInner]**](GetOrganizationBrandingPolicies200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationBrandingPolicy_1

> GetOrganizationBrandingPolicies200ResponseInner getOrganizationBrandingPolicy_1(organizationId, brandingPolicyId)

Return a branding policy

Return a branding policy

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.BrandingPoliciesApi();
let organizationId = "organizationId_example"; // String | 
let brandingPolicyId = "brandingPolicyId_example"; // String | 
apiInstance.getOrganizationBrandingPolicy_1(organizationId, brandingPolicyId, (error, data, response) => {
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
 **brandingPolicyId** | **String**|  | 

### Return type

[**GetOrganizationBrandingPolicies200ResponseInner**](GetOrganizationBrandingPolicies200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateOrganizationBrandingPoliciesPriorities_1

> GetOrganizationBrandingPoliciesPriorities200Response updateOrganizationBrandingPoliciesPriorities_1(organizationId, opts)

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

let apiInstance = new MerakiDashboardApi.BrandingPoliciesApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'updateOrganizationBrandingPoliciesPrioritiesRequest': new MerakiDashboardApi.UpdateOrganizationBrandingPoliciesPrioritiesRequest() // UpdateOrganizationBrandingPoliciesPrioritiesRequest | 
};
apiInstance.updateOrganizationBrandingPoliciesPriorities_1(organizationId, opts, (error, data, response) => {
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


## updateOrganizationBrandingPolicy_1

> GetOrganizationBrandingPolicies200ResponseInner updateOrganizationBrandingPolicy_1(organizationId, brandingPolicyId, opts)

Update a branding policy

Update a branding policy

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.BrandingPoliciesApi();
let organizationId = "organizationId_example"; // String | 
let brandingPolicyId = "brandingPolicyId_example"; // String | 
let opts = {
  'updateOrganizationBrandingPolicyRequest': new MerakiDashboardApi.UpdateOrganizationBrandingPolicyRequest() // UpdateOrganizationBrandingPolicyRequest | 
};
apiInstance.updateOrganizationBrandingPolicy_1(organizationId, brandingPolicyId, opts, (error, data, response) => {
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
 **brandingPolicyId** | **String**|  | 
 **updateOrganizationBrandingPolicyRequest** | [**UpdateOrganizationBrandingPolicyRequest**](UpdateOrganizationBrandingPolicyRequest.md)|  | [optional] 

### Return type

[**GetOrganizationBrandingPolicies200ResponseInner**](GetOrganizationBrandingPolicies200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

