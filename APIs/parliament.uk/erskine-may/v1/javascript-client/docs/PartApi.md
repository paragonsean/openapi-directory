# ErskineMayApi.PartApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiPartGet**](PartApi.md#apiPartGet) | **GET** /api/Part | Returns a list of all parts.
[**apiPartPartNumberGet**](PartApi.md#apiPartPartNumberGet) | **GET** /api/Part/{partNumber} | Returns a part by part number.



## apiPartGet

> [ErskineMayPart] apiPartGet()

Returns a list of all parts.

### Example

```javascript
import ErskineMayApi from 'erskine_may_api';

let apiInstance = new ErskineMayApi.PartApi();
apiInstance.apiPartGet((error, data, response) => {
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

[**[ErskineMayPart]**](ErskineMayPart.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiPartPartNumberGet

> ErskineMayPart apiPartPartNumberGet(partNumber)

Returns a part by part number.

### Example

```javascript
import ErskineMayApi from 'erskine_may_api';

let apiInstance = new ErskineMayApi.PartApi();
let partNumber = 56; // Number | Part by part number
apiInstance.apiPartPartNumberGet(partNumber, (error, data, response) => {
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
 **partNumber** | **Number**| Part by part number | 

### Return type

[**ErskineMayPart**](ErskineMayPart.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

