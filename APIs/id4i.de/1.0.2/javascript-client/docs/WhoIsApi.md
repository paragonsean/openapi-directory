# Id4iApi.WhoIsApi

All URIs are relative to *http://backend.id4i.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resolveWhoIsEntry_0**](WhoIsApi.md#resolveWhoIsEntry_0) | **GET** /whois/{id4n} | Resolve owner of id4n



## resolveWhoIsEntry_0

> WhoIsResponse resolveWhoIsEntry_0(id4n)

Resolve owner of id4n

### Example

```javascript
import Id4iApi from 'id4i_api';

let apiInstance = new Id4iApi.WhoIsApi();
let id4n = "id4n_example"; // String | id4n
apiInstance.resolveWhoIsEntry_0(id4n, (error, data, response) => {
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
 **id4n** | **String**| id4n | 

### Return type

[**WhoIsResponse**](WhoIsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

