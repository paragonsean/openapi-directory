# TokenJayApiServices.TokenVerificationApi

All URIs are relative to *https://api.tokenjay.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkToken**](TokenVerificationApi.md#checkToken) | **GET** /tokens/check/{tokenId}/{tokenName} | Check a token verification
[**listBlocked**](TokenVerificationApi.md#listBlocked) | **GET** /tokens/listBlocked | Lists all blocked tokens
[**listGenuine**](TokenVerificationApi.md#listGenuine) | **GET** /tokens/listGenuine | Lists all genuine tokens known



## checkToken

> CheckResponse checkToken(tokenId, tokenName)

Check a token verification

### Example

```javascript
import TokenJayApiServices from 'token_jay_api_services';

let apiInstance = new TokenJayApiServices.TokenVerificationApi();
let tokenId = "tokenId_example"; // String | 
let tokenName = "tokenName_example"; // String | 
apiInstance.checkToken(tokenId, tokenName, (error, data, response) => {
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
 **tokenId** | **String**|  | 
 **tokenName** | **String**|  | 

### Return type

[**CheckResponse**](CheckResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## listBlocked

> [String] listBlocked()

Lists all blocked tokens

### Example

```javascript
import TokenJayApiServices from 'token_jay_api_services';

let apiInstance = new TokenJayApiServices.TokenVerificationApi();
apiInstance.listBlocked((error, data, response) => {
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

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## listGenuine

> [GenuineToken] listGenuine()

Lists all genuine tokens known

### Example

```javascript
import TokenJayApiServices from 'token_jay_api_services';

let apiInstance = new TokenJayApiServices.TokenVerificationApi();
apiInstance.listGenuine((error, data, response) => {
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

[**[GenuineToken]**](GenuineToken.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

