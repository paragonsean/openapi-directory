# PaylocityApi.EarningsApi

All URIs are relative to *https://api.paylocity.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addOrUpdateAnEmployeeEarning**](EarningsApi.md#addOrUpdateAnEmployeeEarning) | **PUT** /v2/companies/{companyId}/employees/{employeeId}/earnings | Add/Update Earning
[**deleteEarningByEarningCodeAndStartDate**](EarningsApi.md#deleteEarningByEarningCodeAndStartDate) | **DELETE** /v2/companies/{companyId}/employees/{employeeId}/earnings/{earningCode}/{startDate} | Delete Earning by Earning Code and Start Date
[**getAllEarnings**](EarningsApi.md#getAllEarnings) | **GET** /v2/companies/{companyId}/employees/{employeeId}/earnings | Get All Earnings
[**getEarningByEarningCodeAndStartDate**](EarningsApi.md#getEarningByEarningCodeAndStartDate) | **GET** /v2/companies/{companyId}/employees/{employeeId}/earnings/{earningCode}/{startDate} | Get Earning by Earning Code and Start Date
[**getEarningsByEarningCode**](EarningsApi.md#getEarningsByEarningCode) | **GET** /v2/companies/{companyId}/employees/{employeeId}/earnings/{earningCode} | Get Earnings by Earning Code



## addOrUpdateAnEmployeeEarning

> addOrUpdateAnEmployeeEarning(companyId, employeeId, earning)

Add/Update Earning

Add/Update Earning API sends new or updated employee earnings information directly to Web Pay.

### Example

```javascript
import PaylocityApi from 'paylocity_api';
let defaultClient = PaylocityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: paylocity_auth
let paylocity_auth = defaultClient.authentications['paylocity_auth'];
paylocity_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PaylocityApi.EarningsApi();
let companyId = "companyId_example"; // String | Company Id
let employeeId = "employeeId_example"; // String | Employee Id
let earning = new PaylocityApi.Earning(); // Earning | Earning Model
apiInstance.addOrUpdateAnEmployeeEarning(companyId, employeeId, earning, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **companyId** | **String**| Company Id | 
 **employeeId** | **String**| Employee Id | 
 **earning** | [**Earning**](Earning.md)| Earning Model | 

### Return type

null (empty response body)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteEarningByEarningCodeAndStartDate

> deleteEarningByEarningCodeAndStartDate(companyId, employeeId, earningCode, startDate)

Delete Earning by Earning Code and Start Date

Delete Earning by Earning Code and Start Date

### Example

```javascript
import PaylocityApi from 'paylocity_api';
let defaultClient = PaylocityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: paylocity_auth
let paylocity_auth = defaultClient.authentications['paylocity_auth'];
paylocity_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PaylocityApi.EarningsApi();
let companyId = "companyId_example"; // String | Company Id
let employeeId = "employeeId_example"; // String | Employee Id
let earningCode = "earningCode_example"; // String | Earning Code
let startDate = "startDate_example"; // String | Start Date
apiInstance.deleteEarningByEarningCodeAndStartDate(companyId, employeeId, earningCode, startDate, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **companyId** | **String**| Company Id | 
 **employeeId** | **String**| Employee Id | 
 **earningCode** | **String**| Earning Code | 
 **startDate** | **String**| Start Date | 

### Return type

null (empty response body)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllEarnings

> [Earning] getAllEarnings(companyId, employeeId)

Get All Earnings

Get All Earnings returns all earnings for the selected employee.

### Example

```javascript
import PaylocityApi from 'paylocity_api';
let defaultClient = PaylocityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: paylocity_auth
let paylocity_auth = defaultClient.authentications['paylocity_auth'];
paylocity_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PaylocityApi.EarningsApi();
let companyId = "companyId_example"; // String | Company Id
let employeeId = "employeeId_example"; // String | Employee Id
apiInstance.getAllEarnings(companyId, employeeId, (error, data, response) => {
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
 **companyId** | **String**| Company Id | 
 **employeeId** | **String**| Employee Id | 

### Return type

[**[Earning]**](Earning.md)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEarningByEarningCodeAndStartDate

> Earning getEarningByEarningCodeAndStartDate(companyId, employeeId, earningCode, startDate)

Get Earning by Earning Code and Start Date

Get Earnings returns the single earning with the provided earning code and start date for the selected employee.

### Example

```javascript
import PaylocityApi from 'paylocity_api';
let defaultClient = PaylocityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: paylocity_auth
let paylocity_auth = defaultClient.authentications['paylocity_auth'];
paylocity_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PaylocityApi.EarningsApi();
let companyId = "companyId_example"; // String | Company Id
let employeeId = "employeeId_example"; // String | Employee Id
let earningCode = "earningCode_example"; // String | Earning Code
let startDate = "startDate_example"; // String | Start Date
apiInstance.getEarningByEarningCodeAndStartDate(companyId, employeeId, earningCode, startDate, (error, data, response) => {
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
 **companyId** | **String**| Company Id | 
 **employeeId** | **String**| Employee Id | 
 **earningCode** | **String**| Earning Code | 
 **startDate** | **String**| Start Date | 

### Return type

[**Earning**](Earning.md)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEarningsByEarningCode

> [Earning] getEarningsByEarningCode(companyId, employeeId, earningCode)

Get Earnings by Earning Code

Get Earnings returns all earnings with the provided earning code for the selected employee.

### Example

```javascript
import PaylocityApi from 'paylocity_api';
let defaultClient = PaylocityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: paylocity_auth
let paylocity_auth = defaultClient.authentications['paylocity_auth'];
paylocity_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PaylocityApi.EarningsApi();
let companyId = "companyId_example"; // String | Company Id
let employeeId = "employeeId_example"; // String | Employee Id
let earningCode = "earningCode_example"; // String | Earning Code
apiInstance.getEarningsByEarningCode(companyId, employeeId, earningCode, (error, data, response) => {
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
 **companyId** | **String**| Company Id | 
 **employeeId** | **String**| Employee Id | 
 **earningCode** | **String**| Earning Code | 

### Return type

[**[Earning]**](Earning.md)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

