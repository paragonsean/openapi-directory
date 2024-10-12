# Data2CrmApi.InvoiceApi

All URIs are relative to *https://api-2445581398133.apicast.io:443/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createInvoiceEntity**](InvoiceApi.md#createInvoiceEntity) | **POST** /application/entity/invoice | POST for invoice
[**createInvoiceEntityBulk**](InvoiceApi.md#createInvoiceEntityBulk) | **POST** /application/entity/invoice/bulk | POST bulk  for invoice
[**deleteInvoiceCollectionBulk**](InvoiceApi.md#deleteInvoiceCollectionBulk) | **DELETE** /application/entity/invoice/bulk | DELETE bulk  for invoice
[**deleteInvoiceEntity**](InvoiceApi.md#deleteInvoiceEntity) | **DELETE** /application/entity/invoice/{invoice_id} | DELETE for invoice
[**getInvoiceAggregate**](InvoiceApi.md#getInvoiceAggregate) | **GET** /application/entity/invoice/aggregate | AGGREGATE for invoice
[**getInvoiceCollection**](InvoiceApi.md#getInvoiceCollection) | **GET** /application/entity/invoice/list | GET for invoice
[**getInvoiceCountCollection**](InvoiceApi.md#getInvoiceCountCollection) | **GET** /application/entity/invoice/count | COUNT for invoice
[**getInvoiceDescribe**](InvoiceApi.md#getInvoiceDescribe) | **GET** /application/entity/invoice/describe | DESCRIBE for invoice
[**getInvoiceEntity**](InvoiceApi.md#getInvoiceEntity) | **GET** /application/entity/invoice/{invoice_id} | GET for invoice
[**updateInvoiceEntity**](InvoiceApi.md#updateInvoiceEntity) | **PUT** /application/entity/invoice/{invoice_id} | PUT for invoice
[**updateInvoiceEntityBulk**](InvoiceApi.md#updateInvoiceEntityBulk) | **PUT** /application/entity/invoice/bulk | PUT bulk  for invoice



## createInvoiceEntity

> InvoiceEntityRelation createInvoiceEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, opts)

POST for invoice

Add invoice into the system

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.InvoiceApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let body = new Data2CrmApi.InvoiceEntity(); // InvoiceEntity | Add invoice into the system
let opts = {
  'xAPI2CRMNATIVEENABLE': "xAPI2CRMNATIVEENABLE_example", // String | Return native response
  'xAPI2CRMDESCRIBELIFETIME': "xAPI2CRMDESCRIBELIFETIME_example" // String | Describe lifetime
};
apiInstance.createInvoiceEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, opts, (error, data, response) => {
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
 **xAPI2CRMUSERKEY** | **String**| User Key | [default to &#39;e2a6379ab878ae7e58119d4ec842bf9c&#39;]
 **xAPI2CRMAPPLICATIONKEY** | **String**| Application Key | [default to &#39;7ae5b17008fb414d84981191cf3b66a476ef8bef&#39;]
 **body** | [**InvoiceEntity**](InvoiceEntity.md)| Add invoice into the system | 
 **xAPI2CRMNATIVEENABLE** | **String**| Return native response | [optional] 
 **xAPI2CRMDESCRIBELIFETIME** | **String**| Describe lifetime | [optional] 

### Return type

[**InvoiceEntityRelation**](InvoiceEntityRelation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createInvoiceEntityBulk

> BulkEntityRelation createInvoiceEntityBulk(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, opts)

POST bulk  for invoice

Add invoice into the system

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.InvoiceApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let body = new Data2CrmApi.BulkEntity(); // BulkEntity | Add invoice into the system
let opts = {
  'xAPI2CRMNATIVEENABLE': "xAPI2CRMNATIVEENABLE_example", // String | Return native response
  'xAPI2CRMDESCRIBELIFETIME': "xAPI2CRMDESCRIBELIFETIME_example" // String | Describe lifetime
};
apiInstance.createInvoiceEntityBulk(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, opts, (error, data, response) => {
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
 **xAPI2CRMUSERKEY** | **String**| User Key | [default to &#39;e2a6379ab878ae7e58119d4ec842bf9c&#39;]
 **xAPI2CRMAPPLICATIONKEY** | **String**| Application Key | [default to &#39;7ae5b17008fb414d84981191cf3b66a476ef8bef&#39;]
 **body** | [**BulkEntity**](BulkEntity.md)| Add invoice into the system | 
 **xAPI2CRMNATIVEENABLE** | **String**| Return native response | [optional] 
 **xAPI2CRMDESCRIBELIFETIME** | **String**| Describe lifetime | [optional] 

### Return type

[**BulkEntityRelation**](BulkEntityRelation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteInvoiceCollectionBulk

> BulkEntity deleteInvoiceCollectionBulk(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body)

DELETE bulk  for invoice

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.InvoiceApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let body = new Data2CrmApi.BulkEntity(); // BulkEntity | 
apiInstance.deleteInvoiceCollectionBulk(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, (error, data, response) => {
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
 **xAPI2CRMUSERKEY** | **String**| User Key | [default to &#39;e2a6379ab878ae7e58119d4ec842bf9c&#39;]
 **xAPI2CRMAPPLICATIONKEY** | **String**| Application Key | [default to &#39;7ae5b17008fb414d84981191cf3b66a476ef8bef&#39;]
 **body** | [**BulkEntity**](BulkEntity.md)|  | 

### Return type

[**BulkEntity**](BulkEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteInvoiceEntity

> deleteInvoiceEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, invoiceId)

DELETE for invoice

Delete invoice information

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.InvoiceApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let invoiceId = "invoiceId_example"; // String | Invoice Identifier
apiInstance.deleteInvoiceEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, invoiceId, (error, data, response) => {
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
 **xAPI2CRMUSERKEY** | **String**| User Key | [default to &#39;e2a6379ab878ae7e58119d4ec842bf9c&#39;]
 **xAPI2CRMAPPLICATIONKEY** | **String**| Application Key | [default to &#39;7ae5b17008fb414d84981191cf3b66a476ef8bef&#39;]
 **invoiceId** | **String**| Invoice Identifier | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getInvoiceAggregate

> Aggregate getInvoiceAggregate(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts)

AGGREGATE for invoice

Returns aggregate for invoices

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.InvoiceApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let opts = {
  'xAPI2CRMNATIVEENABLE': "xAPI2CRMNATIVEENABLE_example", // String | Return native response
  'xAPI2CRMDATAENABLE': "xAPI2CRMDATAENABLE_example", // String | Data Enable
  'xAPI2CRMDATABUILD': "xAPI2CRMDATABUILD_example", // String | Data Build
  'xAPI2CRMDATAISFINAL': "xAPI2CRMDATAISFINAL_example", // String | Data Is Final
  'xAPI2CRMDATASTRATEGY': "xAPI2CRMDATASTRATEGY_example", // String | Data Strategy
  'xAPI2CRMDATACOHERENTENTITIES': "xAPI2CRMDATACOHERENTENTITIES_example", // String | Coherent Entities
  'xAPI2CRMDATAALWAYSACTUAL': "xAPI2CRMDATAALWAYSACTUAL_example", // String | Data Is Actual
  'xAPI2CRMDATAACTUALAT': new Date("2013-10-20T19:20:30+01:00"), // Date | Data Actual At
  'xAPI2CRMDESCRIBELIFETIME': "xAPI2CRMDESCRIBELIFETIME_example", // String | Describe lifetime
  'filter': "filter_example", // String | Filter
  'pipeline': "pipeline_example" // String | Pipeline
};
apiInstance.getInvoiceAggregate(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts, (error, data, response) => {
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
 **xAPI2CRMUSERKEY** | **String**| User Key | [default to &#39;e2a6379ab878ae7e58119d4ec842bf9c&#39;]
 **xAPI2CRMAPPLICATIONKEY** | **String**| Application Key | [default to &#39;7ae5b17008fb414d84981191cf3b66a476ef8bef&#39;]
 **xAPI2CRMNATIVEENABLE** | **String**| Return native response | [optional] 
 **xAPI2CRMDATAENABLE** | **String**| Data Enable | [optional] 
 **xAPI2CRMDATABUILD** | **String**| Data Build | [optional] 
 **xAPI2CRMDATAISFINAL** | **String**| Data Is Final | [optional] 
 **xAPI2CRMDATASTRATEGY** | **String**| Data Strategy | [optional] 
 **xAPI2CRMDATACOHERENTENTITIES** | **String**| Coherent Entities | [optional] 
 **xAPI2CRMDATAALWAYSACTUAL** | **String**| Data Is Actual | [optional] 
 **xAPI2CRMDATAACTUALAT** | **Date**| Data Actual At | [optional] 
 **xAPI2CRMDESCRIBELIFETIME** | **String**| Describe lifetime | [optional] 
 **filter** | **String**| Filter | [optional] 
 **pipeline** | **String**| Pipeline | [optional] 

### Return type

[**Aggregate**](Aggregate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInvoiceCollection

> [InvoiceEntity] getInvoiceCollection(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts)

GET for invoice

Returns all invoices from the system

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.InvoiceApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let opts = {
  'xAPI2CRMNATIVEENABLE': "xAPI2CRMNATIVEENABLE_example", // String | Return native response
  'xAPI2CRMDATAENABLE': "xAPI2CRMDATAENABLE_example", // String | Data Enable
  'xAPI2CRMDATABUILD': "xAPI2CRMDATABUILD_example", // String | Data Build
  'xAPI2CRMDATAISFINAL': "xAPI2CRMDATAISFINAL_example", // String | Data Is Final
  'xAPI2CRMDATASTRATEGY': "xAPI2CRMDATASTRATEGY_example", // String | Data Strategy
  'xAPI2CRMDATACOHERENTENTITIES': "xAPI2CRMDATACOHERENTENTITIES_example", // String | Coherent Entities
  'xAPI2CRMDATAALWAYSACTUAL': "xAPI2CRMDATAALWAYSACTUAL_example", // String | Data Is Actual
  'xAPI2CRMDATAACTUALAT': new Date("2013-10-20T19:20:30+01:00"), // Date | Data Actual At
  'xAPI2CRMDESCRIBELIFETIME': "xAPI2CRMDESCRIBELIFETIME_example", // String | Describe lifetime
  'pageSize': 56, // Number | Amount of results (default: 25)
  'page': 56, // Number | Page to show (default: 1)
  'filter': "filter_example", // String | Filter
  'expand': "expand_example", // String | Expand relations
  'fields': "fields_example", // String | Comma-separated list of fields to include in the response
  'sort': "sort_example", // String | Specifies ascending or descending sort on existing fields
  'unique': "unique_example" // String | Find all unique values for selected field
};
apiInstance.getInvoiceCollection(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts, (error, data, response) => {
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
 **xAPI2CRMUSERKEY** | **String**| User Key | [default to &#39;e2a6379ab878ae7e58119d4ec842bf9c&#39;]
 **xAPI2CRMAPPLICATIONKEY** | **String**| Application Key | [default to &#39;7ae5b17008fb414d84981191cf3b66a476ef8bef&#39;]
 **xAPI2CRMNATIVEENABLE** | **String**| Return native response | [optional] 
 **xAPI2CRMDATAENABLE** | **String**| Data Enable | [optional] 
 **xAPI2CRMDATABUILD** | **String**| Data Build | [optional] 
 **xAPI2CRMDATAISFINAL** | **String**| Data Is Final | [optional] 
 **xAPI2CRMDATASTRATEGY** | **String**| Data Strategy | [optional] 
 **xAPI2CRMDATACOHERENTENTITIES** | **String**| Coherent Entities | [optional] 
 **xAPI2CRMDATAALWAYSACTUAL** | **String**| Data Is Actual | [optional] 
 **xAPI2CRMDATAACTUALAT** | **Date**| Data Actual At | [optional] 
 **xAPI2CRMDESCRIBELIFETIME** | **String**| Describe lifetime | [optional] 
 **pageSize** | **Number**| Amount of results (default: 25) | [optional] 
 **page** | **Number**| Page to show (default: 1) | [optional] 
 **filter** | **String**| Filter | [optional] 
 **expand** | **String**| Expand relations | [optional] 
 **fields** | **String**| Comma-separated list of fields to include in the response | [optional] 
 **sort** | **String**| Specifies ascending or descending sort on existing fields | [optional] 
 **unique** | **String**| Find all unique values for selected field | [optional] 

### Return type

[**[InvoiceEntity]**](InvoiceEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInvoiceCountCollection

> Count getInvoiceCountCollection(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts)

COUNT for invoice

Count all invoices from the system

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.InvoiceApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let opts = {
  'xAPI2CRMDATAENABLE': "xAPI2CRMDATAENABLE_example", // String | Data Enable
  'xAPI2CRMDATABUILD': "xAPI2CRMDATABUILD_example", // String | Data Build
  'xAPI2CRMDATAISFINAL': "xAPI2CRMDATAISFINAL_example", // String | Data Is Final
  'xAPI2CRMDATASTRATEGY': "xAPI2CRMDATASTRATEGY_example", // String | Data Strategy
  'xAPI2CRMDATACOHERENTENTITIES': "xAPI2CRMDATACOHERENTENTITIES_example", // String | Coherent Entities
  'xAPI2CRMDATAALWAYSACTUAL': "xAPI2CRMDATAALWAYSACTUAL_example", // String | Data Is Actual
  'xAPI2CRMDATAACTUALAT': new Date("2013-10-20T19:20:30+01:00"), // Date | Data Actual At
  'filter': "filter_example" // String | Filter
};
apiInstance.getInvoiceCountCollection(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts, (error, data, response) => {
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
 **xAPI2CRMUSERKEY** | **String**| User Key | [default to &#39;e2a6379ab878ae7e58119d4ec842bf9c&#39;]
 **xAPI2CRMAPPLICATIONKEY** | **String**| Application Key | [default to &#39;7ae5b17008fb414d84981191cf3b66a476ef8bef&#39;]
 **xAPI2CRMDATAENABLE** | **String**| Data Enable | [optional] 
 **xAPI2CRMDATABUILD** | **String**| Data Build | [optional] 
 **xAPI2CRMDATAISFINAL** | **String**| Data Is Final | [optional] 
 **xAPI2CRMDATASTRATEGY** | **String**| Data Strategy | [optional] 
 **xAPI2CRMDATACOHERENTENTITIES** | **String**| Coherent Entities | [optional] 
 **xAPI2CRMDATAALWAYSACTUAL** | **String**| Data Is Actual | [optional] 
 **xAPI2CRMDATAACTUALAT** | **Date**| Data Actual At | [optional] 
 **filter** | **String**| Filter | [optional] 

### Return type

[**Count**](Count.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInvoiceDescribe

> InvoiceDescribe getInvoiceDescribe(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts)

DESCRIBE for invoice

Returns describe for invoices

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.InvoiceApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let opts = {
  'xAPI2CRMDATAENABLE': "xAPI2CRMDATAENABLE_example", // String | Data Enable
  'xAPI2CRMDATABUILD': "xAPI2CRMDATABUILD_example", // String | Data Build
  'xAPI2CRMDATAISFINAL': "xAPI2CRMDATAISFINAL_example", // String | Data Is Final
  'xAPI2CRMDATASTRATEGY': "xAPI2CRMDATASTRATEGY_example", // String | Data Strategy
  'xAPI2CRMDATACOHERENTENTITIES': "xAPI2CRMDATACOHERENTENTITIES_example", // String | Coherent Entities
  'xAPI2CRMDATAALWAYSACTUAL': "xAPI2CRMDATAALWAYSACTUAL_example", // String | Data Is Actual
  'xAPI2CRMDATAACTUALAT': new Date("2013-10-20T19:20:30+01:00"), // Date | Data Actual At
  'xAPI2CRMDESCRIBELIFETIME': "xAPI2CRMDESCRIBELIFETIME_example" // String | Describe lifetime
};
apiInstance.getInvoiceDescribe(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts, (error, data, response) => {
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
 **xAPI2CRMUSERKEY** | **String**| User Key | [default to &#39;e2a6379ab878ae7e58119d4ec842bf9c&#39;]
 **xAPI2CRMAPPLICATIONKEY** | **String**| Application Key | [default to &#39;7ae5b17008fb414d84981191cf3b66a476ef8bef&#39;]
 **xAPI2CRMDATAENABLE** | **String**| Data Enable | [optional] 
 **xAPI2CRMDATABUILD** | **String**| Data Build | [optional] 
 **xAPI2CRMDATAISFINAL** | **String**| Data Is Final | [optional] 
 **xAPI2CRMDATASTRATEGY** | **String**| Data Strategy | [optional] 
 **xAPI2CRMDATACOHERENTENTITIES** | **String**| Coherent Entities | [optional] 
 **xAPI2CRMDATAALWAYSACTUAL** | **String**| Data Is Actual | [optional] 
 **xAPI2CRMDATAACTUALAT** | **Date**| Data Actual At | [optional] 
 **xAPI2CRMDESCRIBELIFETIME** | **String**| Describe lifetime | [optional] 

### Return type

[**InvoiceDescribe**](InvoiceDescribe.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInvoiceEntity

> InvoiceEntity getInvoiceEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, invoiceId, opts)

GET for invoice

Return invoice information

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.InvoiceApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let invoiceId = "invoiceId_example"; // String | Invoice Identifier
let opts = {
  'xAPI2CRMNATIVEENABLE': "xAPI2CRMNATIVEENABLE_example", // String | Return native response
  'xAPI2CRMDATAENABLE': "xAPI2CRMDATAENABLE_example", // String | Data Enable
  'xAPI2CRMDATABUILD': "xAPI2CRMDATABUILD_example", // String | Data Build
  'xAPI2CRMDATAISFINAL': "xAPI2CRMDATAISFINAL_example", // String | Data Is Final
  'xAPI2CRMDATASTRATEGY': "xAPI2CRMDATASTRATEGY_example", // String | Data Strategy
  'xAPI2CRMDATACOHERENTENTITIES': "xAPI2CRMDATACOHERENTENTITIES_example", // String | Coherent Entities
  'xAPI2CRMDATAALWAYSACTUAL': "xAPI2CRMDATAALWAYSACTUAL_example", // String | Data Is Actual
  'xAPI2CRMDATAACTUALAT': new Date("2013-10-20T19:20:30+01:00"), // Date | Data Actual At
  'xAPI2CRMDESCRIBELIFETIME': "xAPI2CRMDESCRIBELIFETIME_example", // String | Describe lifetime
  'expand': "expand_example", // String | Expand relations
  'fields': "fields_example" // String | Comma-separated list of fields to include in the response
};
apiInstance.getInvoiceEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, invoiceId, opts, (error, data, response) => {
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
 **xAPI2CRMUSERKEY** | **String**| User Key | [default to &#39;e2a6379ab878ae7e58119d4ec842bf9c&#39;]
 **xAPI2CRMAPPLICATIONKEY** | **String**| Application Key | [default to &#39;7ae5b17008fb414d84981191cf3b66a476ef8bef&#39;]
 **invoiceId** | **String**| Invoice Identifier | 
 **xAPI2CRMNATIVEENABLE** | **String**| Return native response | [optional] 
 **xAPI2CRMDATAENABLE** | **String**| Data Enable | [optional] 
 **xAPI2CRMDATABUILD** | **String**| Data Build | [optional] 
 **xAPI2CRMDATAISFINAL** | **String**| Data Is Final | [optional] 
 **xAPI2CRMDATASTRATEGY** | **String**| Data Strategy | [optional] 
 **xAPI2CRMDATACOHERENTENTITIES** | **String**| Coherent Entities | [optional] 
 **xAPI2CRMDATAALWAYSACTUAL** | **String**| Data Is Actual | [optional] 
 **xAPI2CRMDATAACTUALAT** | **Date**| Data Actual At | [optional] 
 **xAPI2CRMDESCRIBELIFETIME** | **String**| Describe lifetime | [optional] 
 **expand** | **String**| Expand relations | [optional] 
 **fields** | **String**| Comma-separated list of fields to include in the response | [optional] 

### Return type

[**InvoiceEntity**](InvoiceEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateInvoiceEntity

> InvoiceEntityRelation updateInvoiceEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, invoiceId, body, opts)

PUT for invoice

Update invoice information

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.InvoiceApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let invoiceId = "invoiceId_example"; // String | Invoice Identifier
let body = new Data2CrmApi.InvoiceEntity(); // InvoiceEntity | Update invoice information
let opts = {
  'xAPI2CRMNATIVEENABLE': "xAPI2CRMNATIVEENABLE_example", // String | Return native response
  'xAPI2CRMDESCRIBELIFETIME': "xAPI2CRMDESCRIBELIFETIME_example" // String | Describe lifetime
};
apiInstance.updateInvoiceEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, invoiceId, body, opts, (error, data, response) => {
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
 **xAPI2CRMUSERKEY** | **String**| User Key | [default to &#39;e2a6379ab878ae7e58119d4ec842bf9c&#39;]
 **xAPI2CRMAPPLICATIONKEY** | **String**| Application Key | [default to &#39;7ae5b17008fb414d84981191cf3b66a476ef8bef&#39;]
 **invoiceId** | **String**| Invoice Identifier | 
 **body** | [**InvoiceEntity**](InvoiceEntity.md)| Update invoice information | 
 **xAPI2CRMNATIVEENABLE** | **String**| Return native response | [optional] 
 **xAPI2CRMDESCRIBELIFETIME** | **String**| Describe lifetime | [optional] 

### Return type

[**InvoiceEntityRelation**](InvoiceEntityRelation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateInvoiceEntityBulk

> BulkEntityRelation updateInvoiceEntityBulk(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, opts)

PUT bulk  for invoice

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.InvoiceApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let body = new Data2CrmApi.BulkEntity(); // BulkEntity | 
let opts = {
  'xAPI2CRMNATIVEENABLE': "xAPI2CRMNATIVEENABLE_example", // String | Return native response
  'xAPI2CRMDESCRIBELIFETIME': "xAPI2CRMDESCRIBELIFETIME_example" // String | Describe lifetime
};
apiInstance.updateInvoiceEntityBulk(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, opts, (error, data, response) => {
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
 **xAPI2CRMUSERKEY** | **String**| User Key | [default to &#39;e2a6379ab878ae7e58119d4ec842bf9c&#39;]
 **xAPI2CRMAPPLICATIONKEY** | **String**| Application Key | [default to &#39;7ae5b17008fb414d84981191cf3b66a476ef8bef&#39;]
 **body** | [**BulkEntity**](BulkEntity.md)|  | 
 **xAPI2CRMNATIVEENABLE** | **String**| Return native response | [optional] 
 **xAPI2CRMDESCRIBELIFETIME** | **String**| Describe lifetime | [optional] 

### Return type

[**BulkEntityRelation**](BulkEntityRelation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

