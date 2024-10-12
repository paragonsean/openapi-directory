# ConsumptionManagementClient.PriceSheetApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**priceSheetGet**](PriceSheetApi.md#priceSheetGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Consumption/pricesheets/default | 
[**priceSheetGetByBillingPeriod**](PriceSheetApi.md#priceSheetGetByBillingPeriod) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}/providers/Microsoft.Consumption/pricesheets/default | 



## priceSheetGet

> PriceSheetResult priceSheetGet(subscriptionId, apiVersion, opts)



Gets the price sheet for a scope by subscriptionId. Price sheet is available via this API only for May 1, 2014 or later.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.PriceSheetApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-05-01-preview.
let opts = {
  'expand': "expand_example", // String | May be used to expand the properties/meterDetails within a price sheet. By default, these fields are not included when returning price sheet.
  'skiptoken': "skiptoken_example", // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
  'top': 56 // Number | May be used to limit the number of results to the top N results.
};
apiInstance.priceSheetGet(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-05-01-preview. | 
 **expand** | **String**| May be used to expand the properties/meterDetails within a price sheet. By default, these fields are not included when returning price sheet. | [optional] 
 **skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] 
 **top** | **Number**| May be used to limit the number of results to the top N results. | [optional] 

### Return type

[**PriceSheetResult**](PriceSheetResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## priceSheetGetByBillingPeriod

> PriceSheetResult priceSheetGetByBillingPeriod(subscriptionId, apiVersion, billingPeriodName, opts)



Get the price sheet for a scope by subscriptionId and billing period. Price sheet is available via this API only for May 1, 2014 or later.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.PriceSheetApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-05-01-preview.
let billingPeriodName = "billingPeriodName_example"; // String | Billing Period Name.
let opts = {
  'expand': "expand_example", // String | May be used to expand the properties/meterDetails within a price sheet. By default, these fields are not included when returning price sheet.
  'skiptoken': "skiptoken_example", // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
  'top': 56 // Number | May be used to limit the number of results to the top N results.
};
apiInstance.priceSheetGetByBillingPeriod(subscriptionId, apiVersion, billingPeriodName, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-05-01-preview. | 
 **billingPeriodName** | **String**| Billing Period Name. | 
 **expand** | **String**| May be used to expand the properties/meterDetails within a price sheet. By default, these fields are not included when returning price sheet. | [optional] 
 **skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] 
 **top** | **Number**| May be used to limit the number of results to the top N results. | [optional] 

### Return type

[**PriceSheetResult**](PriceSheetResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

