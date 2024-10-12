# NordigenAccountInformationServicesApi.PaymentsApi

All URIs are relative to *https://ob.nordigen.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createPayment**](PaymentsApi.md#createPayment) | **POST** /api/v2/payments/ | 
[**deletePeriodicPayment**](PaymentsApi.md#deletePeriodicPayment) | **DELETE** /api/v2/payments/{id}/ | 
[**listMinimumRequiredFieldsForInstitution**](PaymentsApi.md#listMinimumRequiredFieldsForInstitution) | **GET** /api/v2/payments/fields/{institution_id}/ | 
[**listPayments**](PaymentsApi.md#listPayments) | **GET** /api/v2/payments/ | 
[**paymentsCreditorsCreate**](PaymentsApi.md#paymentsCreditorsCreate) | **POST** /api/v2/payments/creditors/ | 
[**paymentsCreditorsDestroy**](PaymentsApi.md#paymentsCreditorsDestroy) | **DELETE** /api/v2/payments/creditors/{id}/ | 
[**paymentsCreditorsList**](PaymentsApi.md#paymentsCreditorsList) | **GET** /api/v2/payments/creditors/ | 
[**paymentsCreditorsRetrieve**](PaymentsApi.md#paymentsCreditorsRetrieve) | **GET** /api/v2/payments/creditors/{id}/ | 
[**paymentsSubmitCreate**](PaymentsApi.md#paymentsSubmitCreate) | **POST** /api/v2/payments/{id}/submit/ | 
[**retrieveAllPaymentCreditorAccounts**](PaymentsApi.md#retrieveAllPaymentCreditorAccounts) | **GET** /api/v2/payments/account/ | 
[**retrievePayment**](PaymentsApi.md#retrievePayment) | **GET** /api/v2/payments/{id}/ | 



## createPayment

> PaymentWrite createPayment(paymentWriteRequest)



Create payment

### Example

```javascript
import NordigenAccountInformationServicesApi from 'nordigen_account_information_services_api';
let defaultClient = NordigenAccountInformationServicesApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwtAuth
let jwtAuth = defaultClient.authentications['jwtAuth'];
jwtAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NordigenAccountInformationServicesApi.PaymentsApi();
let paymentWriteRequest = new NordigenAccountInformationServicesApi.PaymentWriteRequest(); // PaymentWriteRequest | 
apiInstance.createPayment(paymentWriteRequest, (error, data, response) => {
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
 **paymentWriteRequest** | [**PaymentWriteRequest**](PaymentWriteRequest.md)|  | 

### Return type

[**PaymentWrite**](PaymentWrite.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json


## deletePeriodicPayment

> {String: Object} deletePeriodicPayment(id)



Delete periodic payment

### Example

```javascript
import NordigenAccountInformationServicesApi from 'nordigen_account_information_services_api';
let defaultClient = NordigenAccountInformationServicesApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwtAuth
let jwtAuth = defaultClient.authentications['jwtAuth'];
jwtAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NordigenAccountInformationServicesApi.PaymentsApi();
let id = "id_example"; // String | 
apiInstance.deletePeriodicPayment(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

**{String: Object}**

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMinimumRequiredFieldsForInstitution

> {String: Object} listMinimumRequiredFieldsForInstitution(institutionId)



List minimum required fields for institution

### Example

```javascript
import NordigenAccountInformationServicesApi from 'nordigen_account_information_services_api';
let defaultClient = NordigenAccountInformationServicesApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwtAuth
let jwtAuth = defaultClient.authentications['jwtAuth'];
jwtAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NordigenAccountInformationServicesApi.PaymentsApi();
let institutionId = "institutionId_example"; // String | 
apiInstance.listMinimumRequiredFieldsForInstitution(institutionId, (error, data, response) => {
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
 **institutionId** | **String**|  | 

### Return type

**{String: Object}**

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPayments

> PaginatedPaymentReadList listPayments(opts)



Retrieve all payments belonging to the company

### Example

```javascript
import NordigenAccountInformationServicesApi from 'nordigen_account_information_services_api';
let defaultClient = NordigenAccountInformationServicesApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwtAuth
let jwtAuth = defaultClient.authentications['jwtAuth'];
jwtAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NordigenAccountInformationServicesApi.PaymentsApi();
let opts = {
  'limit': 100, // Number | Number of results to return per page.
  'offset': 1 // Number | The initial index from which to return the results.
};
apiInstance.listPayments(opts, (error, data, response) => {
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
 **limit** | **Number**| Number of results to return per page. | [optional] [default to 100]
 **offset** | **Number**| The initial index from which to return the results. | [optional] [default to 1]

### Return type

[**PaginatedPaymentReadList**](PaginatedPaymentReadList.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## paymentsCreditorsCreate

> CreditorAccountWrite paymentsCreditorsCreate(creditorAccountWriteRequest)



API endpoints related to creditor accounts.

### Example

```javascript
import NordigenAccountInformationServicesApi from 'nordigen_account_information_services_api';
let defaultClient = NordigenAccountInformationServicesApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwtAuth
let jwtAuth = defaultClient.authentications['jwtAuth'];
jwtAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NordigenAccountInformationServicesApi.PaymentsApi();
let creditorAccountWriteRequest = new NordigenAccountInformationServicesApi.CreditorAccountWriteRequest(); // CreditorAccountWriteRequest | 
apiInstance.paymentsCreditorsCreate(creditorAccountWriteRequest, (error, data, response) => {
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
 **creditorAccountWriteRequest** | [**CreditorAccountWriteRequest**](CreditorAccountWriteRequest.md)|  | 

### Return type

[**CreditorAccountWrite**](CreditorAccountWrite.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json


## paymentsCreditorsDestroy

> paymentsCreditorsDestroy(id)



API endpoints related to creditor accounts.

### Example

```javascript
import NordigenAccountInformationServicesApi from 'nordigen_account_information_services_api';
let defaultClient = NordigenAccountInformationServicesApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwtAuth
let jwtAuth = defaultClient.authentications['jwtAuth'];
jwtAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NordigenAccountInformationServicesApi.PaymentsApi();
let id = "id_example"; // String | 
apiInstance.paymentsCreditorsDestroy(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## paymentsCreditorsList

> PaginatedCreditorAccountList paymentsCreditorsList(opts)



API endpoints related to creditor accounts.

### Example

```javascript
import NordigenAccountInformationServicesApi from 'nordigen_account_information_services_api';
let defaultClient = NordigenAccountInformationServicesApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwtAuth
let jwtAuth = defaultClient.authentications['jwtAuth'];
jwtAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NordigenAccountInformationServicesApi.PaymentsApi();
let opts = {
  'account': "account_example", // String | 
  'addressCountry': "addressCountry_example", // String | 
  'agent': "agent_example", // String | 
  'currency': "currency_example", // String | 
  'limit': 100, // Number | Number of results to return per page.
  'name': "name_example", // String | 
  'offset': 1, // Number | The initial index from which to return the results.
  'type': "type_example" // String | 
};
apiInstance.paymentsCreditorsList(opts, (error, data, response) => {
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
 **account** | **String**|  | [optional] 
 **addressCountry** | **String**|  | [optional] 
 **agent** | **String**|  | [optional] 
 **currency** | **String**|  | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] [default to 100]
 **name** | **String**|  | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] [default to 1]
 **type** | **String**|  | [optional] 

### Return type

[**PaginatedCreditorAccountList**](PaginatedCreditorAccountList.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## paymentsCreditorsRetrieve

> CreditorAccount paymentsCreditorsRetrieve(id)



API endpoints related to creditor accounts.

### Example

```javascript
import NordigenAccountInformationServicesApi from 'nordigen_account_information_services_api';
let defaultClient = NordigenAccountInformationServicesApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwtAuth
let jwtAuth = defaultClient.authentications['jwtAuth'];
jwtAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NordigenAccountInformationServicesApi.PaymentsApi();
let id = "id_example"; // String | 
apiInstance.paymentsCreditorsRetrieve(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**CreditorAccount**](CreditorAccount.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## paymentsSubmitCreate

> PaymentRead paymentsSubmitCreate(id, paymentReadRequest)



Initiate the payment on bank&#39;s side.  Complete the payment and return payment details as a response.

### Example

```javascript
import NordigenAccountInformationServicesApi from 'nordigen_account_information_services_api';
let defaultClient = NordigenAccountInformationServicesApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwtAuth
let jwtAuth = defaultClient.authentications['jwtAuth'];
jwtAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NordigenAccountInformationServicesApi.PaymentsApi();
let id = "id_example"; // String | 
let paymentReadRequest = new NordigenAccountInformationServicesApi.PaymentReadRequest(); // PaymentReadRequest | 
apiInstance.paymentsSubmitCreate(id, paymentReadRequest, (error, data, response) => {
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
 **id** | **String**|  | 
 **paymentReadRequest** | [**PaymentReadRequest**](PaymentReadRequest.md)|  | 

### Return type

[**PaymentRead**](PaymentRead.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json


## retrieveAllPaymentCreditorAccounts

> [CreditorAccount] retrieveAllPaymentCreditorAccounts()



Retrieve all payment creditor accounts

### Example

```javascript
import NordigenAccountInformationServicesApi from 'nordigen_account_information_services_api';
let defaultClient = NordigenAccountInformationServicesApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwtAuth
let jwtAuth = defaultClient.authentications['jwtAuth'];
jwtAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NordigenAccountInformationServicesApi.PaymentsApi();
apiInstance.retrieveAllPaymentCreditorAccounts((error, data, response) => {
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

[**[CreditorAccount]**](CreditorAccount.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrievePayment

> PaymentRead retrievePayment(id)



Retrieve payment

### Example

```javascript
import NordigenAccountInformationServicesApi from 'nordigen_account_information_services_api';
let defaultClient = NordigenAccountInformationServicesApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwtAuth
let jwtAuth = defaultClient.authentications['jwtAuth'];
jwtAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NordigenAccountInformationServicesApi.PaymentsApi();
let id = "id_example"; // String | 
apiInstance.retrievePayment(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**PaymentRead**](PaymentRead.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

