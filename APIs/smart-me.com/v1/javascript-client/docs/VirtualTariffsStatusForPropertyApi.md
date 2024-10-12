# SmartMe.VirtualTariffsStatusForPropertyApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualTariffsStatusForPropertyGet**](VirtualTariffsStatusForPropertyApi.md#virtualTariffsStatusForPropertyGet) | **GET** /api/VirtualTariffsStatusForProperty/{id} | Gets the calculation status for a virtual tariff property



## virtualTariffsStatusForPropertyGet

> String virtualTariffsStatusForPropertyGet(id)

Gets the calculation status for a virtual tariff property

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.VirtualTariffsStatusForPropertyApi();
let id = "id_example"; // String | 
apiInstance.virtualTariffsStatusForPropertyGet(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

