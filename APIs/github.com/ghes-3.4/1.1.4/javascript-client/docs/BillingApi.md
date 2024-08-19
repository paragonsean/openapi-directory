# GitHubV3RestApi.BillingApi

All URIs are relative to *https://github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billingGetGithubAdvancedSecurityBillingGhe**](BillingApi.md#billingGetGithubAdvancedSecurityBillingGhe) | **GET** /enterprises/{enterprise}/settings/billing/advanced-security | Get GitHub Advanced Security active committers for an enterprise
[**billingGetGithubAdvancedSecurityBillingOrg**](BillingApi.md#billingGetGithubAdvancedSecurityBillingOrg) | **GET** /orgs/{org}/settings/billing/advanced-security | Get GitHub Advanced Security active committers for an organization



## billingGetGithubAdvancedSecurityBillingGhe

> AdvancedSecurityActiveCommitters billingGetGithubAdvancedSecurityBillingGhe(enterprise, opts)

Get GitHub Advanced Security active committers for an enterprise

Gets the GitHub Advanced Security active committers for an enterprise per repository.  Each distinct user login across all repositories is counted as a single Advanced Security seat, so the &#x60;total_advanced_security_committers&#x60; is not the sum of active_users for each repository.  The total number of repositories with committer information is tracked by the &#x60;total_count&#x60; field.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.BillingApi();
let enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.billingGetGithubAdvancedSecurityBillingGhe(enterprise, opts, (error, data, response) => {
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
 **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**AdvancedSecurityActiveCommitters**](AdvancedSecurityActiveCommitters.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingGetGithubAdvancedSecurityBillingOrg

> AdvancedSecurityActiveCommitters billingGetGithubAdvancedSecurityBillingOrg(org, opts)

Get GitHub Advanced Security active committers for an organization

Gets the GitHub Advanced Security active committers for an organization per repository.  Each distinct user login across all repositories is counted as a single Advanced Security seat, so the &#x60;total_advanced_security_committers&#x60; is not the sum of advanced_security_committers for each repository.  If this organization defers to an enterprise for billing, the &#x60;total_advanced_security_committers&#x60; returned from the organization API may include some users that are in more than one organization, so they will only consume a single Advanced Security seat at the enterprise level.  The total number of repositories with committer information is tracked by the &#x60;total_count&#x60; field.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.BillingApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.billingGetGithubAdvancedSecurityBillingOrg(org, opts, (error, data, response) => {
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
 **org** | **String**| The organization name. The name is not case sensitive. | 
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**AdvancedSecurityActiveCommitters**](AdvancedSecurityActiveCommitters.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

