# MerakiDashboardApi.OpenAPISpecApi

All URIs are relative to *https://api.meraki.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOrganizationOpenapiSpec**](OpenAPISpecApi.md#getOrganizationOpenapiSpec) | **GET** /organizations/{organizationId}/openapiSpec | Return the OpenAPI 2.0 Specification of the organization&#39;s API documentation in JSON



## getOrganizationOpenapiSpec

> Object getOrganizationOpenapiSpec(organizationId)

Return the OpenAPI 2.0 Specification of the organization&#39;s API documentation in JSON

Return the OpenAPI 2.0 Specification of the organization&#39;s API documentation in JSON

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.OpenAPISpecApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationOpenapiSpec(organizationId, (error, data, response) => {
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

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

