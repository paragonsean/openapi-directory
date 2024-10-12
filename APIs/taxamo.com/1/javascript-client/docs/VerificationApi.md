# Taxamo.VerificationApi

All URIs are relative to *https://api.taxamo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSMSToken**](VerificationApi.md#createSMSToken) | **POST** /api/v1/verification/sms | Create SMS token
[**verifySMSToken**](VerificationApi.md#verifySMSToken) | **GET** /api/v1/verification/sms/{token} | Verify SMS token



## createSMSToken

> CreateSMSTokenOut createSMSToken(input)

Create SMS token

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.VerificationApi();
let input = new Taxamo.CreateSMSTokenIn(); // CreateSMSTokenIn | Input
apiInstance.createSMSToken(input, (error, data, response) => {
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
 **input** | [**CreateSMSTokenIn**](CreateSMSTokenIn.md)| Input | 

### Return type

[**CreateSMSTokenOut**](CreateSMSTokenOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## verifySMSToken

> VerifySMSTokenOut verifySMSToken(token)

Verify SMS token

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.VerificationApi();
let token = "token_example"; // String | Provided token.
apiInstance.verifySMSToken(token, (error, data, response) => {
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
 **token** | **String**| Provided token. | 

### Return type

[**VerifySMSTokenOut**](VerifySMSTokenOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

