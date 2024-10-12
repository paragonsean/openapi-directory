# ConsumptionManagementClient.ChargesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chargesListByDepartment**](ChargesApi.md#chargesListByDepartment) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}/providers/Microsoft.Consumption/charges | 
[**chargesListByEnrollmentAccount**](ChargesApi.md#chargesListByEnrollmentAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}/providers/Microsoft.Consumption/charges | 
[**chargesListForBillingPeriodByDepartment**](ChargesApi.md#chargesListForBillingPeriodByDepartment) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}/providers/Microsoft.Consumption/charges | 
[**chargesListForBillingPeriodByEnrollmentAccount**](ChargesApi.md#chargesListForBillingPeriodByEnrollmentAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}/providers/Microsoft.Consumption/charges | 



## chargesListByDepartment

> ChargesListResult chargesListByDepartment(billingAccountId, departmentId, apiVersion, opts)



Lists the charges by departmentId.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.ChargesApi();
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let departmentId = "departmentId_example"; // String | Department ID
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-10-01.
let opts = {
  'filter': "filter_example" // String | May be used to filter charges by properties/usageEnd (Utc time), properties/usageStart (Utc time). The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is a key value pair string where key and value is separated by a colon (:).
};
apiInstance.chargesListByDepartment(billingAccountId, departmentId, apiVersion, opts, (error, data, response) => {
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
 **billingAccountId** | **String**| BillingAccount ID | 
 **departmentId** | **String**| Department ID | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-10-01. | 
 **filter** | **String**| May be used to filter charges by properties/usageEnd (Utc time), properties/usageStart (Utc time). The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:). | [optional] 

### Return type

[**ChargesListResult**](ChargesListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chargesListByEnrollmentAccount

> ChargesListResult chargesListByEnrollmentAccount(billingAccountId, enrollmentAccountId, apiVersion, opts)



Lists the charges by enrollmentAccountId.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.ChargesApi();
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let enrollmentAccountId = "enrollmentAccountId_example"; // String | EnrollmentAccount ID
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-10-01.
let opts = {
  'filter': "filter_example" // String | May be used to filter charges by properties/usageEnd (Utc time), properties/usageStart (Utc time). The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is a key value pair string where key and value is separated by a colon (:).
};
apiInstance.chargesListByEnrollmentAccount(billingAccountId, enrollmentAccountId, apiVersion, opts, (error, data, response) => {
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
 **billingAccountId** | **String**| BillingAccount ID | 
 **enrollmentAccountId** | **String**| EnrollmentAccount ID | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-10-01. | 
 **filter** | **String**| May be used to filter charges by properties/usageEnd (Utc time), properties/usageStart (Utc time). The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:). | [optional] 

### Return type

[**ChargesListResult**](ChargesListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chargesListForBillingPeriodByDepartment

> ChargeSummary chargesListForBillingPeriodByDepartment(billingAccountId, departmentId, billingPeriodName, apiVersion, opts)



Lists the charges based on departmentId by billing period.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.ChargesApi();
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let departmentId = "departmentId_example"; // String | Department ID
let billingPeriodName = "billingPeriodName_example"; // String | Billing Period Name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-10-01.
let opts = {
  'filter': "filter_example" // String | May be used to filter charges by properties/usageEnd (Utc time), properties/usageStart (Utc time). The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is a key value pair string where key and value is separated by a colon (:).
};
apiInstance.chargesListForBillingPeriodByDepartment(billingAccountId, departmentId, billingPeriodName, apiVersion, opts, (error, data, response) => {
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
 **billingAccountId** | **String**| BillingAccount ID | 
 **departmentId** | **String**| Department ID | 
 **billingPeriodName** | **String**| Billing Period Name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-10-01. | 
 **filter** | **String**| May be used to filter charges by properties/usageEnd (Utc time), properties/usageStart (Utc time). The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:). | [optional] 

### Return type

[**ChargeSummary**](ChargeSummary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chargesListForBillingPeriodByEnrollmentAccount

> ChargeSummary chargesListForBillingPeriodByEnrollmentAccount(billingAccountId, enrollmentAccountId, billingPeriodName, apiVersion, opts)



Lists the charges based on enrollmentAccountId by billing period.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.ChargesApi();
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let enrollmentAccountId = "enrollmentAccountId_example"; // String | EnrollmentAccount ID
let billingPeriodName = "billingPeriodName_example"; // String | Billing Period Name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-10-01.
let opts = {
  'filter': "filter_example" // String | May be used to filter charges by properties/usageEnd (Utc time), properties/usageStart (Utc time). The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is a key value pair string where key and value is separated by a colon (:).
};
apiInstance.chargesListForBillingPeriodByEnrollmentAccount(billingAccountId, enrollmentAccountId, billingPeriodName, apiVersion, opts, (error, data, response) => {
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
 **billingAccountId** | **String**| BillingAccount ID | 
 **enrollmentAccountId** | **String**| EnrollmentAccount ID | 
 **billingPeriodName** | **String**| Billing Period Name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-10-01. | 
 **filter** | **String**| May be used to filter charges by properties/usageEnd (Utc time), properties/usageStart (Utc time). The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:). | [optional] 

### Return type

[**ChargeSummary**](ChargeSummary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

