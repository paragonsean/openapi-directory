# TheWaterLinkedUnderwaterGpsApi.PoiApi

All URIs are relative to *http://demo.waterlinked.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**poiCreate**](PoiApi.md#poiCreate) | **POST** /api/v1/poi/ | Create poi
[**poiDelete**](PoiApi.md#poiDelete) | **DELETE** /api/v1/poi/{ID} | Delete poi
[**poiList**](PoiApi.md#poiList) | **GET** /api/v1/poi/ | List poi
[**poiShow**](PoiApi.md#poiShow) | **GET** /api/v1/poi/{ID} | Show poi
[**poiUpdate**](PoiApi.md#poiUpdate) | **PATCH** /api/v1/poi/{ID} | Update poi



## poiCreate

> poiCreate(payload)

Create poi

Create a new POI

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.PoiApi();
let payload = new TheWaterLinkedUnderwaterGpsApi.CreatePoiPayload(); // CreatePoiPayload | A list of all POI
apiInstance.poiCreate(payload, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**CreatePoiPayload**](CreatePoiPayload.md)| A list of all POI | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.goa.error


## poiDelete

> poiDelete(ID)

Delete poi

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.PoiApi();
let ID = 56; // Number | 
apiInstance.poiDelete(ID, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ID** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.goa.error


## poiList

> [WaterlinkedPoi] poiList()

List poi

List all points of interest

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.PoiApi();
apiInstance.poiList((error, data, response) => {
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

[**[WaterlinkedPoi]**](WaterlinkedPoi.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.waterlinked.poi+json; type=collection


## poiShow

> WaterlinkedPoi poiShow(ID)

Show poi

Get a POI

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.PoiApi();
let ID = 56; // Number | 
apiInstance.poiShow(ID, (error, data, response) => {
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
 **ID** | **Number**|  | 

### Return type

[**WaterlinkedPoi**](WaterlinkedPoi.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.waterlinked.poi+json


## poiUpdate

> poiUpdate(ID, payload)

Update poi

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.PoiApi();
let ID = 56; // Number | 
let payload = new TheWaterLinkedUnderwaterGpsApi.UpdatePoiPayload(); // UpdatePoiPayload | A list of all POI
apiInstance.poiUpdate(ID, payload, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ID** | **Number**|  | 
 **payload** | [**UpdatePoiPayload**](UpdatePoiPayload.md)| A list of all POI | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.goa.error

