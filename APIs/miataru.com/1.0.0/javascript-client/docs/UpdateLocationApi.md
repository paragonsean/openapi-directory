# Miataru.UpdateLocationApi

All URIs are relative to *http://service.miataru.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**updateLocation**](UpdateLocationApi.md#updateLocation) | **POST** /UpdateLocation | 



## updateLocation

> ACK updateLocation(body)



This method is used to update the location of a device. The device does not need to be known already to the Miataru server but it rather creates a unique identifier for itself in the client application. This unique identifier, or device ID is then used to address this particular device.

### Example

```javascript
import Miataru from 'miataru';

let apiInstance = new Miataru.UpdateLocationApi();
let body = new Miataru.MiataruUpdateLocationRequest(); // MiataruUpdateLocationRequest | the body of this UpdateLocation POST request contains the JSON formatted parameters.
apiInstance.updateLocation(body, (error, data, response) => {
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
 **body** | [**MiataruUpdateLocationRequest**](MiataruUpdateLocationRequest.md)| the body of this UpdateLocation POST request contains the JSON formatted parameters. | 

### Return type

[**ACK**](ACK.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

