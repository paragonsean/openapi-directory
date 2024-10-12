# Data2CrmApi.CaseApi

All URIs are relative to *https://api-2445581398133.apicast.io:443/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCaseEntity**](CaseApi.md#createCaseEntity) | **POST** /application/entity/case | POST for case
[**createCaseEntityBulk**](CaseApi.md#createCaseEntityBulk) | **POST** /application/entity/case/bulk | POST bulk  for case
[**deleteCaseCollectionBulk**](CaseApi.md#deleteCaseCollectionBulk) | **DELETE** /application/entity/case/bulk | DELETE bulk  for case
[**deleteCaseEntity**](CaseApi.md#deleteCaseEntity) | **DELETE** /application/entity/case/{case_id} | DELETE for case
[**getCaseAggregate**](CaseApi.md#getCaseAggregate) | **GET** /application/entity/case/aggregate | AGGREGATE for case
[**getCaseCollection**](CaseApi.md#getCaseCollection) | **GET** /application/entity/case/list | GET for case
[**getCaseCountCollection**](CaseApi.md#getCaseCountCollection) | **GET** /application/entity/case/count | COUNT for case
[**getCaseDescribe**](CaseApi.md#getCaseDescribe) | **GET** /application/entity/case/describe | DESCRIBE for case
[**getCaseEntity**](CaseApi.md#getCaseEntity) | **GET** /application/entity/case/{case_id} | GET for case
[**updateCaseEntity**](CaseApi.md#updateCaseEntity) | **PUT** /application/entity/case/{case_id} | PUT for case
[**updateCaseEntityBulk**](CaseApi.md#updateCaseEntityBulk) | **PUT** /application/entity/case/bulk | PUT bulk  for case



## createCaseEntity

> CasesEntityRelation createCaseEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, opts)

POST for case

Add case into the system

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.CaseApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let body = new Data2CrmApi.CasesEntity(); // CasesEntity | Add case into the system
let opts = {
  'xAPI2CRMNATIVEENABLE': "xAPI2CRMNATIVEENABLE_example", // String | Return native response
  'xAPI2CRMDESCRIBELIFETIME': "xAPI2CRMDESCRIBELIFETIME_example" // String | Describe lifetime
};
apiInstance.createCaseEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, opts, (error, data, response) => {
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
 **body** | [**CasesEntity**](CasesEntity.md)| Add case into the system | 
 **xAPI2CRMNATIVEENABLE** | **String**| Return native response | [optional] 
 **xAPI2CRMDESCRIBELIFETIME** | **String**| Describe lifetime | [optional] 

### Return type

[**CasesEntityRelation**](CasesEntityRelation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createCaseEntityBulk

> BulkEntityRelation createCaseEntityBulk(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, opts)

POST bulk  for case

Add case into the system

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.CaseApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let body = new Data2CrmApi.BulkEntity(); // BulkEntity | Add case into the system
let opts = {
  'xAPI2CRMNATIVEENABLE': "xAPI2CRMNATIVEENABLE_example", // String | Return native response
  'xAPI2CRMDESCRIBELIFETIME': "xAPI2CRMDESCRIBELIFETIME_example" // String | Describe lifetime
};
apiInstance.createCaseEntityBulk(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, opts, (error, data, response) => {
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
 **body** | [**BulkEntity**](BulkEntity.md)| Add case into the system | 
 **xAPI2CRMNATIVEENABLE** | **String**| Return native response | [optional] 
 **xAPI2CRMDESCRIBELIFETIME** | **String**| Describe lifetime | [optional] 

### Return type

[**BulkEntityRelation**](BulkEntityRelation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteCaseCollectionBulk

> BulkEntity deleteCaseCollectionBulk(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body)

DELETE bulk  for case

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.CaseApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let body = new Data2CrmApi.BulkEntity(); // BulkEntity | 
apiInstance.deleteCaseCollectionBulk(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, (error, data, response) => {
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


## deleteCaseEntity

> deleteCaseEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, caseId)

DELETE for case

Delete case information

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.CaseApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let caseId = "caseId_example"; // String | Case Identifier
apiInstance.deleteCaseEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, caseId, (error, data, response) => {
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
 **caseId** | **String**| Case Identifier | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getCaseAggregate

> Aggregate getCaseAggregate(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts)

AGGREGATE for case

Returns aggregate for cases

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.CaseApi();
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
apiInstance.getCaseAggregate(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts, (error, data, response) => {
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


## getCaseCollection

> [CasesEntity] getCaseCollection(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts)

GET for case

Returns all cases from the system

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.CaseApi();
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
apiInstance.getCaseCollection(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts, (error, data, response) => {
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

[**[CasesEntity]**](CasesEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCaseCountCollection

> Count getCaseCountCollection(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts)

COUNT for case

Count all cases from the system

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.CaseApi();
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
apiInstance.getCaseCountCollection(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts, (error, data, response) => {
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


## getCaseDescribe

> CaseDescribe getCaseDescribe(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts)

DESCRIBE for case

Returns describe for cases

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.CaseApi();
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
apiInstance.getCaseDescribe(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts, (error, data, response) => {
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

[**CaseDescribe**](CaseDescribe.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCaseEntity

> CasesEntity getCaseEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, caseId, opts)

GET for case

Return case information

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.CaseApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let caseId = "caseId_example"; // String | Case Identifier
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
apiInstance.getCaseEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, caseId, opts, (error, data, response) => {
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
 **caseId** | **String**| Case Identifier | 
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

[**CasesEntity**](CasesEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateCaseEntity

> CasesEntityRelation updateCaseEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, caseId, body, opts)

PUT for case

Update case information

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.CaseApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let caseId = "caseId_example"; // String | Case Identifier
let body = new Data2CrmApi.CasesEntity(); // CasesEntity | Update case information
let opts = {
  'xAPI2CRMNATIVEENABLE': "xAPI2CRMNATIVEENABLE_example", // String | Return native response
  'xAPI2CRMDESCRIBELIFETIME': "xAPI2CRMDESCRIBELIFETIME_example" // String | Describe lifetime
};
apiInstance.updateCaseEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, caseId, body, opts, (error, data, response) => {
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
 **caseId** | **String**| Case Identifier | 
 **body** | [**CasesEntity**](CasesEntity.md)| Update case information | 
 **xAPI2CRMNATIVEENABLE** | **String**| Return native response | [optional] 
 **xAPI2CRMDESCRIBELIFETIME** | **String**| Describe lifetime | [optional] 

### Return type

[**CasesEntityRelation**](CasesEntityRelation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateCaseEntityBulk

> BulkEntityRelation updateCaseEntityBulk(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, opts)

PUT bulk  for case

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.CaseApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let body = new Data2CrmApi.BulkEntity(); // BulkEntity | 
let opts = {
  'xAPI2CRMNATIVEENABLE': "xAPI2CRMNATIVEENABLE_example", // String | Return native response
  'xAPI2CRMDESCRIBELIFETIME': "xAPI2CRMDESCRIBELIFETIME_example" // String | Describe lifetime
};
apiInstance.updateCaseEntityBulk(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, opts, (error, data, response) => {
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

