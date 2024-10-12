# ConsumptionManagementClient.AggregatedCostApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggregatedCostGetByManagementGroup**](AggregatedCostApi.md#aggregatedCostGetByManagementGroup) | **GET** /providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.Consumption/aggregatedcost | 
[**aggregatedCostGetForBillingPeriodByManagementGroup**](AggregatedCostApi.md#aggregatedCostGetForBillingPeriodByManagementGroup) | **GET** /providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}/Microsoft.Consumption/aggregatedcost | 



## aggregatedCostGetByManagementGroup

> ManagementGroupAggregatedCostResult aggregatedCostGetByManagementGroup(managementGroupId, apiVersion, opts)



Provides the aggregate cost of a management group and all child management groups by current billing period.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.AggregatedCostApi();
let managementGroupId = "managementGroupId_example"; // String | Azure Management Group ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-01-01.
let opts = {
  'filter': "filter_example" // String | May be used to filter aggregated cost by properties/usageStart (Utc time), properties/usageEnd (Utc time). The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is a key value pair string where key and value is separated by a colon (:).
};
apiInstance.aggregatedCostGetByManagementGroup(managementGroupId, apiVersion, opts, (error, data, response) => {
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
 **managementGroupId** | **String**| Azure Management Group ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-01-01. | 
 **filter** | **String**| May be used to filter aggregated cost by properties/usageStart (Utc time), properties/usageEnd (Utc time). The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:). | [optional] 

### Return type

[**ManagementGroupAggregatedCostResult**](ManagementGroupAggregatedCostResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aggregatedCostGetForBillingPeriodByManagementGroup

> ManagementGroupAggregatedCostResult aggregatedCostGetForBillingPeriodByManagementGroup(managementGroupId, billingPeriodName, apiVersion)



Provides the aggregate cost of a management group and all child management groups by specified billing period

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.AggregatedCostApi();
let managementGroupId = "managementGroupId_example"; // String | Azure Management Group ID.
let billingPeriodName = "billingPeriodName_example"; // String | Billing Period Name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-01-01.
apiInstance.aggregatedCostGetForBillingPeriodByManagementGroup(managementGroupId, billingPeriodName, apiVersion, (error, data, response) => {
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
 **managementGroupId** | **String**| Azure Management Group ID. | 
 **billingPeriodName** | **String**| Billing Period Name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-01-01. | 

### Return type

[**ManagementGroupAggregatedCostResult**](ManagementGroupAggregatedCostResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

