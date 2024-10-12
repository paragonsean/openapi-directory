# CallFireApiDocumentation.ReportsApi

All URIs are relative to *https://api.callfire.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDeliveryReports**](ReportsApi.md#getDeliveryReports) | **GET** /reports/delivery | Get delivery reports by ad hoc criteria



## getDeliveryReports

> PageDeliveryReport getDeliveryReports(opts)

Get delivery reports by ad hoc criteria

Get delivery reports

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.ReportsApi();
let opts = {
  'startDate': "startDate_example", // String | ~
  'endDate': "endDate_example", // String | ~
  'limit': 100, // Number | To set the maximum number of records to return in a paged list response. The default is 100
  'offset': 0, // Number | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
  'campaignId': 789, // Number | ~
  'fromNumber': "fromNumber_example", // String | ~
  'toNumber': "toNumber_example", // String | ~
  'deliveryCategory': "deliveryCategory_example", // String | ~
  'deliveryState': "deliveryState_example", // String | ~
  'carrier': "carrier_example", // String | ~
  'messageText': "messageText_example" // String | ~
};
apiInstance.getDeliveryReports(opts, (error, data, response) => {
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
 **startDate** | **String**| ~ | [optional] 
 **endDate** | **String**| ~ | [optional] 
 **limit** | **Number**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 100]
 **offset** | **Number**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0]
 **campaignId** | **Number**| ~ | [optional] 
 **fromNumber** | **String**| ~ | [optional] 
 **toNumber** | **String**| ~ | [optional] 
 **deliveryCategory** | **String**| ~ | [optional] 
 **deliveryState** | **String**| ~ | [optional] 
 **carrier** | **String**| ~ | [optional] 
 **messageText** | **String**| ~ | [optional] 

### Return type

[**PageDeliveryReport**](PageDeliveryReport.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

