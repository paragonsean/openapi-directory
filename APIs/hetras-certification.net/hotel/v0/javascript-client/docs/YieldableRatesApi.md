# HetrasHotelApiVersion0.YieldableRatesApi

All URIs are relative to *https://api.hetras-certification.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**yieldableRatesSavePrices**](YieldableRatesApi.md#yieldableRatesSavePrices) | **PUT** /api/hotel/v0/hotels/{hotelId}/yieldable_rateplans/{rateplanCode}/$rates | Saves Yieldable Rate Prices for existing Yieldable Rateplan.



## yieldableRatesSavePrices

> Object yieldableRatesSavePrices(appId, appKey, hotelId, rateplanCode, yieldableRatePrices)

Saves Yieldable Rate Prices for existing Yieldable Rateplan.

Saves Yieldable Rate Prices for existing Yieldable Rateplan. The rateplan has been created before and with this End Point we               create or update the rate prices. If the Yieldable rateplan prices exist it updates them with the new price if not it creates new price entries.&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.

### Example

```javascript
import HetrasHotelApiVersion0 from 'hetras_hotel_api_version_0';

let apiInstance = new HetrasHotelApiVersion0.YieldableRatesApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let hotelId = 56; // Number | Specifies the hotelId which identifies Hotel for which the operation will be performed.
let rateplanCode = "rateplanCode_example"; // String | Specifies the rateplanCode for which the operation will be performed.
let yieldableRatePrices = [new HetrasHotelApiVersion0.YieldableRateTimeSlice()]; // [YieldableRateTimeSlice] | Specifies the the Yieldable rateplan and prices details to be created or updated.
apiInstance.yieldableRatesSavePrices(appId, appKey, hotelId, rateplanCode, yieldableRatePrices, (error, data, response) => {
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
 **appId** | **String**| Application identifier | 
 **appKey** | **String**| Application key. | 
 **hotelId** | **Number**| Specifies the hotelId which identifies Hotel for which the operation will be performed. | 
 **rateplanCode** | **String**| Specifies the rateplanCode for which the operation will be performed. | 
 **yieldableRatePrices** | [**[YieldableRateTimeSlice]**](YieldableRateTimeSlice.md)| Specifies the the Yieldable rateplan and prices details to be created or updated. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

