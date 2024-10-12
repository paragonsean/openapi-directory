# RemoteSettingsProd.ChangessApi

All URIs are relative to *https://firefox.settings.services.mozilla.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getChangess**](ChangessApi.md#getChangess) | **GET** /buckets/monitor/collections/changes/records | 



## getChangess

> Schema1 getChangess(opts)



### Example

```javascript
import RemoteSettingsProd from 'remote_settings_prod';

let apiInstance = new RemoteSettingsProd.ChangessApi();
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
apiInstance.getChangess(opts, (error, data, response) => {
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

[**Schema1**](Schema1.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

