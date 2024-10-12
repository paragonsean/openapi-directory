# MerakiDashboardApi.AlertTypesApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOrganizationWebhooksAlertTypes_2**](AlertTypesApi.md#getOrganizationWebhooksAlertTypes_2) | **GET** /organizations/{organizationId}/webhooks/alertTypes | Return a list of alert types to be used with managing webhook alerts



## getOrganizationWebhooksAlertTypes_2

> [Object] getOrganizationWebhooksAlertTypes_2(organizationId, opts)

Return a list of alert types to be used with managing webhook alerts

Return a list of alert types to be used with managing webhook alerts

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AlertTypesApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'productType': "productType_example" // String | Filter sample alerts to a specific product type
};
apiInstance.getOrganizationWebhooksAlertTypes_2(organizationId, opts, (error, data, response) => {
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
 **productType** | **String**| Filter sample alerts to a specific product type | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

