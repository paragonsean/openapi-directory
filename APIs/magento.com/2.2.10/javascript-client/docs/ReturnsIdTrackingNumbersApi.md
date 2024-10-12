# MagentoB2B.ReturnsIdTrackingNumbersApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rmaTrackManagementV1AddTrackPost**](ReturnsIdTrackingNumbersApi.md#rmaTrackManagementV1AddTrackPost) | **POST** /V1/returns/{id}/tracking-numbers | returns/{id}/tracking-numbers
[**rmaTrackManagementV1GetTracksGet**](ReturnsIdTrackingNumbersApi.md#rmaTrackManagementV1GetTracksGet) | **GET** /V1/returns/{id}/tracking-numbers | returns/{id}/tracking-numbers



## rmaTrackManagementV1AddTrackPost

> Boolean rmaTrackManagementV1AddTrackPost(id, opts)

returns/{id}/tracking-numbers

Add track

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ReturnsIdTrackingNumbersApi();
let id = 56; // Number | 
let opts = {
  'rmaTrackManagementV1AddTrackPostRequest': new MagentoB2B.RmaTrackManagementV1AddTrackPostRequest() // RmaTrackManagementV1AddTrackPostRequest | 
};
apiInstance.rmaTrackManagementV1AddTrackPost(id, opts, (error, data, response) => {
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
 **rmaTrackManagementV1AddTrackPostRequest** | [**RmaTrackManagementV1AddTrackPostRequest**](RmaTrackManagementV1AddTrackPostRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## rmaTrackManagementV1GetTracksGet

> RmaDataTrackSearchResultInterface rmaTrackManagementV1GetTracksGet(id)

returns/{id}/tracking-numbers

Get track list

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ReturnsIdTrackingNumbersApi();
let id = 56; // Number | 
apiInstance.rmaTrackManagementV1GetTracksGet(id, (error, data, response) => {
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

### Return type

[**RmaDataTrackSearchResultInterface**](RmaDataTrackSearchResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

