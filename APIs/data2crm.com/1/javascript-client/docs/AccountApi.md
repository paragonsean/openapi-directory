# Data2CrmApi.AccountApi

All URIs are relative to *https://api-2445581398133.apicast.io:443/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAccountEntity**](AccountApi.md#createAccountEntity) | **POST** /application/entity/account | POST for account
[**createAccountEntityBulk**](AccountApi.md#createAccountEntityBulk) | **POST** /application/entity/account/bulk | POST bulk  for account
[**deleteAccountCollectionBulk**](AccountApi.md#deleteAccountCollectionBulk) | **DELETE** /application/entity/account/bulk | DELETE bulk  for account
[**deleteAccountEntity**](AccountApi.md#deleteAccountEntity) | **DELETE** /application/entity/account/{account_id} | DELETE for account
[**getAccountAggregate**](AccountApi.md#getAccountAggregate) | **GET** /application/entity/account/aggregate | AGGREGATE for account
[**getAccountCollection**](AccountApi.md#getAccountCollection) | **GET** /application/entity/account/list | GET for account
[**getAccountCountCollection**](AccountApi.md#getAccountCountCollection) | **GET** /application/entity/account/count | COUNT for account
[**getAccountDescribe**](AccountApi.md#getAccountDescribe) | **GET** /application/entity/account/describe | DESCRIBE for account
[**getAccountEntity**](AccountApi.md#getAccountEntity) | **GET** /application/entity/account/{account_id} | GET for account
[**updateAccountEntity**](AccountApi.md#updateAccountEntity) | **PUT** /application/entity/account/{account_id} | PUT for account
[**updateAccountEntityBulk**](AccountApi.md#updateAccountEntityBulk) | **PUT** /application/entity/account/bulk | PUT bulk  for account



## createAccountEntity

> AccountEntityRelation createAccountEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, opts)

POST for account

Add account into the system

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.AccountApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let body = new Data2CrmApi.AccountEntity(); // AccountEntity | Add account into the system
let opts = {
  'xAPI2CRMNATIVEENABLE': "xAPI2CRMNATIVEENABLE_example", // String | Return native response
  'xAPI2CRMDESCRIBELIFETIME': "xAPI2CRMDESCRIBELIFETIME_example" // String | Describe lifetime
};
apiInstance.createAccountEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, opts, (error, data, response) => {
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
 **body** | [**AccountEntity**](AccountEntity.md)| Add account into the system | 
 **xAPI2CRMNATIVEENABLE** | **String**| Return native response | [optional] 
 **xAPI2CRMDESCRIBELIFETIME** | **String**| Describe lifetime | [optional] 

### Return type

[**AccountEntityRelation**](AccountEntityRelation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAccountEntityBulk

> BulkEntityRelation createAccountEntityBulk(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, opts)

POST bulk  for account

Add account into the system

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.AccountApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let body = new Data2CrmApi.BulkEntity(); // BulkEntity | Add account into the system
let opts = {
  'xAPI2CRMNATIVEENABLE': "xAPI2CRMNATIVEENABLE_example", // String | Return native response
  'xAPI2CRMDESCRIBELIFETIME': "xAPI2CRMDESCRIBELIFETIME_example" // String | Describe lifetime
};
apiInstance.createAccountEntityBulk(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, opts, (error, data, response) => {
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
 **body** | [**BulkEntity**](BulkEntity.md)| Add account into the system | 
 **xAPI2CRMNATIVEENABLE** | **String**| Return native response | [optional] 
 **xAPI2CRMDESCRIBELIFETIME** | **String**| Describe lifetime | [optional] 

### Return type

[**BulkEntityRelation**](BulkEntityRelation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAccountCollectionBulk

> BulkEntity deleteAccountCollectionBulk(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body)

DELETE bulk  for account

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.AccountApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let body = new Data2CrmApi.BulkEntity(); // BulkEntity | 
apiInstance.deleteAccountCollectionBulk(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, (error, data, response) => {
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


## deleteAccountEntity

> deleteAccountEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, accountId)

DELETE for account

Delete account information

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.AccountApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let accountId = "accountId_example"; // String | Account Identifier
apiInstance.deleteAccountEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, accountId, (error, data, response) => {
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
 **accountId** | **String**| Account Identifier | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAccountAggregate

> Aggregate getAccountAggregate(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts)

AGGREGATE for account

Returns aggregate for accounts

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.AccountApi();
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
apiInstance.getAccountAggregate(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts, (error, data, response) => {
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


## getAccountCollection

> [AccountEntity] getAccountCollection(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts)

GET for account

Returns all accounts from the system

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.AccountApi();
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
apiInstance.getAccountCollection(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts, (error, data, response) => {
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

[**[AccountEntity]**](AccountEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAccountCountCollection

> Count getAccountCountCollection(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts)

COUNT for account

Count all accounts from the system

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.AccountApi();
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
apiInstance.getAccountCountCollection(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts, (error, data, response) => {
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


## getAccountDescribe

> AccountDescribe getAccountDescribe(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts)

DESCRIBE for account

Returns describe for accounts

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.AccountApi();
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
apiInstance.getAccountDescribe(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts, (error, data, response) => {
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

[**AccountDescribe**](AccountDescribe.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAccountEntity

> AccountEntity getAccountEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, accountId, opts)

GET for account

Return account information

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.AccountApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let accountId = "accountId_example"; // String | Account Identifier
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
apiInstance.getAccountEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, accountId, opts, (error, data, response) => {
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
 **accountId** | **String**| Account Identifier | 
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

[**AccountEntity**](AccountEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateAccountEntity

> AccountEntityRelation updateAccountEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, accountId, body, opts)

PUT for account

Update account information

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.AccountApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let accountId = "accountId_example"; // String | Account Identifier
let body = new Data2CrmApi.AccountEntity(); // AccountEntity | Update account information
let opts = {
  'xAPI2CRMNATIVEENABLE': "xAPI2CRMNATIVEENABLE_example", // String | Return native response
  'xAPI2CRMDESCRIBELIFETIME': "xAPI2CRMDESCRIBELIFETIME_example" // String | Describe lifetime
};
apiInstance.updateAccountEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, accountId, body, opts, (error, data, response) => {
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
 **accountId** | **String**| Account Identifier | 
 **body** | [**AccountEntity**](AccountEntity.md)| Update account information | 
 **xAPI2CRMNATIVEENABLE** | **String**| Return native response | [optional] 
 **xAPI2CRMDESCRIBELIFETIME** | **String**| Describe lifetime | [optional] 

### Return type

[**AccountEntityRelation**](AccountEntityRelation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateAccountEntityBulk

> BulkEntityRelation updateAccountEntityBulk(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, opts)

PUT bulk  for account

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.AccountApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let body = new Data2CrmApi.BulkEntity(); // BulkEntity | 
let opts = {
  'xAPI2CRMNATIVEENABLE': "xAPI2CRMNATIVEENABLE_example", // String | Return native response
  'xAPI2CRMDESCRIBELIFETIME': "xAPI2CRMDESCRIBELIFETIME_example" // String | Describe lifetime
};
apiInstance.updateAccountEntityBulk(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, body, opts, (error, data, response) => {
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

