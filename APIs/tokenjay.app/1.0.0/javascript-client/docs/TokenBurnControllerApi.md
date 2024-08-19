# TokenJayApiServices.TokenBurnControllerApi

All URIs are relative to *https://api.tokenjay.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBurningTransaction**](TokenBurnControllerApi.md#getBurningTransaction) | **GET** /mosaik/tokenburn/get/{uuid} | 
[**mainApp**](TokenBurnControllerApi.md#mainApp) | **GET** /mosaik/tokenburn | 
[**prepareTransaction**](TokenBurnControllerApi.md#prepareTransaction) | **POST** /mosaik/tokenburn/prepare | 



## getBurningTransaction

> ErgoPayResponse getBurningTransaction(uuid)



### Example

```javascript
import TokenJayApiServices from 'token_jay_api_services';

let apiInstance = new TokenJayApiServices.TokenBurnControllerApi();
let uuid = "uuid_example"; // String | 
apiInstance.getBurningTransaction(uuid, (error, data, response) => {
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
 **uuid** | **String**|  | 

### Return type

[**ErgoPayResponse**](ErgoPayResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## mainApp

> MosaikApp mainApp()



### Example

```javascript
import TokenJayApiServices from 'token_jay_api_services';

let apiInstance = new TokenJayApiServices.TokenBurnControllerApi();
apiInstance.mainApp((error, data, response) => {
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


## prepareTransaction

> FetchActionResponse prepareTransaction(requestBody)



### Example

```javascript
import TokenJayApiServices from 'token_jay_api_services';

let apiInstance = new TokenJayApiServices.TokenBurnControllerApi();
let requestBody = {key: null}; // {String: Object} | 
apiInstance.prepareTransaction(requestBody, (error, data, response) => {
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
 **requestBody** | [**{String: Object}**](Object.md)|  | 

### Return type

[**FetchActionResponse**](FetchActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*

