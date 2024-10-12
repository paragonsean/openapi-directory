# Qakka.StatusApi

All URIs are relative to *https://apache.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**status**](StatusApi.md#status) | **GET** /status | Status of webapp.



## status

> Object status()

Status of webapp.



### Example

```javascript
import Qakka from 'qakka';

let apiInstance = new Qakka.StatusApi();
apiInstance.status((error, data, response) => {
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

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

