# BigRedCloudApi.CustomersApi

All URIs are relative to *https://app.bigredcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customersDelete**](CustomersApi.md#customersDelete) | **DELETE** /v1/customers/{id} | Removes an existing Customer.
[**customersGet**](CustomersApi.md#customersGet) | **GET** /v1/customers | Returns a list of company&#39;s Customers. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; and \&quot;code\&quot; fields.
[**customersGetAccountTrans**](CustomersApi.md#customersGetAccountTrans) | **GET** /v1/customers/{itemId}/accountTrans | Returns a list of Customer&#39;s account transactions.
[**customersGetOpeningBalance**](CustomersApi.md#customersGetOpeningBalance) | **GET** /v1/customers/{itemId}/openingBalance | Returns a Customer&#39;s opening balances, calculated for the next periods: current month, one month old, two months old, three and more months old.
[**customersGetOpeningBalanceList**](CustomersApi.md#customersGetOpeningBalanceList) | **GET** /v1/customers/{itemId}/openingBalanceList | Returns a list of Customer&#39;s opening balance transactions.
[**customersGetQuotes**](CustomersApi.md#customersGetQuotes) | **GET** /v1/customers/{itemId}/quotes | Returns a list of Customer&#39;s quotes.
[**customersPost**](CustomersApi.md#customersPost) | **POST** /v1/customers | Creates a new Customer.
[**customersProcessBatch**](CustomersApi.md#customersProcessBatch) | **PUT** /v1/customers/batch | Processes a batch of Customers.
[**customersPut**](CustomersApi.md#customersPut) | **PUT** /v1/customers/{id} | Updates an existing Customer.
[**v1CustomersIdGet**](CustomersApi.md#v1CustomersIdGet) | **GET** /v1/customers/{id} | Returns information about a single Customer. You may specify that Customer&#39;s ledger balance should be calculated.



## customersDelete

> Object customersDelete(id, timestamp)

Removes an existing Customer.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.CustomersApi();
let id = 789; // Number | Id of Customer to remove.
let timestamp = "timestamp_example"; // String | Timestamp of Customer to remove. Should be encoded in Base64.
apiInstance.customersDelete(id, timestamp, (error, data, response) => {
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
 **id** | **Number**| Id of Customer to remove. | 
 **timestamp** | **String**| Timestamp of Customer to remove. Should be encoded in Base64. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customersGet

> PageResultCustomerQueryDto customersGet()

Returns a list of company&#39;s Customers. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; and \&quot;code\&quot; fields.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.CustomersApi();
apiInstance.customersGet((error, data, response) => {
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

[**PageResultCustomerQueryDto**](PageResultCustomerQueryDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customersGetAccountTrans

> [AccountTranDto] customersGetAccountTrans(itemId)

Returns a list of Customer&#39;s account transactions.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.CustomersApi();
let itemId = 789; // Number | Id of Customer to return account transaction.
apiInstance.customersGetAccountTrans(itemId, (error, data, response) => {
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
 **itemId** | **Number**| Id of Customer to return account transaction. | 

### Return type

[**[AccountTranDto]**](AccountTranDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customersGetOpeningBalance

> OwnerOpeningBalanceInPeriodsDto customersGetOpeningBalance(itemId)

Returns a Customer&#39;s opening balances, calculated for the next periods: current month, one month old, two months old, three and more months old.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.CustomersApi();
let itemId = 789; // Number | Id of Customer to return opening balances.
apiInstance.customersGetOpeningBalance(itemId, (error, data, response) => {
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
 **itemId** | **Number**| Id of Customer to return opening balances. | 

### Return type

[**OwnerOpeningBalanceInPeriodsDto**](OwnerOpeningBalanceInPeriodsDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customersGetOpeningBalanceList

> [OwnerOpeningBalanceDto] customersGetOpeningBalanceList(itemId)

Returns a list of Customer&#39;s opening balance transactions.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.CustomersApi();
let itemId = 789; // Number | Id of Customer to return opening balances transaction.
apiInstance.customersGetOpeningBalanceList(itemId, (error, data, response) => {
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
 **itemId** | **Number**| Id of Customer to return opening balances transaction. | 

### Return type

[**[OwnerOpeningBalanceDto]**](OwnerOpeningBalanceDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customersGetQuotes

> [QuoteDto] customersGetQuotes(itemId)

Returns a list of Customer&#39;s quotes.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.CustomersApi();
let itemId = 789; // Number | Id of Customer to return quotes.
apiInstance.customersGetQuotes(itemId, (error, data, response) => {
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
 **itemId** | **Number**| Id of Customer to return quotes. | 

### Return type

[**[QuoteDto]**](QuoteDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customersPost

> Object customersPost(customerDto)

Creates a new Customer.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.CustomersApi();
let customerDto = new BigRedCloudApi.CustomerDto(); // CustomerDto | Information of Customer to create.
apiInstance.customersPost(customerDto, (error, data, response) => {
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
 **customerDto** | [**CustomerDto**](CustomerDto.md)| Information of Customer to create. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## customersProcessBatch

> Object customersProcessBatch(batchItemCustomerDto)

Processes a batch of Customers.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.CustomersApi();
let batchItemCustomerDto = [new BigRedCloudApi.BatchItemCustomerDto()]; // [BatchItemCustomerDto] | Batch of Customers to process.
apiInstance.customersProcessBatch(batchItemCustomerDto, (error, data, response) => {
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
 **batchItemCustomerDto** | [**[BatchItemCustomerDto]**](BatchItemCustomerDto.md)| Batch of Customers to process. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## customersPut

> Object customersPut(id, customerDto)

Updates an existing Customer.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.CustomersApi();
let id = 789; // Number | Id of Customer to update.
let customerDto = new BigRedCloudApi.CustomerDto(); // CustomerDto | Information of Customer to update.
apiInstance.customersPut(id, customerDto, (error, data, response) => {
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
 **id** | **Number**| Id of Customer to update. | 
 **customerDto** | [**CustomerDto**](CustomerDto.md)| Information of Customer to update. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## v1CustomersIdGet

> CustomerDto v1CustomersIdGet(id, opts)

Returns information about a single Customer. You may specify that Customer&#39;s ledger balance should be calculated.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.CustomersApi();
let id = 789; // Number | Id of Customer to return.
let opts = {
  'needBalance': true // Boolean | If \"true\" then Customer's ledger balance will be calculated; otherwise balance will be returned as 0.
};
apiInstance.v1CustomersIdGet(id, opts, (error, data, response) => {
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
 **id** | **Number**| Id of Customer to return. | 
 **needBalance** | **Boolean**| If \&quot;true\&quot; then Customer&#39;s ledger balance will be calculated; otherwise balance will be returned as 0. | [optional] 

### Return type

[**CustomerDto**](CustomerDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

