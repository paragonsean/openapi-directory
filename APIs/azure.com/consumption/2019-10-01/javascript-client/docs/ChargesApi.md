# ConsumptionManagementClient.ChargesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chargesList**](ChargesApi.md#chargesList) | **GET** /{scope}/providers/Microsoft.Consumption/charges | 



## chargesList

> ChargesListResult chargesList(scope, apiVersion, opts)



Lists the charges based for the defined scope.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.ChargesApi();
let scope = "scope_example"; // String | The scope associated with charges operations. This includes '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for Department scope, and '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope. For department and enrollment accounts, you can also add billing period to the scope using '/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}'. For e.g. to specify billing period at department scope use '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}'. Also, Modern Commerce Account scopes are '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for billingAccount scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for billingProfile scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}' for invoiceSection scope, and 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}' specific for partners.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01.
let opts = {
  'startDate': "startDate_example", // String | Start date
  'endDate': "endDate_example", // String | End date
  'filter': "filter_example", // String | May be used to filter charges by properties/usageEnd (Utc time), properties/usageStart (Utc time). The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is a key value pair string where key and value is separated by a colon (:).
  'apply': "apply_example" // String | May be used to group charges for billingAccount scope by properties/billingProfileId, properties/invoiceSectionId, properties/customerId (specific for Partner Led), or for billingProfile scope by properties/invoiceSectionId.
};
apiInstance.chargesList(scope, apiVersion, opts, (error, data, response) => {
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
 **scope** | **String**| The scope associated with charges operations. This includes &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}&#39; for Department scope, and &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}&#39; for EnrollmentAccount scope. For department and enrollment accounts, you can also add billing period to the scope using &#39;/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}&#39;. For e.g. to specify billing period at department scope use &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}&#39;. Also, Modern Commerce Account scopes are &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for billingAccount scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}&#39; for billingProfile scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}&#39; for invoiceSection scope, and &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}&#39; specific for partners. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01. | 
 **startDate** | **String**| Start date | [optional] 
 **endDate** | **String**| End date | [optional] 
 **filter** | **String**| May be used to filter charges by properties/usageEnd (Utc time), properties/usageStart (Utc time). The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:). | [optional] 
 **apply** | **String**| May be used to group charges for billingAccount scope by properties/billingProfileId, properties/invoiceSectionId, properties/customerId (specific for Partner Led), or for billingProfile scope by properties/invoiceSectionId. | [optional] 

### Return type

[**ChargesListResult**](ChargesListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

