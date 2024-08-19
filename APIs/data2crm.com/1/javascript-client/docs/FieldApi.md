# Data2CrmApi.FieldApi

All URIs are relative to *https://api-2445581398133.apicast.io:443/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getFieldCollection**](FieldApi.md#getFieldCollection) | **GET** /application/field/list | GET for field
[**getFieldCountCollection**](FieldApi.md#getFieldCountCollection) | **GET** /application/field/count | COUNT for field
[**getFieldEntity**](FieldApi.md#getFieldEntity) | **GET** /application/field/{field_id} | GET for field



## getFieldCollection

> [FieldEntity] getFieldCollection(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts)

GET for field

Returns all fields from the system

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.FieldApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let opts = {
  'xAPI2CRMDESCRIBELIFETIME': "xAPI2CRMDESCRIBELIFETIME_example", // String | Describe lifetime
  'pageSize': 56, // Number | Amount of results (default: 25)
  'page': 56, // Number | Page to show (default: 1)
  'filter': "filter_example", // String | Filter
  'fields': "fields_example" // String | Comma-separated list of fields to include in the response
};
apiInstance.getFieldCollection(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, opts, (error, data, response) => {
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
 **xAPI2CRMDESCRIBELIFETIME** | **String**| Describe lifetime | [optional] 
 **pageSize** | **Number**| Amount of results (default: 25) | [optional] 
 **page** | **Number**| Page to show (default: 1) | [optional] 
 **filter** | **String**| Filter | [optional] 
 **fields** | **String**| Comma-separated list of fields to include in the response | [optional] 

### Return type

[**[FieldEntity]**](FieldEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFieldCountCollection

> Count getFieldCountCollection(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY)

COUNT for field

Count all fields from the system

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.FieldApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
apiInstance.getFieldCountCollection(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, (error, data, response) => {
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

### Return type

[**Count**](Count.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFieldEntity

> FieldEntity getFieldEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, fieldId, opts)

GET for field

Return field information

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.FieldApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let fieldId = "fieldId_example"; // String | Field Identifier
let opts = {
  'xAPI2CRMDESCRIBELIFETIME': "xAPI2CRMDESCRIBELIFETIME_example", // String | Describe lifetime
  'fields': "fields_example" // String | Comma-separated list of fields to include in the response
};
apiInstance.getFieldEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, fieldId, opts, (error, data, response) => {
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
 **fieldId** | **String**| Field Identifier | 
 **xAPI2CRMDESCRIBELIFETIME** | **String**| Describe lifetime | [optional] 
 **fields** | **String**| Comma-separated list of fields to include in the response | [optional] 

### Return type

[**FieldEntity**](FieldEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

