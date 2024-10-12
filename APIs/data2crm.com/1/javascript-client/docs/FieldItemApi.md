# Data2CrmApi.FieldItemApi

All URIs are relative to *https://api-2445581398133.apicast.io:443/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createFieldItemEntity**](FieldItemApi.md#createFieldItemEntity) | **POST** /application/field/{field_id} | POST for fieldItem
[**deleteFieldItemEntity**](FieldItemApi.md#deleteFieldItemEntity) | **DELETE** /application/field/{field_id}/{field_item_id} | DELETE for fieldItem
[**getFieldItemCollection**](FieldItemApi.md#getFieldItemCollection) | **GET** /application/field/{field_id}/list | GET for fieldItem
[**getFieldItemCountCollection**](FieldItemApi.md#getFieldItemCountCollection) | **GET** /application/field/{field_id}/count | COUNT for fieldItem
[**getFieldItemDescribe**](FieldItemApi.md#getFieldItemDescribe) | **GET** /application/field/{field_id}/describe | DESCRIBE for fieldItem
[**getFieldItemEntity**](FieldItemApi.md#getFieldItemEntity) | **GET** /application/field/{field_id}/{field_item_id} | GET for fieldItem
[**updateFieldItemEntity**](FieldItemApi.md#updateFieldItemEntity) | **PUT** /application/field/{field_id}/{field_item_id} | PUT for fieldItem



## createFieldItemEntity

> FieldItemEntityRelation createFieldItemEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, fieldId, body, opts)

POST for fieldItem

Add field item into the system

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.FieldItemApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let fieldId = "fieldId_example"; // String | Field Identifier
let body = new Data2CrmApi.FieldItemEntity(); // FieldItemEntity | Add field item into the system
let opts = {
  'xAPI2CRMDESCRIBELIFETIME': "xAPI2CRMDESCRIBELIFETIME_example" // String | Describe lifetime
};
apiInstance.createFieldItemEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, fieldId, body, opts, (error, data, response) => {
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
 **body** | [**FieldItemEntity**](FieldItemEntity.md)| Add field item into the system | 
 **xAPI2CRMDESCRIBELIFETIME** | **String**| Describe lifetime | [optional] 

### Return type

[**FieldItemEntityRelation**](FieldItemEntityRelation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteFieldItemEntity

> deleteFieldItemEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, fieldId, fieldItemId)

DELETE for fieldItem

Delete field item information

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.FieldItemApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let fieldId = "fieldId_example"; // String | Field Identifier
let fieldItemId = "fieldItemId_example"; // String | Field Item Identifier
apiInstance.deleteFieldItemEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, fieldId, fieldItemId, (error, data, response) => {
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
 **fieldId** | **String**| Field Identifier | 
 **fieldItemId** | **String**| Field Item Identifier | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getFieldItemCollection

> [FieldItemEntity] getFieldItemCollection(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, fieldId, opts)

GET for fieldItem

Returns all fields from the system items

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.FieldItemApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let fieldId = "fieldId_example"; // String | Field Identifier
let opts = {
  'xAPI2CRMDESCRIBELIFETIME': "xAPI2CRMDESCRIBELIFETIME_example", // String | Describe lifetime
  'pageSize': 56, // Number | Amount of results (default: 25)
  'page': 56, // Number | Page to show (default: 1)
  'fields': "fields_example" // String | Comma-separated list of fields to include in the response
};
apiInstance.getFieldItemCollection(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, fieldId, opts, (error, data, response) => {
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
 **pageSize** | **Number**| Amount of results (default: 25) | [optional] 
 **page** | **Number**| Page to show (default: 1) | [optional] 
 **fields** | **String**| Comma-separated list of fields to include in the response | [optional] 

### Return type

[**[FieldItemEntity]**](FieldItemEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFieldItemCountCollection

> Count getFieldItemCountCollection(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, fieldId)

COUNT for fieldItem

Count all field items from the system

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.FieldItemApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let fieldId = "fieldId_example"; // String | Field Identifier
apiInstance.getFieldItemCountCollection(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, fieldId, (error, data, response) => {
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

### Return type

[**Count**](Count.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFieldItemDescribe

> FieldItemDescribe getFieldItemDescribe(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, fieldId, opts)

DESCRIBE for fieldItem

Returns describe for field items

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.FieldItemApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let fieldId = "fieldId_example"; // String | Field Identifier
let opts = {
  'xAPI2CRMDESCRIBELIFETIME': "xAPI2CRMDESCRIBELIFETIME_example" // String | Describe lifetime
};
apiInstance.getFieldItemDescribe(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, fieldId, opts, (error, data, response) => {
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

### Return type

[**FieldItemDescribe**](FieldItemDescribe.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFieldItemEntity

> FieldItemEntity getFieldItemEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, fieldId, fieldItemId, opts)

GET for fieldItem

Return field item information

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.FieldItemApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let fieldId = "fieldId_example"; // String | Field Identifier
let fieldItemId = "fieldItemId_example"; // String | Field Item Identifier
let opts = {
  'xAPI2CRMDESCRIBELIFETIME': "xAPI2CRMDESCRIBELIFETIME_example", // String | Describe lifetime
  'fields': "fields_example" // String | Comma-separated list of fields to include in the response
};
apiInstance.getFieldItemEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, fieldId, fieldItemId, opts, (error, data, response) => {
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
 **fieldItemId** | **String**| Field Item Identifier | 
 **xAPI2CRMDESCRIBELIFETIME** | **String**| Describe lifetime | [optional] 
 **fields** | **String**| Comma-separated list of fields to include in the response | [optional] 

### Return type

[**FieldItemEntity**](FieldItemEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateFieldItemEntity

> FieldItemEntityRelation updateFieldItemEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, fieldId, fieldItemId, body, opts)

PUT for fieldItem

Update field item information

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.FieldItemApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | User Key
let xAPI2CRMAPPLICATIONKEY = "'7ae5b17008fb414d84981191cf3b66a476ef8bef'"; // String | Application Key
let fieldId = "fieldId_example"; // String | Field Identifier
let fieldItemId = "fieldItemId_example"; // String | Field Item Identifier
let body = new Data2CrmApi.FieldItemEntity(); // FieldItemEntity | Update field item information
let opts = {
  'xAPI2CRMDESCRIBELIFETIME': "xAPI2CRMDESCRIBELIFETIME_example" // String | Describe lifetime
};
apiInstance.updateFieldItemEntity(xAPI2CRMUSERKEY, xAPI2CRMAPPLICATIONKEY, fieldId, fieldItemId, body, opts, (error, data, response) => {
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
 **fieldItemId** | **String**| Field Item Identifier | 
 **body** | [**FieldItemEntity**](FieldItemEntity.md)| Update field item information | 
 **xAPI2CRMDESCRIBELIFETIME** | **String**| Describe lifetime | [optional] 

### Return type

[**FieldItemEntityRelation**](FieldItemEntityRelation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

