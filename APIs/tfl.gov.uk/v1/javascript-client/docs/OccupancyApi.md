# TransportForLondonUnifiedApi.OccupancyApi

All URIs are relative to *https://api.digital.tfl.gov.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**occupancyCarParkGet**](OccupancyApi.md#occupancyCarParkGet) | **GET** /Occupancy/CarPark | Gets the occupancy for all car parks that have occupancy data
[**occupancyGet**](OccupancyApi.md#occupancyGet) | **GET** /Occupancy/CarPark/{id} | Gets the occupancy for a car park with a given id
[**occupancyGetAllChargeConnectorStatus**](OccupancyApi.md#occupancyGetAllChargeConnectorStatus) | **GET** /Occupancy/ChargeConnector | Gets the occupancy for all charge connectors
[**occupancyGetBikePointsOccupancies**](OccupancyApi.md#occupancyGetBikePointsOccupancies) | **GET** /Occupancy/BikePoints/{ids} | Get the occupancy for bike points.
[**occupancyGetChargeConnectorStatus**](OccupancyApi.md#occupancyGetChargeConnectorStatus) | **GET** /Occupancy/ChargeConnector/{ids} | Gets the occupancy for a charge connectors with a given id (sourceSystemPlaceId)



## occupancyCarParkGet

> [TflApiPresentationEntitiesCarParkOccupancy] occupancyCarParkGet()

Gets the occupancy for all car parks that have occupancy data

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.OccupancyApi();
apiInstance.occupancyCarParkGet((error, data, response) => {
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

[**[TflApiPresentationEntitiesCarParkOccupancy]**](TflApiPresentationEntitiesCarParkOccupancy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## occupancyGet

> TflApiPresentationEntitiesCarParkOccupancy occupancyGet(id)

Gets the occupancy for a car park with a given id

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.OccupancyApi();
let id = "id_example"; // String | 
apiInstance.occupancyGet(id, (error, data, response) => {
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

[**TflApiPresentationEntitiesCarParkOccupancy**](TflApiPresentationEntitiesCarParkOccupancy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## occupancyGetAllChargeConnectorStatus

> [TflApiPresentationEntitiesChargeConnectorOccupancy] occupancyGetAllChargeConnectorStatus()

Gets the occupancy for all charge connectors

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.OccupancyApi();
apiInstance.occupancyGetAllChargeConnectorStatus((error, data, response) => {
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

[**[TflApiPresentationEntitiesChargeConnectorOccupancy]**](TflApiPresentationEntitiesChargeConnectorOccupancy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## occupancyGetBikePointsOccupancies

> [TflApiPresentationEntitiesBikePointOccupancy] occupancyGetBikePointsOccupancies(ids)

Get the occupancy for bike points.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.OccupancyApi();
let ids = ["null"]; // [String] | 
apiInstance.occupancyGetBikePointsOccupancies(ids, (error, data, response) => {
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
 **ids** | [**[String]**](String.md)|  | 

### Return type

[**[TflApiPresentationEntitiesBikePointOccupancy]**](TflApiPresentationEntitiesBikePointOccupancy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## occupancyGetChargeConnectorStatus

> [TflApiPresentationEntitiesChargeConnectorOccupancy] occupancyGetChargeConnectorStatus(ids)

Gets the occupancy for a charge connectors with a given id (sourceSystemPlaceId)

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.OccupancyApi();
let ids = ["null"]; // [String] | 
apiInstance.occupancyGetChargeConnectorStatus(ids, (error, data, response) => {
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
 **ids** | [**[String]**](String.md)|  | 

### Return type

[**[TflApiPresentationEntitiesChargeConnectorOccupancy]**](TflApiPresentationEntitiesChargeConnectorOccupancy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

