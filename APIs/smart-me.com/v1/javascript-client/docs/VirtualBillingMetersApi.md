# SmartMe.VirtualBillingMetersApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualBillingMetersGet**](VirtualBillingMetersApi.md#virtualBillingMetersGet) | **GET** /api/VirtualBillingMeters | Beta: Gets all Meters available to activate as a Virtual Meter.



## virtualBillingMetersGet

> [Device] virtualBillingMetersGet()

Beta: Gets all Meters available to activate as a Virtual Meter.

Beta: Gets all Meters available to activate as a Virtual Meter.

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.VirtualBillingMetersApi();
apiInstance.virtualBillingMetersGet((error, data, response) => {
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

[**[Device]**](Device.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

