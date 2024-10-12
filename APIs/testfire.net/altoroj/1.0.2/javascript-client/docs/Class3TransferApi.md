# AltoroJRestApi.Class3TransferApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trasnfer**](Class3TransferApi.md#trasnfer) | **POST** /transfer | 



## trasnfer

> trasnfer(authorization, body)



Transfer money between two accounts

### Example

```javascript
import AltoroJRestApi from 'altoro_j_rest_api';

let apiInstance = new AltoroJRestApi.Class3TransferApi();
let authorization = "authorization_example"; // String | Authorization token (provided upon successful login)
let body = new AltoroJRestApi.Transfer(); // Transfer | Transfer details including ammount, sender and receiver
apiInstance.trasnfer(authorization, body, (error, data, response) => {
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
 **authorization** | **String**| Authorization token (provided upon successful login) | 
 **body** | [**Transfer**](Transfer.md)| Transfer details including ammount, sender and receiver | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

