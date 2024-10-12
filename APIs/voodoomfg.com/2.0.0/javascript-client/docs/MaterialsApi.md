# VoodooManufacturing3DPrintApi.MaterialsApi

All URIs are relative to */api/2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**materialsGet**](MaterialsApi.md#materialsGet) | **GET** /materials | Voodoo Manufacturing offers printing in a number of different materials, with different color options for each. Your organization can expose as many or as few material options as you want to your end-customer. 



## materialsGet

> [Material] materialsGet()

Voodoo Manufacturing offers printing in a number of different materials, with different color options for each. Your organization can expose as many or as few material options as you want to your end-customer. 

The Materials endpoint returns a list of materials that are currently available for production for your account. The responses include display details about each material, along with the unique id required to request a print in a specific material. 

### Example

```javascript
import VoodooManufacturing3DPrintApi from 'voodoo_manufacturing_3_d_print_api';
let defaultClient = VoodooManufacturing3DPrintApi.ApiClient.instance;
// Configure API key authorization: Voodoo Manufacturing API Key
let Voodoo Manufacturing API Key = defaultClient.authentications['Voodoo Manufacturing API Key'];
Voodoo Manufacturing API Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Voodoo Manufacturing API Key.apiKeyPrefix = 'Token';

let apiInstance = new VoodooManufacturing3DPrintApi.MaterialsApi();
apiInstance.materialsGet((error, data, response) => {
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

[**[Material]**](Material.md)

### Authorization

[Voodoo Manufacturing API Key](../README.md#Voodoo Manufacturing API Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

