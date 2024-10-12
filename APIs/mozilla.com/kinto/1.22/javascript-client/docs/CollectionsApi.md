# RemoteSettingsProd.CollectionsApi

All URIs are relative to *https://firefox.settings.services.mozilla.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCollection**](CollectionsApi.md#getCollection) | **GET** /buckets/{bucket_id}/collections/{id} | 
[**getCollections**](CollectionsApi.md#getCollections) | **GET** /buckets/{bucket_id}/collections | 



## getCollection

> ObjectSchema1 getCollection(bucketId, id, opts)



### Example

```javascript
import RemoteSettingsProd from 'remote_settings_prod';

let apiInstance = new RemoteSettingsProd.CollectionsApi();
let bucketId = "bucketId_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'fields': ["null"], // [String] | 
  'ifMatch': "ifMatch_example", // String | 
  'ifNoneMatch': "ifNoneMatch_example" // String | 
};
apiInstance.getCollection(bucketId, id, opts, (error, data, response) => {
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

[**ObjectSchema1**](ObjectSchema1.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCollections

> Schema2 getCollections(bucketId, opts)



### Example

```javascript
import RemoteSettingsProd from 'remote_settings_prod';

let apiInstance = new RemoteSettingsProd.CollectionsApi();
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
apiInstance.getCollections(bucketId, opts, (error, data, response) => {
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

[**Schema2**](Schema2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

