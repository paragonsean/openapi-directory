# TrapStreetApi.DefaultApi

All URIs are relative to *https://api.trapstreet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addressGet**](DefaultApi.md#addressGet) | **GET** /{address} | 



## addressGet

> AddressGet200Response addressGet(address)



### Example

```javascript
import TrapStreetApi from 'trap_street_api';

let apiInstance = new TrapStreetApi.DefaultApi();
let address = "address_example"; // String | 
apiInstance.addressGet(address, (error, data, response) => {
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
 **address** | **String**|  | 

### Return type

[**AddressGet200Response**](AddressGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

