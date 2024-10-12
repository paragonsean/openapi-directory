# FireFinancialServicesBusinessApi.DirectDebitsApi

All URIs are relative to *https://api.fire.com/business*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activateMandate**](DirectDebitsApi.md#activateMandate) | **POST** /v1/mandates/{mandateUuid}/activate | Activate a direct debit mandate
[**cancelMandateByUuid**](DirectDebitsApi.md#cancelMandateByUuid) | **POST** /v1/mandates/{mandateUuid}/cancel | Cancel a direct debit mandate
[**getDirectDebitByUuid**](DirectDebitsApi.md#getDirectDebitByUuid) | **GET** /v1/directdebits/{directDebitUuid} | Get the details of a direct debit
[**getDirectDebitMandates**](DirectDebitsApi.md#getDirectDebitMandates) | **GET** /v1/mandates | List all direct debit mandates
[**getDirectDebitsForMandateUuid**](DirectDebitsApi.md#getDirectDebitsForMandateUuid) | **GET** /v1/directdebits | Get all DD payments associated with a direct debit mandate
[**getMandate**](DirectDebitsApi.md#getMandate) | **GET** /v1/mandates/{mandateUuid} | Get direct debit mandate details
[**rejectDirectDebit**](DirectDebitsApi.md#rejectDirectDebit) | **POST** /v1/directdebits/{directDebitUuid}/reject | Reject a direct debit payment
[**updateMandateAlias**](DirectDebitsApi.md#updateMandateAlias) | **POST** /v1/mandates/{mandateUuid} | Update a direct debit mandate alias



## activateMandate

> activateMandate(mandateUuid)

Activate a direct debit mandate

This endpoint can only be used to activate a direct debit mandate when it is in the status REJECT_REQUESTED (even if the account has direct debits disabled). This action will also enable the account for direct debits if it was previously set to be disabled. The permision needed to access this endpoint is PERM_BUSINESS_POST_MANDATE_ACTIVATE 

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.DirectDebitsApi();
let mandateUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
apiInstance.activateMandate(mandateUuid, (error, data, response) => {
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
 **mandateUuid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## cancelMandateByUuid

> cancelMandateByUuid(mandateUuid)

Cancel a direct debit mandate

This endpoint allows you to cancel a direct debit mandate. The permision needed to access this endpoint is PERM_BUSINESS_POST_MANDATE_CANCEL 

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.DirectDebitsApi();
let mandateUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
apiInstance.cancelMandateByUuid(mandateUuid, (error, data, response) => {
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
 **mandateUuid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDirectDebitByUuid

> DirectDebit getDirectDebitByUuid(directDebitUuid)

Get the details of a direct debit

Retrieve all details of a single direct debit collection/payment, whether successful or not. The permision needed to access this endpoint is **PERM_BUSINESS_GET_DIRECT_DEBIT** 

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.DirectDebitsApi();
let directDebitUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
apiInstance.getDirectDebitByUuid(directDebitUuid, (error, data, response) => {
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
 **directDebitUuid** | **String**|  | 

### Return type

[**DirectDebit**](DirectDebit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDirectDebitMandates

> Mandates getDirectDebitMandates()

List all direct debit mandates

The permision needed to access this endpoint is PERM_BUSINESS_GET_MANDATES 

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.DirectDebitsApi();
apiInstance.getDirectDebitMandates((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Mandates**](Mandates.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDirectDebitsForMandateUuid

> DirectDebits getDirectDebitsForMandateUuid(mandateUuid)

Get all DD payments associated with a direct debit mandate

Retrieve all direct debit payments associated with a direct debit mandate. The permision needed to access this endpoint is PERM_BUSINESS_GET_DIRECT_DEBITS 

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.DirectDebitsApi();
let mandateUuid = "1A07774B-1461-4595-BC4B-423B739712AF"; // String | The mandate UUID to retrieve
apiInstance.getDirectDebitsForMandateUuid(mandateUuid, (error, data, response) => {
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
 **mandateUuid** | **String**| The mandate UUID to retrieve | 

### Return type

[**DirectDebits**](DirectDebits.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMandate

> Mandate getMandate(mandateUuid)

Get direct debit mandate details

Retrieve all details for a direct debit mandate. The permision needed to access this endpoint is PERM_BUSINESS_GET_MANDATE 

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.DirectDebitsApi();
let mandateUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
apiInstance.getMandate(mandateUuid, (error, data, response) => {
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
 **mandateUuid** | **String**|  | 

### Return type

[**Mandate**](Mandate.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rejectDirectDebit

> rejectDirectDebit(directDebitUuid)

Reject a direct debit payment

This endpoint allows you to reject a direct debit payment where the status is still set to RECEIVED. Permission name PERM_BUSINESS_POST_DIRECT_DEBIT_REJECT 

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.DirectDebitsApi();
let directDebitUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
apiInstance.rejectDirectDebit(directDebitUuid, (error, data, response) => {
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
 **directDebitUuid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateMandateAlias

> updateMandateAlias(mandateUuid)

Update a direct debit mandate alias

Update Direct Debit Mandate Alias The permision needed to access this endpoint is PERM_BUSINESS_PUT_MANDATE 

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.DirectDebitsApi();
let mandateUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
apiInstance.updateMandateAlias(mandateUuid, (error, data, response) => {
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
 **mandateUuid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

