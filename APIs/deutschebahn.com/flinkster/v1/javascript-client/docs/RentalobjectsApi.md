# FlinksterApiNg.RentalobjectsApi

All URIs are relative to *https://api.deutschebahn.com/flinkster-api-ng/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getRentalObject**](RentalobjectsApi.md#getRentalObject) | **GET** /providernetworks/{providernetworkUID}/rentalobjects/{rentalObjectUID} | Get information about the RentalObject.



## getRentalObject

> RentalObjectJO getRentalObject(rentalObjectUID, providernetworkUID, opts)

Get information about the RentalObject.

Get information about the Rental Object. 

### Example

```javascript
import FlinksterApiNg from 'flinkster_api_ng';

let apiInstance = new FlinksterApiNg.RentalobjectsApi();
let rentalObjectUID = "rentalObjectUID_example"; // String | 
let providernetworkUID = "providernetworkUID_example"; // String | 
let opts = {
  'expand': "expand_example" // String | 
};
apiInstance.getRentalObject(rentalObjectUID, providernetworkUID, opts, (error, data, response) => {
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
 **rentalObjectUID** | **String**|  | 
 **providernetworkUID** | **String**|  | 
 **expand** | **String**|  | [optional] 

### Return type

[**RentalObjectJO**](RentalObjectJO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

