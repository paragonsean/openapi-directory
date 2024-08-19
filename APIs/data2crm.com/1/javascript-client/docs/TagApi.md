# Data2CrmApi.TagApi

All URIs are relative to *https://api-2445581398133.apicast.io:443/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTagEntity**](TagApi.md#createTagEntity) | **POST** /application/entity/tag | POST for tag
[**createTagEntityBulk**](TagApi.md#createTagEntityBulk) | **POST** /application/entity/tag/bulk | POST bulk  for tag
[**deleteTagCollectionBulk**](TagApi.md#deleteTagCollectionBulk) | **DELETE** /application/entity/tag/bulk | DELETE bulk  for tag
[**deleteTagEntity**](TagApi.md#deleteTagEntity) | **DELETE** /application/entity/tag/{tag_id} | DELETE for tag
[**getTagAggregate**](TagApi.md#getTagAggregate) | **GET** /application/entity/tag/aggregate | AGGREGATE for tag
[**getTagCollection**](TagApi.md#getTagCollection) | **GET** /application/entity/tag/list | GET for tag
[**getTagCountCollection**](TagApi.md#getTagCountCollection) | **GET** /application/entity/tag/count | COUNT for tag
[**getTagDescribe**](TagApi.md#getTagDescribe) | **GET** /application/entity/tag/describe | DESCRIBE for tag
[**getTagEntity**](TagApi.md#getTagEntity) | **GET** /application/entity/tag/{tag_id} | GET for tag
[**updateTagEntity**](TagApi.md#updateTagEntity) | **PUT** /application/entity/tag/{tag_id} | PUT for tag
[**updateTagEntityBulk**](TagApi.md#updateTagEntityBulk) | **PUT** /application/entity/tag/bulk | PUT bulk  for tag



## createTagEntity

> TagEntityRelation createTagEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, opts)

POST for tag

Add tag into the system

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.TagApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let body = new Data2CrmApi.TagEntity(); // TagEntity | Add tag into the system
let opts = {
  'xAPI2CRMNATIVEENABLE': "xAPI2CRMNATIVEENABLE_example", // String | Return native response
  'xAPI2CRMDESCRIBELIFETIME': "xAPI2CRMDESCRIBELIFETIME_example" // String | Describe lifetime
};
apiInstance.createTagEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, opts, (error, data, response) => {
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
 **body** | [**TagEntity**](TagEntity.md)| Add tag into the system | 
 **xAPI2CRMNATIVEENABLE** | **String**| Return native response | [optional] 
 **xAPI2CRMDESCRIBELIFETIME** | **String**| Describe lifetime | [optional] 

### Return type

[**TagEntityRelation**](TagEntityRelation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createTagEntityBulk

> BulkEntityRelation createTagEntityBulk(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, opts)

POST bulk  for tag

Add tag into the system

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.TagApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let body = new Data2CrmApi.BulkEntity(); // BulkEntity | Add tag into the system
let opts = {
  'xAPI2CRMNATIVEENABLE': "xAPI2CRMNATIVEENABLE_example", // String | Return native response
  'xAPI2CRMDESCRIBELIFETIME': "xAPI2CRMDESCRIBELIFETIME_example" // String | Describe lifetime
};
apiInstance.createTagEntityBulk(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, opts, (error, data, response) => {
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
 **body** | [**BulkEntity**](BulkEntity.md)| Add tag into the system | 
 **xAPI2CRMNATIVEENABLE** | **String**| Return native response | [optional] 
 **xAPI2CRMDESCRIBELIFETIME** | **String**| Describe lifetime | [optional] 

### Return type

[**BulkEntityRelation**](BulkEntityRelation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteTagCollectionBulk

> BulkEntity deleteTagCollectionBulk(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body)

DELETE bulk  for tag

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.TagApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let body = new Data2CrmApi.BulkEntity(); // BulkEntity | 
apiInstance.deleteTagCollectionBulk(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, (error, data, response) => {
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


## deleteTagEntity

> deleteTagEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, tagId)

DELETE for tag

Delete tag information

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.TagApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let tagId = "tagId_example"; // String | Tag Identifier
apiInstance.deleteTagEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, tagId, (error, data, response) => {
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
 **tagId** | **String**| Tag Identifier | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getTagAggregate

> Aggregate getTagAggregate(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts)

AGGREGATE for tag

Returns aggregate for tags

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.TagApi();
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
apiInstance.getTagAggregate(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts, (error, data, response) => {
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


## getTagCollection

> [TagEntity] getTagCollection(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts)

GET for tag

Returns all tags from the system

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.TagApi();
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
apiInstance.getTagCollection(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts, (error, data, response) => {
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

[**[TagEntity]**](TagEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTagCountCollection

> Count getTagCountCollection(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts)

COUNT for tag

Count all tags from the system

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.TagApi();
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
apiInstance.getTagCountCollection(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts, (error, data, response) => {
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


## getTagDescribe

> TagDescribe getTagDescribe(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts)

DESCRIBE for tag

Returns describe for tags

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.TagApi();
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
apiInstance.getTagDescribe(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts, (error, data, response) => {
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

[**TagDescribe**](TagDescribe.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTagEntity

> TagEntity getTagEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, tagId, opts)

GET for tag

Return tag information

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.TagApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let tagId = "tagId_example"; // String | Tag Identifier
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
apiInstance.getTagEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, tagId, opts, (error, data, response) => {
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
 **tagId** | **String**| Tag Identifier | 
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

[**TagEntity**](TagEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateTagEntity

> TagEntityRelation updateTagEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, tagId, body, opts)

PUT for tag

Update tag information

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.TagApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let tagId = "tagId_example"; // String | Tag Identifier
let body = new Data2CrmApi.TagEntity(); // TagEntity | Update tag information
let opts = {
  'xAPI2CRMNATIVEENABLE': "xAPI2CRMNATIVEENABLE_example", // String | Return native response
  'xAPI2CRMDESCRIBELIFETIME': "xAPI2CRMDESCRIBELIFETIME_example" // String | Describe lifetime
};
apiInstance.updateTagEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, tagId, body, opts, (error, data, response) => {
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
 **tagId** | **String**| Tag Identifier | 
 **body** | [**TagEntity**](TagEntity.md)| Update tag information | 
 **xAPI2CRMNATIVEENABLE** | **String**| Return native response | [optional] 
 **xAPI2CRMDESCRIBELIFETIME** | **String**| Describe lifetime | [optional] 

### Return type

[**TagEntityRelation**](TagEntityRelation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateTagEntityBulk

> BulkEntityRelation updateTagEntityBulk(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, opts)

PUT bulk  for tag

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.TagApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let body = new Data2CrmApi.BulkEntity(); // BulkEntity | 
let opts = {
  'xAPI2CRMNATIVEENABLE': "xAPI2CRMNATIVEENABLE_example", // String | Return native response
  'xAPI2CRMDESCRIBELIFETIME': "xAPI2CRMDESCRIBELIFETIME_example" // String | Describe lifetime
};
apiInstance.updateTagEntityBulk(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, opts, (error, data, response) => {
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

