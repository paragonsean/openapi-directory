# MerakiDashboardApi.ApnsCertApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOrganizationSmApnsCert_1**](ApnsCertApi.md#getOrganizationSmApnsCert_1) | **GET** /organizations/{organizationId}/sm/apnsCert | Get the organization&#39;s APNS certificate



## getOrganizationSmApnsCert_1

> GetOrganizationSmApnsCert200Response getOrganizationSmApnsCert_1(organizationId)

Get the organization&#39;s APNS certificate

Get the organization&#39;s APNS certificate

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.ApnsCertApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationSmApnsCert_1(organizationId, (error, data, response) => {
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

[**GetOrganizationSmApnsCert200Response**](GetOrganizationSmApnsCert200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

