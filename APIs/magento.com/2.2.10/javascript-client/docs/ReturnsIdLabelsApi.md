# MagentoB2B.ReturnsIdLabelsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rmaTrackManagementV1GetShippingLabelPdfGet**](ReturnsIdLabelsApi.md#rmaTrackManagementV1GetShippingLabelPdfGet) | **GET** /V1/returns/{id}/labels | returns/{id}/labels



## rmaTrackManagementV1GetShippingLabelPdfGet

> String rmaTrackManagementV1GetShippingLabelPdfGet(id)

returns/{id}/labels

Get shipping label int the PDF format

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ReturnsIdLabelsApi();
let id = 56; // Number | 
apiInstance.rmaTrackManagementV1GetShippingLabelPdfGet(id, (error, data, response) => {
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

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

