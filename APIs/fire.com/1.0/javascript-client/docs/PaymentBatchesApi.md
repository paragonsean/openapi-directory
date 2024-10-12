# FireFinancialServicesBusinessApi.PaymentBatchesApi

All URIs are relative to *https://api.fire.com/business*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addBankTransferBatchPayment**](PaymentBatchesApi.md#addBankTransferBatchPayment) | **POST** /v1/batches/{batchUuid}/banktransfers | Add a bank transfer payment to the batch.
[**addInternalTransferBatchPayment**](PaymentBatchesApi.md#addInternalTransferBatchPayment) | **POST** /v1/batches/{batchUuid}/internaltransfers | Add an internal transfer payment to the batch
[**addInternationalTransferBatchPayment**](PaymentBatchesApi.md#addInternationalTransferBatchPayment) | **POST** /v2/batches/{batchUuid}/internationaltransfers | Add an international transfer payment to the batch.
[**cancelBatchPayment**](PaymentBatchesApi.md#cancelBatchPayment) | **DELETE** /v1/batches/{batchUuid} | Cancel a batch
[**createBatchPayment**](PaymentBatchesApi.md#createBatchPayment) | **POST** /v1/batches | Create a new batch of payments
[**deleteBankTransferBatchPayment**](PaymentBatchesApi.md#deleteBankTransferBatchPayment) | **DELETE** /v1/batches/{batchUuid}/banktransfers/{itemUuid} | Remove a Payment from the Batch (Bank Transfers)
[**deleteInternalTransferBatchPayment**](PaymentBatchesApi.md#deleteInternalTransferBatchPayment) | **DELETE** /v1/batches/{batchUuid}/internaltransfers/{itemUuid} | Remove a Payment from the Batch (Internal Transfer)
[**deleteInternationalTransferBatchPayment**](PaymentBatchesApi.md#deleteInternationalTransferBatchPayment) | **DELETE** /v2/batches/{batchUuid}/internationaltransfers/{itemUuid} | Remove a Payment from the Batch (International Transfers)
[**getBatches**](PaymentBatchesApi.md#getBatches) | **GET** /v1/batches | List batches
[**getDetailsSingleBatch**](PaymentBatchesApi.md#getDetailsSingleBatch) | **GET** /v1/batches/{batchUuid} | Get details of a single Batch
[**getItemsBatchBankTransfer**](PaymentBatchesApi.md#getItemsBatchBankTransfer) | **GET** /v1/batches/{batchUuid}/banktransfers | List items in a Batch (Bank Transfers)
[**getItemsBatchInternalTrasnfer**](PaymentBatchesApi.md#getItemsBatchInternalTrasnfer) | **GET** /v1/batches/{batchUuid}/internaltransfers | List items in a Batch (Internal Transfers)
[**getItemsBatchInternationalTransfer**](PaymentBatchesApi.md#getItemsBatchInternationalTransfer) | **GET** /v2/batches/{batchUuid}/internationaltransfers | List items in a Batch (International Transfers)
[**getListofApproversForBatch**](PaymentBatchesApi.md#getListofApproversForBatch) | **GET** /v1/batches/{batchUuid}/approvals | List Approvers for a Batch
[**submitBatch**](PaymentBatchesApi.md#submitBatch) | **PUT** /v1/batches/{batchUuid} | Submit a batch for approval



## addBankTransferBatchPayment

> NewBatchItemResponse addBankTransferBatchPayment(batchUuid, addBankTransferBatchPaymentRequest)

Add a bank transfer payment to the batch.

There are two ways to process bank transfers - by Payee ID (**Mode 1**) or by Payee Account Details (**Mode 2**).  **Mode 1:** Use the payee IDs of existing approved payees set up against your account. These batches can be approved in the normal manner.  **Mode 2:** Use the account details of the payee. In the event that these details correspond to an existing approved payee, the batch can be approved as normal. If the account details are new, a batch of New Payees will automatically be created. This batch will need to be approved before the Payment batch can be approved. These payees will then exist as approved payees for future batches. 

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.PaymentBatchesApi();
let batchUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
let addBankTransferBatchPaymentRequest = new FireFinancialServicesBusinessApi.AddBankTransferBatchPaymentRequest(); // AddBankTransferBatchPaymentRequest | Details of **Mode 1** & **Mode 2**.
apiInstance.addBankTransferBatchPayment(batchUuid, addBankTransferBatchPaymentRequest, (error, data, response) => {
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
 **batchUuid** | **String**|  | 
 **addBankTransferBatchPaymentRequest** | [**AddBankTransferBatchPaymentRequest**](AddBankTransferBatchPaymentRequest.md)| Details of **Mode 1** &amp; **Mode 2**. | 

### Return type

[**NewBatchItemResponse**](NewBatchItemResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## addInternalTransferBatchPayment

> NewBatchItemResponse addInternalTransferBatchPayment(batchUuid, batchItemInternalTransfer)

Add an internal transfer payment to the batch

Simply specify the source account, destination account, amount and a reference.

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.PaymentBatchesApi();
let batchUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
let batchItemInternalTransfer = new FireFinancialServicesBusinessApi.BatchItemInternalTransfer(); // BatchItemInternalTransfer | Details of the source account, destination account, amount and a reference.
apiInstance.addInternalTransferBatchPayment(batchUuid, batchItemInternalTransfer, (error, data, response) => {
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
 **batchUuid** | **String**|  | 
 **batchItemInternalTransfer** | [**BatchItemInternalTransfer**](BatchItemInternalTransfer.md)| Details of the source account, destination account, amount and a reference. | 

### Return type

[**NewBatchItemResponse**](NewBatchItemResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## addInternationalTransferBatchPayment

> NewBatchItemResponse addInternationalTransferBatchPayment(batchUuid, batchItemInternationalTransferMode1)

Add an international transfer payment to the batch.

International transfers must be added to a batch using the Payee ID (**Mode 1**). Payees must be set up using the web application.  **Mode 1:** Use the payee IDs of existing approved payees set up against your account. These batches can be approved in the normal manner. 

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.PaymentBatchesApi();
let batchUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
let batchItemInternationalTransferMode1 = new FireFinancialServicesBusinessApi.BatchItemInternationalTransferMode1(); // BatchItemInternationalTransferMode1 | Details of **Mode 1**
apiInstance.addInternationalTransferBatchPayment(batchUuid, batchItemInternationalTransferMode1, (error, data, response) => {
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
 **batchUuid** | **String**|  | 
 **batchItemInternationalTransferMode1** | [**BatchItemInternationalTransferMode1**](BatchItemInternationalTransferMode1.md)| Details of **Mode 1** | 

### Return type

[**NewBatchItemResponse**](NewBatchItemResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cancelBatchPayment

> cancelBatchPayment(batchUuid)

Cancel a batch

Cancels the Batch. You can only cancel a batch before it is submitted for approval (while it is in the OPEN state).

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.PaymentBatchesApi();
let batchUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
apiInstance.cancelBatchPayment(batchUuid, (error, data, response) => {
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
 **batchUuid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## createBatchPayment

> NewBatchResponse createBatchPayment(newBatch)

Create a new batch of payments

The fire.com API allows businesses to automate payments between their accounts or to third parties across the UK and Europe.  For added security, the API can only set up the payments in batches. These batches must be approved by an authorised user via the firework mobile app.   The process is as follows:  **1.**Create a new batch  **2.**Add payments to the batch  **3.**Submit the batch for approval  Once the batch is submitted, the authorised users will receive notifications to their firework mobile apps. They can review the contents of the batch and then approve or reject it. If approved, the batch is then processed. You can avail of enhanced security by using Dual Authorisation to verify payments if you wish. Dual Authorisation can be enabled by you when setting up your API application in firework online.  **Batch Life Cycle Events**  A batch webhook can be specified to receive details of all the payments as they are processed. This webhook receives notifications for every event in the batch lifecycle.  The following events are triggered during a batch:  **batch.opened:** Contains the details of the batch opened. Checks that the callback URL exists - unless a HTTP 200 response is returned, the callback URL will not be configured.  **batch.item-added:** Details of the item added to the batch  **batch.item-removed:** Details of the item removed from the batch  **batch.cancelled:** Notifies that the batch was cancelled.  **batch.submitted:** Notifes that the batch was submitted  **batch.approved:** Notifies that the batch was approved.  **batch.rejected:** Notifies that the batch was rejected.  **batch.failed:** Notifies that the batch failed - includes the details of the failure (insufficient funds etc)  **batch.completed:** Notifies that the batch completed successfully. Includes a summary.  Push notifications are sent to the firework mobile app for many of these events too - these can be configured from within the app.  This is the first step in creating a batch payment. 

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.PaymentBatchesApi();
let newBatch = new FireFinancialServicesBusinessApi.NewBatch(); // NewBatch | Details of the batch payment
apiInstance.createBatchPayment(newBatch, (error, data, response) => {
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
 **newBatch** | [**NewBatch**](NewBatch.md)| Details of the batch payment | 

### Return type

[**NewBatchResponse**](NewBatchResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteBankTransferBatchPayment

> deleteBankTransferBatchPayment(batchUuid, itemUuid)

Remove a Payment from the Batch (Bank Transfers)

Removes a Payment from the Batch (Bank Transfers). You can only remove payments before the batch is submitted for approval (while it is in the OPEN state).

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.PaymentBatchesApi();
let batchUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
let itemUuid = "itemUuid_example"; // String | 
apiInstance.deleteBankTransferBatchPayment(batchUuid, itemUuid, (error, data, response) => {
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
 **batchUuid** | **String**|  | 
 **itemUuid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteInternalTransferBatchPayment

> deleteInternalTransferBatchPayment(batchUuid, itemUuid)

Remove a Payment from the Batch (Internal Transfer)

Removes a Payment from the Batch (Internal Transfer). You can only remove payments before the batch is submitted for approval (while it is in the OPEN state).

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.PaymentBatchesApi();
let batchUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
let itemUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
apiInstance.deleteInternalTransferBatchPayment(batchUuid, itemUuid, (error, data, response) => {
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
 **batchUuid** | **String**|  | 
 **itemUuid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteInternationalTransferBatchPayment

> deleteInternationalTransferBatchPayment(batchUuid, itemUuid)

Remove a Payment from the Batch (International Transfers)

Removes a Payment from the Batch (International Transfers). You can only remove payments before the batch is submitted for approval (while it is in the OPEN state).

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.PaymentBatchesApi();
let batchUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
let itemUuid = "itemUuid_example"; // String | 
apiInstance.deleteInternationalTransferBatchPayment(batchUuid, itemUuid, (error, data, response) => {
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
 **batchUuid** | **String**|  | 
 **itemUuid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getBatches

> BatchItems getBatches(opts)

List batches

Returns the list of batch with the specified types and statuses. 

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.PaymentBatchesApi();
let opts = {
  'batchStatus': "SUBMITTED", // String | 
  'batchTypes': "INTERNAL_TRANSFER", // String | 
  'orderBy': "DATE", // String | 
  'order': "DESC" // String | 
};
apiInstance.getBatches(opts, (error, data, response) => {
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
 **batchStatus** | **String**|  | [optional] 
 **batchTypes** | **String**|  | [optional] 
 **orderBy** | **String**|  | [optional] 
 **order** | **String**|  | [optional] 

### Return type

[**BatchItems**](BatchItems.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDetailsSingleBatch

> Batch getDetailsSingleBatch(batchUuid)

Get details of a single Batch

Returns the details of the batch specified in the API endpoint - {batchUuid}.

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.PaymentBatchesApi();
let batchUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
apiInstance.getDetailsSingleBatch(batchUuid, (error, data, response) => {
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
 **batchUuid** | **String**|  | 

### Return type

[**Batch**](Batch.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getItemsBatchBankTransfer

> BatchItems getItemsBatchBankTransfer(batchUuid, opts)

List items in a Batch (Bank Transfers)

Returns a paginated list of items in the specified batch.

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.PaymentBatchesApi();
let batchUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
let opts = {
  'offset': 0, // Number | 
  'limit': 10 // Number | 
};
apiInstance.getItemsBatchBankTransfer(batchUuid, opts, (error, data, response) => {
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
 **batchUuid** | **String**|  | 
 **offset** | **Number**|  | [optional] 
 **limit** | **Number**|  | [optional] 

### Return type

[**BatchItems**](BatchItems.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getItemsBatchInternalTrasnfer

> BatchItems getItemsBatchInternalTrasnfer(batchUuid, opts)

List items in a Batch (Internal Transfers)

Returns a paginated list of items in the specified batch.

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.PaymentBatchesApi();
let batchUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
let opts = {
  'offset': 0, // Number | 
  'limit': 10 // Number | 
};
apiInstance.getItemsBatchInternalTrasnfer(batchUuid, opts, (error, data, response) => {
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
 **batchUuid** | **String**|  | 
 **offset** | **Number**|  | [optional] 
 **limit** | **Number**|  | [optional] 

### Return type

[**BatchItems**](BatchItems.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getItemsBatchInternationalTransfer

> BatchItems getItemsBatchInternationalTransfer(batchUuid, opts)

List items in a Batch (International Transfers)

Returns a paginated list of items in the specified batch.

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.PaymentBatchesApi();
let batchUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
let opts = {
  'offset': 0, // Number | 
  'limit': 10 // Number | 
};
apiInstance.getItemsBatchInternationalTransfer(batchUuid, opts, (error, data, response) => {
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
 **batchUuid** | **String**|  | 
 **offset** | **Number**|  | [optional] 
 **limit** | **Number**|  | [optional] 

### Return type

[**BatchItems**](BatchItems.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getListofApproversForBatch

> BatchApprovers getListofApproversForBatch(batchUuid)

List Approvers for a Batch

Returns a list of approvers for this batch.

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.PaymentBatchesApi();
let batchUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
apiInstance.getListofApproversForBatch(batchUuid, (error, data, response) => {
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
 **batchUuid** | **String**|  | 

### Return type

[**BatchApprovers**](BatchApprovers.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## submitBatch

> submitBatch(batchUuid)

Submit a batch for approval

Submits the Batch (for approval in the case of a **BANK_TRANSFER** or **INTERNATIONAL_TRANSFER**). If this is an **INTERNAL_TRANSFER** batch, the transfers are immediately queued for processing. If this is a **BANK_TRANSFER** or **INTERNATIONAL_TRANSFER** batch, this will trigger requests for approval to the firework mobile apps of authorised users. Once those users approve the batch, it is queued for processing.  You can only submit a batch while it is in the OPEN state. 

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.PaymentBatchesApi();
let batchUuid = "4ADFB67A-0F5B-4A9A-9D74-34437250045C"; // String | 
apiInstance.submitBatch(batchUuid, (error, data, response) => {
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
 **batchUuid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

