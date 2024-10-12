# SmartMe.VirtualBillingMeterDeactivateApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualBillingMeterDeactivatePost**](VirtualBillingMeterDeactivateApi.md#virtualBillingMeterDeactivatePost) | **POST** /api/VirtualBillingMeterDeactivate | Beta: Virtual Meter API: Deactivates a Virtual Meter.



## virtualBillingMeterDeactivatePost

> Object virtualBillingMeterDeactivatePost(vMeterToDeactivate)

Beta: Virtual Meter API: Deactivates a Virtual Meter.

Beta: Virtual Meter API: Deactivates a Virtual Meter.

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.VirtualBillingMeterDeactivateApi();
let vMeterToDeactivate = new SmartMe.VMeterToDeactivate(); // VMeterToDeactivate | The Meter to activate
apiInstance.virtualBillingMeterDeactivatePost(vMeterToDeactivate, (error, data, response) => {
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
 **vMeterToDeactivate** | [**VMeterToDeactivate**](VMeterToDeactivate.md)| The Meter to activate | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml

