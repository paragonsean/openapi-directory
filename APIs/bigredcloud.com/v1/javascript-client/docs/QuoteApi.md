# BigRedCloudApi.QuoteApi

All URIs are relative to *https://app.bigredcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quoteClose**](QuoteApi.md#quoteClose) | **PUT** /v1/quotes/close/{id} | Close a Quote.
[**quoteDelete**](QuoteApi.md#quoteDelete) | **DELETE** /v1/quotes/{id} | Removes an existing Quote.
[**quoteGet**](QuoteApi.md#quoteGet) | **GET** /v1/quotes | Returns a list of company&#39;s Quotes.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot;.
[**quotePost**](QuoteApi.md#quotePost) | **POST** /v1/quotes | Creates a new Quote.
[**quotePostCreateQuoteWithGeneratingReference**](QuoteApi.md#quotePostCreateQuoteWithGeneratingReference) | **POST** /v1/quotes/createQuoteWithGeneratingReference | Creates a new Quote with auto generating reference.
[**quotePostGenerateSaleInvoice**](QuoteApi.md#quotePostGenerateSaleInvoice) | **POST** /v1/quotes/generateSaleInvoice | Generate a sale invoice from a Quote.  When sale invoice is empty, new sale invoice will be generated from Quote.
[**quoteProcessBatch**](QuoteApi.md#quoteProcessBatch) | **PUT** /v1/quotes/batch | Processes a batch of Quote.
[**quotePut**](QuoteApi.md#quotePut) | **PUT** /v1/quotes/{id} | Updates an existing Quote.
[**quoteReopen**](QuoteApi.md#quoteReopen) | **PUT** /v1/quotes/reopen/{id} | Reopen a Quote.
[**v1QuotesIdGet**](QuoteApi.md#v1QuotesIdGet) | **GET** /v1/quotes/{id} | Returns information about a single Quote.



## quoteClose

> Object quoteClose(id)

Close a Quote.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.QuoteApi();
let id = 789; // Number | Id of Quote to close
apiInstance.quoteClose(id, (error, data, response) => {
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
 **id** | **Number**| Id of Quote to close | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quoteDelete

> Object quoteDelete(id, timestamp)

Removes an existing Quote.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.QuoteApi();
let id = 789; // Number | Id of Quote to remove.
let timestamp = "timestamp_example"; // String | Timestamp of Quote to remove. Should be encoded in Base64.
apiInstance.quoteDelete(id, timestamp, (error, data, response) => {
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
 **id** | **Number**| Id of Quote to remove. | 
 **timestamp** | **String**| Timestamp of Quote to remove. Should be encoded in Base64. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quoteGet

> PageResultQuoteDto quoteGet()

Returns a list of company&#39;s Quotes.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot;.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.QuoteApi();
apiInstance.quoteGet((error, data, response) => {
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

[**PageResultQuoteDto**](PageResultQuoteDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quotePost

> Object quotePost(quoteDto)

Creates a new Quote.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.QuoteApi();
let quoteDto = new BigRedCloudApi.QuoteDto(); // QuoteDto | Information of Quote to create.
apiInstance.quotePost(quoteDto, (error, data, response) => {
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
 **quoteDto** | [**QuoteDto**](QuoteDto.md)| Information of Quote to create. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## quotePostCreateQuoteWithGeneratingReference

> Object quotePostCreateQuoteWithGeneratingReference(quoteDto)

Creates a new Quote with auto generating reference.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.QuoteApi();
let quoteDto = new BigRedCloudApi.QuoteDto(); // QuoteDto | Information of Quote to create.
apiInstance.quotePostCreateQuoteWithGeneratingReference(quoteDto, (error, data, response) => {
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
 **quoteDto** | [**QuoteDto**](QuoteDto.md)| Information of Quote to create. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## quotePostGenerateSaleInvoice

> Object quotePostGenerateSaleInvoice(quoteGeneratingInvoiceDto)

Generate a sale invoice from a Quote.  When sale invoice is empty, new sale invoice will be generated from Quote.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.QuoteApi();
let quoteGeneratingInvoiceDto = new BigRedCloudApi.QuoteGeneratingInvoiceDto(); // QuoteGeneratingInvoiceDto | Id of Quote to generate
apiInstance.quotePostGenerateSaleInvoice(quoteGeneratingInvoiceDto, (error, data, response) => {
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
 **quoteGeneratingInvoiceDto** | [**QuoteGeneratingInvoiceDto**](QuoteGeneratingInvoiceDto.md)| Id of Quote to generate | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## quoteProcessBatch

> Object quoteProcessBatch(batchItemQuoteDto)

Processes a batch of Quote.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.QuoteApi();
let batchItemQuoteDto = [new BigRedCloudApi.BatchItemQuoteDto()]; // [BatchItemQuoteDto] | Batch of Quote to process.
apiInstance.quoteProcessBatch(batchItemQuoteDto, (error, data, response) => {
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
 **batchItemQuoteDto** | [**[BatchItemQuoteDto]**](BatchItemQuoteDto.md)| Batch of Quote to process. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## quotePut

> Object quotePut(id, quoteDto)

Updates an existing Quote.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.QuoteApi();
let id = 789; // Number | Id of Quote to update.
let quoteDto = new BigRedCloudApi.QuoteDto(); // QuoteDto | Information of Quote to update.
apiInstance.quotePut(id, quoteDto, (error, data, response) => {
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
 **id** | **Number**| Id of Quote to update. | 
 **quoteDto** | [**QuoteDto**](QuoteDto.md)| Information of Quote to update. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## quoteReopen

> Object quoteReopen(id)

Reopen a Quote.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.QuoteApi();
let id = 789; // Number | Id of Quote to reopen
apiInstance.quoteReopen(id, (error, data, response) => {
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
 **id** | **Number**| Id of Quote to reopen | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v1QuotesIdGet

> QuoteDto v1QuotesIdGet(id)

Returns information about a single Quote.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.QuoteApi();
let id = 789; // Number | Id of Sale Rep to return.
apiInstance.v1QuotesIdGet(id, (error, data, response) => {
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
 **id** | **Number**| Id of Sale Rep to return. | 

### Return type

[**QuoteDto**](QuoteDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

