# Data2CrmApi.PlatformApi

All URIs are relative to *https://api-2445581398133.apicast.io:443/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPlatformCollection**](PlatformApi.md#getPlatformCollection) | **GET** /platform/list | GET for platform
[**getPlatformEntity**](PlatformApi.md#getPlatformEntity) | **GET** /platform/{type} | GET for platform



## getPlatformCollection

> [PlatformEntity] getPlatformCollection(xAPI2CRMUSERKEY, opts)

GET for platform

Returns all platforms from the system

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.PlatformApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | API2CRM user key
let opts = {
  'pageSize': 56, // Number | Amount of results (default: 25)
  'page': 56, // Number | Page to show (default: 1)
  'fields': "fields_example", // String | Comma-separated list of fields to include in the response
  'sort': "sort_example" // String | Specifies ascending or descending sort on existing fields
};
apiInstance.getPlatformCollection(xAPI2CRMUSERKEY, opts, (error, data, response) => {
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
 **fields** | **String**| Comma-separated list of fields to include in the response | [optional] 
 **sort** | **String**| Specifies ascending or descending sort on existing fields | [optional] 

### Return type

[**[PlatformEntity]**](PlatformEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPlatformEntity

> PlatformEntity getPlatformEntity(xAPI2CRMUSERKEY, type, opts)

GET for platform

Return platform information

### Example

```javascript
import Data2CrmApi from 'data2_crm_api';

let apiInstance = new Data2CrmApi.PlatformApi();
let xAPI2CRMUSERKEY = "'e2a6379ab878ae7e58119d4ec842bf9c'"; // String | API2CRM user key
let type = "type_example"; // String | Platform type
let opts = {
  'fields': "fields_example" // String | Comma-separated list of fields to include in the response
};
apiInstance.getPlatformEntity(xAPI2CRMUSERKEY, type, opts, (error, data, response) => {
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
 **type** | **String**| Platform type | 
 **fields** | **String**| Comma-separated list of fields to include in the response | [optional] 

### Return type

[**PlatformEntity**](PlatformEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

