# BulkWhoisApi.DefaultApi

All URIs are relative to *https://apispot.io/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkDomain**](DefaultApi.md#checkDomain) | **GET** /domains/{domain}/check | 
[**createBatch**](DefaultApi.md#createBatch) | **POST** /batch | 
[**deleteBatch**](DefaultApi.md#deleteBatch) | **DELETE** /batch/{id} | 
[**domainRank**](DefaultApi.md#domainRank) | **GET** /domains/{domain}/rank | 
[**getBatch**](DefaultApi.md#getBatch) | **GET** /batch/{id} | 
[**getBatches**](DefaultApi.md#getBatches) | **GET** /batch | 
[**queryDb**](DefaultApi.md#queryDb) | **GET** /db | 
[**whois**](DefaultApi.md#whois) | **GET** /domains/{domain}/whois | 



## checkDomain

> CheckDomain200Response checkDomain(domain)



Check domain availability

### Example

```javascript
import BulkWhoisApi from 'bulk_whois_api';
let defaultClient = BulkWhoisApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new BulkWhoisApi.DefaultApi();
let domain = "domain_example"; // String | Domain
apiInstance.checkDomain(domain, (error, data, response) => {
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
 **domain** | **String**| Domain | 

### Return type

[**CheckDomain200Response**](CheckDomain200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createBatch

> Batch createBatch(createBatchRequest)



Create batch. Batch is then being processed until all provided items have been completed. At any time it can be &#x60;get&#x60; to provide current status with results optionally.

### Example

```javascript
import BulkWhoisApi from 'bulk_whois_api';
let defaultClient = BulkWhoisApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new BulkWhoisApi.DefaultApi();
let createBatchRequest = new BulkWhoisApi.CreateBatchRequest(); // CreateBatchRequest | 
apiInstance.createBatch(createBatchRequest, (error, data, response) => {
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
 **createBatchRequest** | [**CreateBatchRequest**](CreateBatchRequest.md)|  | 

### Return type

[**Batch**](Batch.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteBatch

> deleteBatch(id)



Delete batch

### Example

```javascript
import BulkWhoisApi from 'bulk_whois_api';
let defaultClient = BulkWhoisApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new BulkWhoisApi.DefaultApi();
let id = "id_example"; // String | Batch ID
apiInstance.deleteBatch(id, (error, data, response) => {
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
 **id** | **String**| Batch ID | 

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## domainRank

> DomainRank200Response domainRank(domain)



Check domain rank (authority).

### Example

```javascript
import BulkWhoisApi from 'bulk_whois_api';
let defaultClient = BulkWhoisApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new BulkWhoisApi.DefaultApi();
let domain = "domain_example"; // String | Domain
apiInstance.domainRank(domain, (error, data, response) => {
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
 **domain** | **String**| Domain | 

### Return type

[**DomainRank200Response**](DomainRank200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBatch

> Batch getBatch(id)



Get batch

### Example

```javascript
import BulkWhoisApi from 'bulk_whois_api';
let defaultClient = BulkWhoisApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new BulkWhoisApi.DefaultApi();
let id = "id_example"; // String | Batch ID
apiInstance.getBatch(id, (error, data, response) => {
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
 **id** | **String**| Batch ID | 

### Return type

[**Batch**](Batch.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBatches

> ArrayOfBatch getBatches()



Get your batches

### Example

```javascript
import BulkWhoisApi from 'bulk_whois_api';
let defaultClient = BulkWhoisApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new BulkWhoisApi.DefaultApi();
apiInstance.getBatches((error, data, response) => {
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

[**ArrayOfBatch**](ArrayOfBatch.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryDb

> Object queryDb(query)



Query domain database

### Example

```javascript
import BulkWhoisApi from 'bulk_whois_api';
let defaultClient = BulkWhoisApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new BulkWhoisApi.DefaultApi();
let query = "query_example"; // String | Query (contact name, dns, domain etc)
apiInstance.queryDb(query, (error, data, response) => {
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
 **query** | **String**| Query (contact name, dns, domain etc) | 

### Return type

**Object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## whois

> whois(domain, opts)



WHOIS query for a domain

### Example

```javascript
import BulkWhoisApi from 'bulk_whois_api';
let defaultClient = BulkWhoisApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new BulkWhoisApi.DefaultApi();
let domain = "domain_example"; // String | Domain
let opts = {
  'format': "format_example" // String | 
};
apiInstance.whois(domain, opts, (error, data, response) => {
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
 **domain** | **String**| Domain | 
 **format** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

