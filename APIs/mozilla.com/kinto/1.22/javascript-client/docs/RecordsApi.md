# RemoteSettingsProd.RecordsApi

All URIs are relative to *https://firefox.settings.services.mozilla.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getRecord**](RecordsApi.md#getRecord) | **GET** /buckets/{bucket_id}/collections/{collection_id}/records/{id} | 
[**getRecords**](RecordsApi.md#getRecords) | **GET** /buckets/{bucket_id}/collections/{collection_id}/records | 



## getRecord

> ObjectSchema getRecord(bucketId, collectionId, id, opts)



### Example

```javascript
import RemoteSettingsProd from 'remote_settings_prod';

let apiInstance = new RemoteSettingsProd.RecordsApi();
let bucketId = "bucketId_example"; // String | 
let collectionId = "collectionId_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'fields': ["null"], // [String] | 
  'ifMatch': "ifMatch_example", // String | 
  'ifNoneMatch': "ifNoneMatch_example" // String | 
};
apiInstance.getRecord(bucketId, collectionId, id, opts, (error, data, response) => {
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
 **collectionId** | **String**|  | 
 **id** | **String**|  | 
 **fields** | [**[String]**](String.md)|  | [optional] 
 **ifMatch** | **String**|  | [optional] 
 **ifNoneMatch** | **String**|  | [optional] 

### Return type

[**ObjectSchema**](ObjectSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRecords

> Schema3 getRecords(bucketId, collectionId, opts)



### Example

```javascript
import RemoteSettingsProd from 'remote_settings_prod';

let apiInstance = new RemoteSettingsProd.RecordsApi();
let bucketId = "bucketId_example"; // String | 
let collectionId = "collectionId_example"; // String | 
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
apiInstance.getRecords(bucketId, collectionId, opts, (error, data, response) => {
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
 **collectionId** | **String**|  | 
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

[**Schema3**](Schema3.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

