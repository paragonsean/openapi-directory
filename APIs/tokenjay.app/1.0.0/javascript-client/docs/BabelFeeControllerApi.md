# TokenJayApiServices.BabelFeeControllerApi

All URIs are relative to *https://api.tokenjay.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkForNotifications**](BabelFeeControllerApi.md#checkForNotifications) | **GET** /mosaik/babelfee/notificationcheck | 
[**ergoPayCreateBabelBox1**](BabelFeeControllerApi.md#ergoPayCreateBabelBox1) | **GET** /cancelbabel/{boxId} | 
[**getBabelFeeOverview**](BabelFeeControllerApi.md#getBabelFeeOverview) | **GET** /mosaik/babelfee/ | 



## checkForNotifications

> NotificationCheckResponse checkForNotifications()



### Example

```javascript
import TokenJayApiServices from 'token_jay_api_services';

let apiInstance = new TokenJayApiServices.BabelFeeControllerApi();
apiInstance.checkForNotifications((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**NotificationCheckResponse**](NotificationCheckResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## ergoPayCreateBabelBox1

> ErgoPayResponse ergoPayCreateBabelBox1(boxId)



### Example

```javascript
import TokenJayApiServices from 'token_jay_api_services';

let apiInstance = new TokenJayApiServices.BabelFeeControllerApi();
let boxId = "boxId_example"; // String | 
apiInstance.ergoPayCreateBabelBox1(boxId, (error, data, response) => {
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
 **boxId** | **String**|  | 

### Return type

[**ErgoPayResponse**](ErgoPayResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getBabelFeeOverview

> MosaikApp getBabelFeeOverview()



### Example

```javascript
import TokenJayApiServices from 'token_jay_api_services';

let apiInstance = new TokenJayApiServices.BabelFeeControllerApi();
apiInstance.getBabelFeeOverview((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**MosaikApp**](MosaikApp.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

