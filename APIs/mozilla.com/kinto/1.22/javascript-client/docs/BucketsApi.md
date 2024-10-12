# RemoteSettingsProd.BucketsApi

All URIs are relative to *https://firefox.settings.services.mozilla.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBucket**](BucketsApi.md#getBucket) | **GET** /buckets/{id} | 
[**getBuckets**](BucketsApi.md#getBuckets) | **GET** /buckets | 



## getBucket

> ObjectSchema3 getBucket(id, opts)



### Example

```javascript
import RemoteSettingsProd from 'remote_settings_prod';

let apiInstance = new RemoteSettingsProd.BucketsApi();
let id = "id_example"; // String | 
let opts = {
  'fields': ["null"], // [String] | 
  'ifMatch': "ifMatch_example", // String | 
  'ifNoneMatch': "ifNoneMatch_example" // String | 
};
apiInstance.getBucket(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **fields** | [**[String]**](String.md)|  | [optional] 
 **ifMatch** | **String**|  | [optional] 
 **ifNoneMatch** | **String**|  | [optional] 

### Return type

[**ObjectSchema3**](ObjectSchema3.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBuckets

> Schema getBuckets(opts)



### Example

```javascript
import RemoteSettingsProd from 'remote_settings_prod';

let apiInstance = new RemoteSettingsProd.BucketsApi();
let opts = {
  'limit': 56, // Number | 
  'sort': ["null"], // [String] | 
  'token': "token_example", // String | 
  'since': 56, // Number | 
  'to': 56, // Number | 
  'before': 56, // Number | 
  'id': "id_example", // String | 
  'lastModified': 56, // Number | 
  'fields': ["null"], // [String] | 
  'ifMatch': "ifMatch_example", // String | 
  'ifNoneMatch': "ifNoneMatch_example" // String | 
};
apiInstance.getBuckets(opts, (error, data, response) => {
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
 **limit** | **Number**|  | [optional] 
 **sort** | [**[String]**](String.md)|  | [optional] 
 **token** | **String**|  | [optional] 
 **since** | **Number**|  | [optional] 
 **to** | **Number**|  | [optional] 
 **before** | **Number**|  | [optional] 
 **id** | **String**|  | [optional] 
 **lastModified** | **Number**|  | [optional] 
 **fields** | [**[String]**](String.md)|  | [optional] 
 **ifMatch** | **String**|  | [optional] 
 **ifNoneMatch** | **String**|  | [optional] 

### Return type

[**Schema**](Schema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

