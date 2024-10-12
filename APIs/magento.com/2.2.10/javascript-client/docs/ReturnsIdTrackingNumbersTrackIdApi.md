# MagentoB2B.ReturnsIdTrackingNumbersTrackIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rmaTrackManagementV1RemoveTrackByIdDelete**](ReturnsIdTrackingNumbersTrackIdApi.md#rmaTrackManagementV1RemoveTrackByIdDelete) | **DELETE** /V1/returns/{id}/tracking-numbers/{trackId} | returns/{id}/tracking-numbers/{trackId}



## rmaTrackManagementV1RemoveTrackByIdDelete

> Boolean rmaTrackManagementV1RemoveTrackByIdDelete(id, trackId)

returns/{id}/tracking-numbers/{trackId}

Remove track by id

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ReturnsIdTrackingNumbersTrackIdApi();
let id = 56; // Number | 
let trackId = 56; // Number | 
apiInstance.rmaTrackManagementV1RemoveTrackByIdDelete(id, trackId, (error, data, response) => {
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
 **id** | **Number**|  | 
 **trackId** | **Number**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

