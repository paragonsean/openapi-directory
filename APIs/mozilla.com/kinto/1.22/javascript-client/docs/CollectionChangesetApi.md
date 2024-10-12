# RemoteSettingsProd.CollectionChangesetApi

All URIs are relative to *https://firefox.settings.services.mozilla.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCollectionChangeset**](CollectionChangesetApi.md#getCollectionChangeset) | **GET** /buckets/{bid}/collections/{cid}/changeset | 



## getCollectionChangeset

> getCollectionChangeset(bid, cid, expected, opts)



### Example

```javascript
import RemoteSettingsProd from 'remote_settings_prod';

let apiInstance = new RemoteSettingsProd.CollectionChangesetApi();
let bid = "bid_example"; // String | 
let cid = "cid_example"; // String | 
let expected = "expected_example"; // String | 
let opts = {
  'since': "since_example", // String | 
  'limit': 56, // Number | 
  'bucket': "bucket_example", // String | 
  'collection': "collection_example" // String | 
};
apiInstance.getCollectionChangeset(bid, cid, expected, opts, (error, data, response) => {
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
 **bid** | **String**|  | 
 **cid** | **String**|  | 
 **expected** | **String**|  | 
 **since** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 
 **bucket** | **String**|  | [optional] 
 **collection** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

