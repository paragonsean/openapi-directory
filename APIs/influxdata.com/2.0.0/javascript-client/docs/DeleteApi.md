# InfluxOssApiService.DeleteApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postDelete**](DeleteApi.md#postDelete) | **POST** /delete | Delete time series data from InfluxDB



## postDelete

> postDelete(deletePredicateRequest, opts)

Delete time series data from InfluxDB

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.DeleteApi();
let deletePredicateRequest = new InfluxOssApiService.DeletePredicateRequest(); // DeletePredicateRequest | Predicate delete request
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}", // String | OpenTracing span context
  'org': "org_example", // String | Specifies the organization to delete data from.
  'bucket': "bucket_example", // String | Specifies the bucket to delete data from.
  'orgID': "orgID_example", // String | Specifies the organization ID of the resource.
  'bucketID': "bucketID_example" // String | Specifies the bucket ID to delete data from.
};
apiInstance.postDelete(deletePredicateRequest, opts, (error, data, response) => {
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
 **deletePredicateRequest** | [**DeletePredicateRequest**](DeletePredicateRequest.md)| Predicate delete request | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 
 **org** | **String**| Specifies the organization to delete data from. | [optional] 
 **bucket** | **String**| Specifies the bucket to delete data from. | [optional] 
 **orgID** | **String**| Specifies the organization ID of the resource. | [optional] 
 **bucketID** | **String**| Specifies the bucket ID to delete data from. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

