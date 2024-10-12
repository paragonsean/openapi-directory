# SnykApi.EntitlementsApi

All URIs are relative to *https://api.snyk.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAnOrganizationsEntitlementValue**](EntitlementsApi.md#getAnOrganizationsEntitlementValue) | **GET** /org/{orgId}/entitlement/{entitlementKey} | Get an organization&#39;s entitlement value
[**listAllEntitlements**](EntitlementsApi.md#listAllEntitlements) | **GET** /org/{orgId}/entitlements | List all entitlements



## getAnOrganizationsEntitlementValue

> getAnOrganizationsEntitlementValue(orgId, entitlementKey)

Get an organization&#39;s entitlement value



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.EntitlementsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID to query the entitlement for. The `API_KEY` must have access to this organization.
let entitlementKey = "reports"; // String | The entitlement to query.
apiInstance.getAnOrganizationsEntitlementValue(orgId, entitlementKey, (error, data, response) => {
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
 **orgId** | **String**| The organization ID to query the entitlement for. The &#x60;API_KEY&#x60; must have access to this organization. | 
 **entitlementKey** | **String**| The entitlement to query. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## listAllEntitlements

> listAllEntitlements(orgId)

List all entitlements



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.EntitlementsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID to list entitlements for. The `API_KEY` must have access to this organization.
apiInstance.listAllEntitlements(orgId, (error, data, response) => {
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
 **orgId** | **String**| The organization ID to list entitlements for. The &#x60;API_KEY&#x60; must have access to this organization. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8

