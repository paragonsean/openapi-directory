# Data2CrmApi.InternalUserApi

All URIs are relative to *https://api-2445581398133.apicast.io:443/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createInternalUserEntity**](InternalUserApi.md#createInternalUserEntity) | **POST** /user | POST for internalUser
[**deleteInternalUserEntity**](InternalUserApi.md#deleteInternalUserEntity) | **DELETE** /user/{internal_user_id} | DELETE for internalUser
[**getInternalUserCollection**](InternalUserApi.md#getInternalUserCollection) | **GET** /user/list | GET for internalUser
[**getInternalUserCountCollection**](InternalUserApi.md#getInternalUserCountCollection) | **GET** /user/count | COUNT for internalUser
[**getInternalUserEntity**](InternalUserApi.md#getInternalUserEntity) | **GET** /user/{internal_user_id} | GET for internalUser
[**updateInternalUserEntity**](InternalUserApi.md#updateInternalUserEntity) | **PUT** /user/{internal_user_id} | PUT for internalUser



## createInternalUserEntity

> InternalUserEntityRelation createInternalUserEntity(xAPI2CRMUSERKEY, body)

POST for internalUser

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.InternalUserApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let body = new Data2CrmApi.InternalUserEntity(); // InternalUserEntity | 
apiInstance.createInternalUserEntity(xAPI2CRMUSERKEY, body, (error, data, response) => {
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
 **body** | [**InternalUserEntity**](InternalUserEntity.md)|  | 

### Return type

[**InternalUserEntityRelation**](InternalUserEntityRelation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteInternalUserEntity

> deleteInternalUserEntity(xAPI2CRMUSERKEY, internalUserId)

DELETE for internalUser

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.InternalUserApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let internalUserId = "internalUserId_example"; // String | Internal User Key
apiInstance.deleteInternalUserEntity(xAPI2CRMUSERKEY, internalUserId, (error, data, response) => {
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
 **internalUserId** | **String**| Internal User Key | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getInternalUserCollection

> [InternalUserEntity] getInternalUserCollection(xAPI2CRMUSERKEY, opts)

GET for internalUser

Returns all internal users from the system

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.InternalUserApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let opts = {
  'pageSize': 56, // Number | Amount of results (default: 25)
  'page': 56, // Number | Page to show (default: 1)
  'filter': "filter_example", // String | Filter
  'fields': "fields_example", // String | Comma-separated list of fields to include in the response
  'sort': "sort_example", // String | Specifies ascending or descending sort on existing fields
  'applicationRequestStart': new Date("2013-10-20"), // Date | All Application Requests from this date
  'applicationRequestEnd': new Date("2013-10-20") // Date | All Application Requests until this date
};
apiInstance.getInternalUserCollection(xAPI2CRMUSERKEY, opts, (error, data, response) => {
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
 **pageSize** | **Number**| Amount of results (default: 25) | [optional] 
 **page** | **Number**| Page to show (default: 1) | [optional] 
 **filter** | **String**| Filter | [optional] 
 **fields** | **String**| Comma-separated list of fields to include in the response | [optional] 
 **sort** | **String**| Specifies ascending or descending sort on existing fields | [optional] 
 **applicationRequestStart** | **Date**| All Application Requests from this date | [optional] 
 **applicationRequestEnd** | **Date**| All Application Requests until this date | [optional] 

### Return type

[**[InternalUserEntity]**](InternalUserEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInternalUserCountCollection

> Count getInternalUserCountCollection(xAPI2CRMUSERKEY, opts)

COUNT for internalUser

Count all internal users from the system

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.InternalUserApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let opts = {
  'filter': "filter_example" // String | Filter
};
apiInstance.getInternalUserCountCollection(xAPI2CRMUSERKEY, opts, (error, data, response) => {
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
 **filter** | **String**| Filter | [optional] 

### Return type

[**Count**](Count.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInternalUserEntity

> InternalUserEntity getInternalUserEntity(xAPI2CRMUSERKEY, internalUserId, opts)

GET for internalUser

Return internal user information

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.InternalUserApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let internalUserId = "internalUserId_example"; // String | Internal User Key
let opts = {
  'fields': "fields_example", // String | Comma-separated list of fields to include in the response
  'applicationRequestStart': new Date("2013-10-20"), // Date | All Application Requests from this date
  'applicationRequestEnd': new Date("2013-10-20") // Date | All Application Requests until this date
};
apiInstance.getInternalUserEntity(xAPI2CRMUSERKEY, internalUserId, opts, (error, data, response) => {
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
 **internalUserId** | **String**| Internal User Key | 
 **fields** | **String**| Comma-separated list of fields to include in the response | [optional] 
 **applicationRequestStart** | **Date**| All Application Requests from this date | [optional] 
 **applicationRequestEnd** | **Date**| All Application Requests until this date | [optional] 

### Return type

[**InternalUserEntity**](InternalUserEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateInternalUserEntity

> InternalUserEntityRelation updateInternalUserEntity(xAPI2CRMUSERKEY, internalUserId, body)

PUT for internalUser

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.InternalUserApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let internalUserId = "internalUserId_example"; // String | Internal User Key
let body = new Data2CrmApi.InternalUserEntity(); // InternalUserEntity | 
apiInstance.updateInternalUserEntity(xAPI2CRMUSERKEY, internalUserId, body, (error, data, response) => {
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
 **internalUserId** | **String**| Internal User Key | 
 **body** | [**InternalUserEntity**](InternalUserEntity.md)|  | 

### Return type

[**InternalUserEntityRelation**](InternalUserEntityRelation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

