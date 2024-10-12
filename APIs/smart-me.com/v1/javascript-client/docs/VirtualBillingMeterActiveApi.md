# SmartMe.VirtualBillingMeterActiveApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualBillingMeterActiveGet**](VirtualBillingMeterActiveApi.md#virtualBillingMeterActiveGet) | **GET** /api/VirtualBillingMeterActive | Beta: Gets all active virtual meters
[**virtualBillingMeterActivePost**](VirtualBillingMeterActiveApi.md#virtualBillingMeterActivePost) | **POST** /api/VirtualBillingMeterActive | Beta: Virtual Meter API: Activates a Meter and add the Consumption to a Virtual Meter assosiated with the User.



## virtualBillingMeterActiveGet

> [Device] virtualBillingMeterActiveGet()

Beta: Gets all active virtual meters

Beta: Gets all active virtual meters.

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.VirtualBillingMeterActiveApi();
apiInstance.virtualBillingMeterActiveGet((error, data, response) => {
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


## virtualBillingMeterActivePost

> Device virtualBillingMeterActivePost(vMeterToActivate)

Beta: Virtual Meter API: Activates a Meter and add the Consumption to a Virtual Meter assosiated with the User.

Beta: Virtual Meter API: Activates a Meter and add the Consumption to a Virtual Meter assosiated with the User.

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.VirtualBillingMeterActiveApi();
let vMeterToActivate = new SmartMe.VMeterToActivate(); // VMeterToActivate | The Meter to activate
apiInstance.virtualBillingMeterActivePost(vMeterToActivate, (error, data, response) => {
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
 **vMeterToActivate** | [**VMeterToActivate**](VMeterToActivate.md)| The Meter to activate | 

### Return type

[**Device**](Device.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml

