# LhPublicApi.CargoApi

All URIs are relative to *https://api.lufthansa.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cargoGetRouteFromDateProductCodeByOriginAndDestinationGet**](CargoApi.md#cargoGetRouteFromDateProductCodeByOriginAndDestinationGet) | **GET** /cargo/getRoute/{origin}-{destination}/{fromDate}/{productCode} | Retrieve all flights
[**cargoShipmentTrackingByAWBPrefixAndAWBNumberGet**](CargoApi.md#cargoShipmentTrackingByAWBPrefixAndAWBNumberGet) | **GET** /cargo/shipmentTracking/{aWBPrefix}-{aWBNumber} | Shipment Tracking



## cargoGetRouteFromDateProductCodeByOriginAndDestinationGet

> Object cargoGetRouteFromDateProductCodeByOriginAndDestinationGet(origin, destination, fromDate, productCode, accept)

Retrieve all flights

Retrieve a list of all possible flights (both direct and connecting) between two airports on a given date. Routes are available for today and up to days in the future.

### Example

```javascript
import LhPublicApi from 'lh_public_api';
let defaultClient = LhPublicApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: auth
let auth = defaultClient.authentications['auth'];
auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LhPublicApi.CargoApi();
let origin = "origin_example"; // String | Departure Airport : 3-letter IATA airport code, e.g. FRA.
let destination = "destination_example"; // String | Arrival airport : 3-letter IATA airport code, e.g. HKG.
let fromDate = "fromDate_example"; // String | Departure date in the local time of the departure airport. Based on LAT (Latest Acceptance Time). format : yyyy-MM-dd eg : 2017-07-15
let productCode = "productCode_example"; // String | Product code for requested service and specials : 3-letter eg: YNZ
let accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
apiInstance.cargoGetRouteFromDateProductCodeByOriginAndDestinationGet(origin, destination, fromDate, productCode, accept, (error, data, response) => {
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
 **origin** | **String**| Departure Airport : 3-letter IATA airport code, e.g. FRA. | 
 **destination** | **String**| Arrival airport : 3-letter IATA airport code, e.g. HKG. | 
 **fromDate** | **String**| Departure date in the local time of the departure airport. Based on LAT (Latest Acceptance Time). format : yyyy-MM-dd eg : 2017-07-15 | 
 **productCode** | **String**| Product code for requested service and specials : 3-letter eg: YNZ | 
 **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | 

### Return type

**Object**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cargoShipmentTrackingByAWBPrefixAndAWBNumberGet

> Object cargoShipmentTrackingByAWBPrefixAndAWBNumberGet(aWBPrefix, aWBNumber, accept)

Shipment Tracking

With this tracking service you can easily retrieve your shipment or flight status information.

### Example

```javascript
import LhPublicApi from 'lh_public_api';
let defaultClient = LhPublicApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: auth
let auth = defaultClient.authentications['auth'];
auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LhPublicApi.CargoApi();
let aWBPrefix = "aWBPrefix_example"; // String | aWBPrefix : Represents the airline that is the owner of this AWB, i.e. \"020\" = Lufthansa Cargo, format : [0-9]{3} e.g. 020
let aWBNumber = "aWBNumber_example"; // String | aWBNumber : The Air Waybill Number , format : [0-9]{8} e.g. 08002050
let accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
apiInstance.cargoShipmentTrackingByAWBPrefixAndAWBNumberGet(aWBPrefix, aWBNumber, accept, (error, data, response) => {
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
 **aWBPrefix** | **String**| aWBPrefix : Represents the airline that is the owner of this AWB, i.e. \&quot;020\&quot; &#x3D; Lufthansa Cargo, format : [0-9]{3} e.g. 020 | 
 **aWBNumber** | **String**| aWBNumber : The Air Waybill Number , format : [0-9]{8} e.g. 08002050 | 
 **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | 

### Return type

**Object**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

