# ConsumptionManagementClient.UsageDetailsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usageDetailsDownload**](UsageDetailsApi.md#usageDetailsDownload) | **POST** /{scope}/providers/Microsoft.Consumption/usageDetails/download | 
[**usageDetailsList**](UsageDetailsApi.md#usageDetailsList) | **GET** /{scope}/providers/Microsoft.Consumption/usageDetails | 



## usageDetailsDownload

> UsageDetailsDownloadResponse usageDetailsDownload(scope, apiVersion, opts)



Download usage details data.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.UsageDetailsApi();
let scope = "scope_example"; // String | The scope associated with usage details operations. This includes '/subscriptions/{subscriptionId}/' for subscription scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope, '/providers/Microsoft.Billing/departments/{departmentId}' for Department scope, '/providers/Microsoft.Billing/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope and '/providers/Microsoft.Management/managementGroups/{managementGroupId}' for Management Group scope. For subscription, billing account, department, enrollment account and management group, you can also add billing period to the scope using '/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}'. For e.g. to specify billing period at department scope use '/providers/Microsoft.Billing/departments/{departmentId}/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}'
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-04-01-preview.
let opts = {
  'metric': "metric_example" // String | Allows to select different type of cost/usage records.
};
apiInstance.usageDetailsDownload(scope, apiVersion, opts, (error, data, response) => {
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
 **scope** | **String**| The scope associated with usage details operations. This includes &#39;/subscriptions/{subscriptionId}/&#39; for subscription scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for Billing Account scope, &#39;/providers/Microsoft.Billing/departments/{departmentId}&#39; for Department scope, &#39;/providers/Microsoft.Billing/enrollmentAccounts/{enrollmentAccountId}&#39; for EnrollmentAccount scope and &#39;/providers/Microsoft.Management/managementGroups/{managementGroupId}&#39; for Management Group scope. For subscription, billing account, department, enrollment account and management group, you can also add billing period to the scope using &#39;/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}&#39;. For e.g. to specify billing period at department scope use &#39;/providers/Microsoft.Billing/departments/{departmentId}/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}&#39; | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-04-01-preview. | 
 **metric** | **String**| Allows to select different type of cost/usage records. | [optional] 

### Return type

[**UsageDetailsDownloadResponse**](UsageDetailsDownloadResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usageDetailsList

> UsageDetailsListResult usageDetailsList(scope, apiVersion, opts)



Lists the usage details for the defined scope. Usage details are available via this API only for May 1, 2014 or later.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.UsageDetailsApi();
let scope = "scope_example"; // String | The scope associated with usage details operations. This includes '/subscriptions/{subscriptionId}/' for subscription scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope, '/providers/Microsoft.Billing/departments/{departmentId}' for Department scope, '/providers/Microsoft.Billing/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope and '/providers/Microsoft.Management/managementGroups/{managementGroupId}' for Management Group scope. For subscription, billing account, department, enrollment account and management group, you can also add billing period to the scope using '/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}'. For e.g. to specify billing period at department scope use '/providers/Microsoft.Billing/departments/{departmentId}/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}'
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-04-01-preview.
let opts = {
  'expand': "expand_example", // String | May be used to expand the properties/additionalInfo or properties/meterDetails within a list of usage details. By default, these fields are not included when listing usage details.
  'filter': "filter_example", // String | May be used to filter usageDetails by properties/resourceGroup, properties/resourceName, properties/resourceId, properties/chargeType, properties/reservationId or tags. The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is a key value pair string where key and value is separated by a colon (:).
  'skiptoken': "skiptoken_example", // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
  'top': 56, // Number | May be used to limit the number of results to the most recent N usageDetails.
  'metric': "metric_example" // String | Allows to select different type of cost/usage records.
};
apiInstance.usageDetailsList(scope, apiVersion, opts, (error, data, response) => {
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
 **scope** | **String**| The scope associated with usage details operations. This includes &#39;/subscriptions/{subscriptionId}/&#39; for subscription scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for Billing Account scope, &#39;/providers/Microsoft.Billing/departments/{departmentId}&#39; for Department scope, &#39;/providers/Microsoft.Billing/enrollmentAccounts/{enrollmentAccountId}&#39; for EnrollmentAccount scope and &#39;/providers/Microsoft.Management/managementGroups/{managementGroupId}&#39; for Management Group scope. For subscription, billing account, department, enrollment account and management group, you can also add billing period to the scope using &#39;/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}&#39;. For e.g. to specify billing period at department scope use &#39;/providers/Microsoft.Billing/departments/{departmentId}/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}&#39; | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-04-01-preview. | 
 **expand** | **String**| May be used to expand the properties/additionalInfo or properties/meterDetails within a list of usage details. By default, these fields are not included when listing usage details. | [optional] 
 **filter** | **String**| May be used to filter usageDetails by properties/resourceGroup, properties/resourceName, properties/resourceId, properties/chargeType, properties/reservationId or tags. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:). | [optional] 
 **skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] 
 **top** | **Number**| May be used to limit the number of results to the most recent N usageDetails. | [optional] 
 **metric** | **String**| Allows to select different type of cost/usage records. | [optional] 

### Return type

[**UsageDetailsListResult**](UsageDetailsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

