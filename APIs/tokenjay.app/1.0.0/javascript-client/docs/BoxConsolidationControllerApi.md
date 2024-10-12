# TokenJayApiServices.BoxConsolidationControllerApi

All URIs are relative to *https://api.tokenjay.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**epConsolidate**](BoxConsolidationControllerApi.md#epConsolidate) | **GET** /mosaik/boxconsolidation/consolidate/{p2pkaddress} | 
[**mainApp1**](BoxConsolidationControllerApi.md#mainApp1) | **GET** /mosaik/boxconsolidation/ | 



## epConsolidate

> ErgoPayResponse epConsolidate(p2pkaddress)



### Example

```javascript
import TokenJayApiServices from 'token_jay_api_services';

let apiInstance = new TokenJayApiServices.BoxConsolidationControllerApi();
let p2pkaddress = "p2pkaddress_example"; // String | 
apiInstance.epConsolidate(p2pkaddress, (error, data, response) => {
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
 **p2pkaddress** | **String**|  | 

### Return type

[**ErgoPayResponse**](ErgoPayResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## mainApp1

> MosaikApp mainApp1()



### Example

```javascript
import TokenJayApiServices from 'token_jay_api_services';

let apiInstance = new TokenJayApiServices.BoxConsolidationControllerApi();
apiInstance.mainApp1((error, data, response) => {
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

