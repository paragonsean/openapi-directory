# BigRedCloudApi.PaymentsApi

All URIs are relative to *https://app.bigredcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**paymentsDelete**](PaymentsApi.md#paymentsDelete) | **DELETE** /v1/payments/{id} | Removes an existing Payment.
[**paymentsGet**](PaymentsApi.md#paymentsGet) | **GET** /v1/payments | Returns a list of company&#39;s Payments. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.
[**paymentsPost**](PaymentsApi.md#paymentsPost) | **POST** /v1/payments | Creates a new Payment.
[**paymentsProcessBatch**](PaymentsApi.md#paymentsProcessBatch) | **PUT** /v1/payments/batch | Processes a batch of Payments.
[**paymentsPut**](PaymentsApi.md#paymentsPut) | **PUT** /v1/payments/{id} | Updates an existing Payment.
[**v1PaymentsIdGet**](PaymentsApi.md#v1PaymentsIdGet) | **GET** /v1/payments/{id} | Returns information about a single Payments.



## paymentsDelete

> Object paymentsDelete(id, timestamp)

Removes an existing Payment.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.PaymentsApi();
let id = 789; // Number | Id of Payment to remove.
let timestamp = "timestamp_example"; // String | Timestamp of Payment to remove. Should be encoded in Base64.
apiInstance.paymentsDelete(id, timestamp, (error, data, response) => {
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
 **id** | **Number**| Id of Payment to remove. | 
 **timestamp** | **String**| Timestamp of Payment to remove. Should be encoded in Base64. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## paymentsGet

> PageResultPaymentQueryDto paymentsGet()

Returns a list of company&#39;s Payments. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.PaymentsApi();
apiInstance.paymentsGet((error, data, response) => {
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

[**PageResultPaymentQueryDto**](PageResultPaymentQueryDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## paymentsPost

> Object paymentsPost(paymentDto)

Creates a new Payment.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.PaymentsApi();
let paymentDto = new BigRedCloudApi.PaymentDto(); // PaymentDto | Information of Payment to create.
apiInstance.paymentsPost(paymentDto, (error, data, response) => {
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
 **paymentDto** | [**PaymentDto**](PaymentDto.md)| Information of Payment to create. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## paymentsProcessBatch

> Object paymentsProcessBatch(batchItemPaymentDto)

Processes a batch of Payments.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.PaymentsApi();
let batchItemPaymentDto = [new BigRedCloudApi.BatchItemPaymentDto()]; // [BatchItemPaymentDto] | Batch of Payments to process.
apiInstance.paymentsProcessBatch(batchItemPaymentDto, (error, data, response) => {
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
 **batchItemPaymentDto** | [**[BatchItemPaymentDto]**](BatchItemPaymentDto.md)| Batch of Payments to process. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## paymentsPut

> Object paymentsPut(id, paymentDto)

Updates an existing Payment.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.PaymentsApi();
let id = 789; // Number | Id of Payment to update.
let paymentDto = new BigRedCloudApi.PaymentDto(); // PaymentDto | Information of Payment to update.
apiInstance.paymentsPut(id, paymentDto, (error, data, response) => {
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
 **id** | **Number**| Id of Payment to update. | 
 **paymentDto** | [**PaymentDto**](PaymentDto.md)| Information of Payment to update. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## v1PaymentsIdGet

> PaymentDto v1PaymentsIdGet(id)

Returns information about a single Payments.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.PaymentsApi();
let id = 789; // Number | Id of Payment to return.
apiInstance.v1PaymentsIdGet(id, (error, data, response) => {
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
 **id** | **Number**| Id of Payment to return. | 

### Return type

[**PaymentDto**](PaymentDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

