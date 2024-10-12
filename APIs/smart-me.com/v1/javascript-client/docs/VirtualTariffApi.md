# SmartMe.VirtualTariffApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiVirtualTariffIdGet**](VirtualTariffApi.md#apiVirtualTariffIdGet) | **GET** /api/VirtualTariff/{id} | Gets all virtual tariffs of a folder
[**virtualTariffGet**](VirtualTariffApi.md#virtualTariffGet) | **GET** /api/VirtualTariff | Gets all Virtual Tariffs of a user



## apiVirtualTariffIdGet

> VirtualTariffsOfFolder apiVirtualTariffIdGet(id)

Gets all virtual tariffs of a folder

Gets all virtual tariffs of a folder

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.VirtualTariffApi();
let id = "id_example"; // String | The ID of the Folder
apiInstance.apiVirtualTariffIdGet(id, (error, data, response) => {
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
 **id** | **String**| The ID of the Folder | 

### Return type

[**VirtualTariffsOfFolder**](VirtualTariffsOfFolder.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## virtualTariffGet

> [VirtualTariffsOfFolder] virtualTariffGet()

Gets all Virtual Tariffs of a user

Gets all Virtual Tariffs of a user

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.VirtualTariffApi();
apiInstance.virtualTariffGet((error, data, response) => {
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

[**[VirtualTariffsOfFolder]**](VirtualTariffsOfFolder.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

