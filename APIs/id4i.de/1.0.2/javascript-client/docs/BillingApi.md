# Id4iApi.BillingApi

All URIs are relative to *http://backend.id4i.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPositionsForOrganization**](BillingApi.md#getPositionsForOrganization) | **GET** /api/v1/billing/{organizationId}/positions | Get billing positions for a given organization
[**getSumForOrganization**](BillingApi.md#getSumForOrganization) | **GET** /api/v1/billing/{organizationId} | Get billing amount of services for a given organization



## getPositionsForOrganization

> [BillingPosition] getPositionsForOrganization(organizationId, opts)

Get billing positions for a given organization

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.BillingApi();
let organizationId = "organizationId_example"; // String | The organization to compute the billing information for
let opts = {
  'fromDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Billing start date
  'toDate': new Date("2013-10-20T19:20:30+01:00") // Date | Billing end date
};
apiInstance.getPositionsForOrganization(organizationId, opts, (error, data, response) => {
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
 **organizationId** | **String**| The organization to compute the billing information for | 
 **fromDate** | **Date**| Billing start date | [optional] 
 **toDate** | **Date**| Billing end date | [optional] 

### Return type

[**[BillingPosition]**](BillingPosition.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getSumForOrganization

> ServiceCosts getSumForOrganization(organizationId, opts)

Get billing amount of services for a given organization

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.BillingApi();
let organizationId = "organizationId_example"; // String | The organization to compute the billing information for
let opts = {
  'fromDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Billing start date
  'toDate': new Date("2013-10-20T19:20:30+01:00") // Date | Billing end date
};
apiInstance.getSumForOrganization(organizationId, opts, (error, data, response) => {
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
 **organizationId** | **String**| The organization to compute the billing information for | 
 **fromDate** | **Date**| Billing start date | [optional] 
 **toDate** | **Date**| Billing end date | [optional] 

### Return type

[**ServiceCosts**](ServiceCosts.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

