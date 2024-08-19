# Data2CrmApi.InvoiceItemApi

All URIs are relative to *https://api-2445581398133.apicast.io:443/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createInvoiceItemEntity**](InvoiceItemApi.md#createInvoiceItemEntity) | **POST** /application/entity/invoiceItem | POST for invoiceItem
[**createInvoiceItemEntityBulk**](InvoiceItemApi.md#createInvoiceItemEntityBulk) | **POST** /application/entity/invoiceItem/bulk | POST bulk  for invoiceItem
[**deleteInvoiceItemCollectionBulk**](InvoiceItemApi.md#deleteInvoiceItemCollectionBulk) | **DELETE** /application/entity/invoiceItem/bulk | DELETE bulk  for invoiceItem
[**deleteInvoiceItemEntity**](InvoiceItemApi.md#deleteInvoiceItemEntity) | **DELETE** /application/entity/invoiceItem/{invoiceItem_id} | DELETE for invoiceItem
[**getInvoiceItemAggregate**](InvoiceItemApi.md#getInvoiceItemAggregate) | **GET** /application/entity/invoiceItem/aggregate | AGGREGATE for invoiceItem
[**getInvoiceItemCollection**](InvoiceItemApi.md#getInvoiceItemCollection) | **GET** /application/entity/invoiceItem/list | GET for invoiceItem
[**getInvoiceItemCountCollection**](InvoiceItemApi.md#getInvoiceItemCountCollection) | **GET** /application/entity/invoiceItem/count | COUNT for invoiceItem
[**getInvoiceItemDescribe**](InvoiceItemApi.md#getInvoiceItemDescribe) | **GET** /application/entity/invoiceItem/describe | DESCRIBE for invoiceItem
[**getInvoiceItemEntity**](InvoiceItemApi.md#getInvoiceItemEntity) | **GET** /application/entity/invoiceItem/{invoiceItem_id} | GET for invoiceItem
[**updateInvoiceItemEntity**](InvoiceItemApi.md#updateInvoiceItemEntity) | **PUT** /application/entity/invoiceItem/{invoiceItem_id} | PUT for invoiceItem
[**updateInvoiceItemEntityBulk**](InvoiceItemApi.md#updateInvoiceItemEntityBulk) | **PUT** /application/entity/invoiceItem/bulk | PUT bulk  for invoiceItem



## createInvoiceItemEntity

> InvoiceItemEntityRelation createInvoiceItemEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, opts)

POST for invoiceItem

Add invoiceItem into the system

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.InvoiceItemApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let body = new Data2CrmApi.InvoiceItemEntity(); // InvoiceItemEntity | Add invoiceItem into the system
let opts = {
  'xAPI2CRMNATIVEENABLE': "xAPI2CRMNATIVEENABLE_example", // String | Return native response
  'xAPI2CRMDESCRIBELIFETIME': "xAPI2CRMDESCRIBELIFETIME_example" // String | Describe lifetime
};
apiInstance.createInvoiceItemEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, opts, (error, data, response) => {
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
 **body** | [**InvoiceItemEntity**](InvoiceItemEntity.md)| Add invoiceItem into the system | 
 **xAPI2CRMNATIVEENABLE** | **String**| Return native response | [optional] 
 **xAPI2CRMDESCRIBELIFETIME** | **String**| Describe lifetime | [optional] 

### Return type

[**InvoiceItemEntityRelation**](InvoiceItemEntityRelation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createInvoiceItemEntityBulk

> BulkEntityRelation createInvoiceItemEntityBulk(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, opts)

POST bulk  for invoiceItem

Add invoiceItem into the system

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.InvoiceItemApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let body = new Data2CrmApi.BulkEntity(); // BulkEntity | Add invoiceItem into the system
let opts = {
  'xAPI2CRMNATIVEENABLE': "xAPI2CRMNATIVEENABLE_example", // String | Return native response
  'xAPI2CRMDESCRIBELIFETIME': "xAPI2CRMDESCRIBELIFETIME_example" // String | Describe lifetime
};
apiInstance.createInvoiceItemEntityBulk(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, opts, (error, data, response) => {
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
 **body** | [**BulkEntity**](BulkEntity.md)| Add invoiceItem into the system | 
 **xAPI2CRMNATIVEENABLE** | **String**| Return native response | [optional] 
 **xAPI2CRMDESCRIBELIFETIME** | **String**| Describe lifetime | [optional] 

### Return type

[**BulkEntityRelation**](BulkEntityRelation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteInvoiceItemCollectionBulk

> BulkEntity deleteInvoiceItemCollectionBulk(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body)

DELETE bulk  for invoiceItem

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.InvoiceItemApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let body = new Data2CrmApi.BulkEntity(); // BulkEntity | 
apiInstance.deleteInvoiceItemCollectionBulk(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, (error, data, response) => {
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


## deleteInvoiceItemEntity

> deleteInvoiceItemEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, invoiceItemId)

DELETE for invoiceItem

Delete invoiceItem information

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.InvoiceItemApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let invoiceItemId = "invoiceItemId_example"; // String | Invoice Item Identifier
apiInstance.deleteInvoiceItemEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, invoiceItemId, (error, data, response) => {
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
 **invoiceItemId** | **String**| Invoice Item Identifier | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getInvoiceItemAggregate

> Aggregate getInvoiceItemAggregate(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts)

AGGREGATE for invoiceItem

Returns aggregate for invoiceItems

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.InvoiceItemApi();
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
apiInstance.getInvoiceItemAggregate(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts, (error, data, response) => {
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


## getInvoiceItemCollection

> [InvoiceItemEntity] getInvoiceItemCollection(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts)

GET for invoiceItem

Returns all invoiceItems from the system

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.InvoiceItemApi();
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
apiInstance.getInvoiceItemCollection(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts, (error, data, response) => {
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

[**[InvoiceItemEntity]**](InvoiceItemEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInvoiceItemCountCollection

> Count getInvoiceItemCountCollection(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts)

COUNT for invoiceItem

Count all invoiceItems from the system

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.InvoiceItemApi();
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
apiInstance.getInvoiceItemCountCollection(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts, (error, data, response) => {
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


## getInvoiceItemDescribe

> InvoiceItemDescribe getInvoiceItemDescribe(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts)

DESCRIBE for invoiceItem

Returns describe for invoiceItems

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.InvoiceItemApi();
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
apiInstance.getInvoiceItemDescribe(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts, (error, data, response) => {
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

[**InvoiceItemDescribe**](InvoiceItemDescribe.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInvoiceItemEntity

> InvoiceItemEntity getInvoiceItemEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, invoiceItemId, opts)

GET for invoiceItem

Return invoiceItem information

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.InvoiceItemApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let invoiceItemId = "invoiceItemId_example"; // String | Invoice Item Identifier
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
apiInstance.getInvoiceItemEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, invoiceItemId, opts, (error, data, response) => {
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
 **invoiceItemId** | **String**| Invoice Item Identifier | 
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

[**InvoiceItemEntity**](InvoiceItemEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateInvoiceItemEntity

> InvoiceItemEntityRelation updateInvoiceItemEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, invoiceItemId, body, opts)

PUT for invoiceItem

Update invoiceItem information

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.InvoiceItemApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let invoiceItemId = "invoiceItemId_example"; // String | Invoice Item Identifier
let body = new Data2CrmApi.InvoiceItemEntity(); // InvoiceItemEntity | Update invoiceItem information
let opts = {
  'xAPI2CRMNATIVEENABLE': "xAPI2CRMNATIVEENABLE_example", // String | Return native response
  'xAPI2CRMDESCRIBELIFETIME': "xAPI2CRMDESCRIBELIFETIME_example" // String | Describe lifetime
};
apiInstance.updateInvoiceItemEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, invoiceItemId, body, opts, (error, data, response) => {
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
 **invoiceItemId** | **String**| Invoice Item Identifier | 
 **body** | [**InvoiceItemEntity**](InvoiceItemEntity.md)| Update invoiceItem information | 
 **xAPI2CRMNATIVEENABLE** | **String**| Return native response | [optional] 
 **xAPI2CRMDESCRIBELIFETIME** | **String**| Describe lifetime | [optional] 

### Return type

[**InvoiceItemEntityRelation**](InvoiceItemEntityRelation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateInvoiceItemEntityBulk

> BulkEntityRelation updateInvoiceItemEntityBulk(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, opts)

PUT bulk  for invoiceItem

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.InvoiceItemApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let body = new Data2CrmApi.BulkEntity(); // BulkEntity | 
let opts = {
  'xAPI2CRMNATIVEENABLE': "xAPI2CRMNATIVEENABLE_example", // String | Return native response
  'xAPI2CRMDESCRIBELIFETIME': "xAPI2CRMDESCRIBELIFETIME_example" // String | Describe lifetime
};
apiInstance.updateInvoiceItemEntityBulk(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, opts, (error, data, response) => {
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

