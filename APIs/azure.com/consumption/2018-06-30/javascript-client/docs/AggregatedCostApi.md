# ConsumptionManagementClient.AggregatedCostApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggregatedCostGetByManagementGroup**](AggregatedCostApi.md#aggregatedCostGetByManagementGroup) | **GET** /providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.Consumption/aggregatedcost | 
[**aggregatedCostGetForBillingPeriodByManagementGroup**](AggregatedCostApi.md#aggregatedCostGetForBillingPeriodByManagementGroup) | **GET** /providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}/Microsoft.Consumption/aggregatedcost | 



## aggregatedCostGetByManagementGroup

> ManagementGroupAggregatedCostResult aggregatedCostGetByManagementGroup(managementGroupId, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-06-30.
apiInstance.aggregatedCostGetByManagementGroup(managementGroupId, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-06-30. | 

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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-06-30.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-06-30. | 

### Return type

[**ManagementGroupAggregatedCostResult**](ManagementGroupAggregatedCostResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

