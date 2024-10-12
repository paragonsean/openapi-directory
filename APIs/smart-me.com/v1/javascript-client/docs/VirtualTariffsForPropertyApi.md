# SmartMe.VirtualTariffsForPropertyApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualTariffsForPropertyGet**](VirtualTariffsForPropertyApi.md#virtualTariffsForPropertyGet) | **GET** /api/VirtualTariffsForProperty/{id} | Gets all Virtual Tariffs for a property (folder)



## virtualTariffsForPropertyGet

> [VirtualTariffsOfFolder] virtualTariffsForPropertyGet(id)

Gets all Virtual Tariffs for a property (folder)

Gets all Virtual Tariffs for a property (folder)

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.VirtualTariffsForPropertyApi();
let id = "id_example"; // String | 
apiInstance.virtualTariffsForPropertyGet(id, (error, data, response) => {
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

[**[VirtualTariffsOfFolder]**](VirtualTariffsOfFolder.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

