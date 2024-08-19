# Data2CrmApi.ApplicationApi

All URIs are relative to *https://api-2445581398133.apicast.io:443/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createApplicationEntity**](ApplicationApi.md#createApplicationEntity) | **POST** /application | POST for application
[**deleteApplicationEntity**](ApplicationApi.md#deleteApplicationEntity) | **DELETE** /application/{key} | DELETE for application
[**getApplicationCollection**](ApplicationApi.md#getApplicationCollection) | **GET** /application/list | GET for application
[**getApplicationCountCollection**](ApplicationApi.md#getApplicationCountCollection) | **GET** /application/count | COUNT for application
[**getApplicationEntity**](ApplicationApi.md#getApplicationEntity) | **GET** /application/{key} | GET for application
[**updateApplicationEntity**](ApplicationApi.md#updateApplicationEntity) | **PUT** /application/{key} | PUT for application



## createApplicationEntity

> ApplicationEntityRelation createApplicationEntity(xAPI2CRMUSERKEY, body)

POST for application

Add application into the system

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.ApplicationApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | API2CRM user key
let body = new Data2CrmApi.ApplicationEntityWrite(); // ApplicationEntityWrite | Add application into the system
apiInstance.createApplicationEntity(xAPI2CRMUSERKEY, body, (error, data, response) => {
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
 **xAPI2CRMUSERKEY** | **String**| API2CRM user key | [default to &#39;e2a6379ab878ae7e58119d4ec842bf9c&#39;]
 **body** | [**ApplicationEntityWrite**](ApplicationEntityWrite.md)| Add application into the system | 

### Return type

[**ApplicationEntityRelation**](ApplicationEntityRelation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteApplicationEntity

> deleteApplicationEntity(xAPI2CRMUSERKEY, key)

DELETE for application

Delete application information

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.ApplicationApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | API2CRM user key
let key = "key_example"; // String | Application key
apiInstance.deleteApplicationEntity(xAPI2CRMUSERKEY, key, (error, data, response) => {
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
 **xAPI2CRMUSERKEY** | **String**| API2CRM user key | [default to &#39;e2a6379ab878ae7e58119d4ec842bf9c&#39;]
 **key** | **String**| Application key | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getApplicationCollection

> [ApplicationEntityList] getApplicationCollection(xAPI2CRMUSERKEY, opts)

GET for application

Returns all applications from the system

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.ApplicationApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | API2CRM user key
let opts = {
  'pageSize': 56, // Number | Amount of results (default: 25)
  'page': 56, // Number | Page to show (default: 1)
  'filter': "filter_example", // String | Filter
  'fields': "fields_example", // String | Comma-separated list of fields to include in the response
  'sort': "sort_example" // String | Specifies ascending or descending sort on existing fields
};
apiInstance.getApplicationCollection(xAPI2CRMUSERKEY, opts, (error, data, response) => {
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
 **xAPI2CRMUSERKEY** | **String**| API2CRM user key | [default to &#39;e2a6379ab878ae7e58119d4ec842bf9c&#39;]
 **pageSize** | **Number**| Amount of results (default: 25) | [optional] 
 **page** | **Number**| Page to show (default: 1) | [optional] 
 **filter** | **String**| Filter | [optional] 
 **fields** | **String**| Comma-separated list of fields to include in the response | [optional] 
 **sort** | **String**| Specifies ascending or descending sort on existing fields | [optional] 

### Return type

[**[ApplicationEntityList]**](ApplicationEntityList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApplicationCountCollection

> Count getApplicationCountCollection(xAPI2CRMUSERKEY, opts)

COUNT for application

Count all applications from the system

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.ApplicationApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | API2CRM user key
let opts = {
  'filter': "filter_example" // String | Filter
};
apiInstance.getApplicationCountCollection(xAPI2CRMUSERKEY, opts, (error, data, response) => {
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
 **xAPI2CRMUSERKEY** | **String**| API2CRM user key | [default to &#39;e2a6379ab878ae7e58119d4ec842bf9c&#39;]
 **filter** | **String**| Filter | [optional] 

### Return type

[**Count**](Count.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApplicationEntity

> ApplicationEntity getApplicationEntity(xAPI2CRMUSERKEY, key, opts)

GET for application

Return application information

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.ApplicationApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | API2CRM user key
let key = "key_example"; // String | Application key
let opts = {
  'fields': "fields_example" // String | Comma-separated list of fields to include in the response
};
apiInstance.getApplicationEntity(xAPI2CRMUSERKEY, key, opts, (error, data, response) => {
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
 **xAPI2CRMUSERKEY** | **String**| API2CRM user key | [default to &#39;e2a6379ab878ae7e58119d4ec842bf9c&#39;]
 **key** | **String**| Application key | 
 **fields** | **String**| Comma-separated list of fields to include in the response | [optional] 

### Return type

[**ApplicationEntity**](ApplicationEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateApplicationEntity

> ApplicationEntityRelation updateApplicationEntity(xAPI2CRMUSERKEY, key, body)

PUT for application

Update application information

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.ApplicationApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | API2CRM user key
let key = "key_example"; // String | Application key
let body = new Data2CrmApi.ApplicationEntityWrite(); // ApplicationEntityWrite | Update application information
apiInstance.updateApplicationEntity(xAPI2CRMUSERKEY, key, body, (error, data, response) => {
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
 **xAPI2CRMUSERKEY** | **String**| API2CRM user key | [default to &#39;e2a6379ab878ae7e58119d4ec842bf9c&#39;]
 **key** | **String**| Application key | 
 **body** | [**ApplicationEntityWrite**](ApplicationEntityWrite.md)| Update application information | 

### Return type

[**ApplicationEntityRelation**](ApplicationEntityRelation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

