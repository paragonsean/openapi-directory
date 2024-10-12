# RemoteSettingsProd.GroupsApi

All URIs are relative to *https://firefox.settings.services.mozilla.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getGroup**](GroupsApi.md#getGroup) | **GET** /buckets/{bucket_id}/groups/{id} | 
[**getGroups**](GroupsApi.md#getGroups) | **GET** /buckets/{bucket_id}/groups | 



## getGroup

> ObjectSchema2 getGroup(bucketId, id, opts)



### Example

```javascript
import RemoteSettingsProd from 'remote_settings_prod';

let apiInstance = new RemoteSettingsProd.GroupsApi();
let bucketId = "bucketId_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'fields': ["null"], // [String] | 
  'ifMatch': "ifMatch_example", // String | 
  'ifNoneMatch': "ifNoneMatch_example" // String | 
};
apiInstance.getGroup(bucketId, id, opts, (error, data, response) => {
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
 **bucketId** | **String**|  | 
 **id** | **String**|  | 
 **fields** | [**[String]**](String.md)|  | [optional] 
 **ifMatch** | **String**|  | [optional] 
 **ifNoneMatch** | **String**|  | [optional] 

### Return type

[**ObjectSchema2**](ObjectSchema2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGroups

> Schema4 getGroups(bucketId, opts)



### Example

```javascript
import RemoteSettingsProd from 'remote_settings_prod';

let apiInstance = new RemoteSettingsProd.GroupsApi();
let bucketId = "bucketId_example"; // String | 
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
apiInstance.getGroups(bucketId, opts, (error, data, response) => {
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
 **bucketId** | **String**|  | 
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

[**Schema4**](Schema4.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

