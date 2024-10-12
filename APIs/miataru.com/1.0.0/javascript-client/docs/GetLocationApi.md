# Miataru.GetLocationApi

All URIs are relative to *http://service.miataru.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getLocation**](GetLocationApi.md#getLocation) | **POST** /GetLocation | 
[**getLocationGeoJSON**](GetLocationApi.md#getLocationGeoJSON) | **GET** /GetLocationGeoJSON/{deviceID} | 
[**getLocationHistory**](GetLocationApi.md#getLocationHistory) | **POST** /GetLocationHistory | 



## getLocation

> MiataruGetLocationResponse getLocation(body)



To retrieve a specific devices latest known location the /GetLocation method is used. Please note that the MiataruConfig portion is optional. RequestMiataruDeviceID should be the ID of the device the request is sent from (or an identifier like an URL).

### Example

```javascript
import Miataru from 'miataru';

let apiInstance = new Miataru.GetLocationApi();
let body = new Miataru.MiataruGetLocationRequest(); // MiataruGetLocationRequest | the complex JSON formatted datastructure to get the location of one or more devices.
apiInstance.getLocation(body, (error, data, response) => {
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
 **body** | [**MiataruGetLocationRequest**](MiataruGetLocationRequest.md)| the complex JSON formatted datastructure to get the location of one or more devices. | 

### Return type

[**MiataruGetLocationResponse**](MiataruGetLocationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getLocationGeoJSON

> MiataruGetLocationGeoJSONResponse getLocationGeoJSON(deviceID)



Retrieves a devices Location in GeoJSON format.

### Example

```javascript
import Miataru from 'miataru';

let apiInstance = new Miataru.GetLocationApi();
let deviceID = "'7b8e6e0ee5296db345162dc2ef652c1350761823'"; // String | the unique device ID of the device the location is requested from
apiInstance.getLocationGeoJSON(deviceID, (error, data, response) => {
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
 **deviceID** | **String**| the unique device ID of the device the location is requested from | [default to &#39;7b8e6e0ee5296db345162dc2ef652c1350761823&#39;]

### Return type

[**MiataruGetLocationGeoJSONResponse**](MiataruGetLocationGeoJSONResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLocationHistory

> MiataruGetLocationHistoryResponse getLocationHistory(body)



Location History is stored on the server only if the client told the server to do so using the “EnableLocationHistory” setting in the Location Update requests. For transitions of enabling/disabling that functionality - Everytime a Location Update is received by the server with “EnableLocationHistory&#x3D;false” the server removes all stored Location History till that point. There is a server-side setting that controls up to how many Location Updates the server is storing in the Location History before it removes the oldest one. To request the Location History of a particular device the client sends the following POST request to the GetLocationHistory service URL. Please note that the MiataruConfig portion is optional. RequestMiataruDeviceID should be the ID of the device the request is sent from (or an identifier like an URL).

### Example

```javascript
import Miataru from 'miataru';

let apiInstance = new Miataru.GetLocationApi();
let body = new Miataru.MiataruGetLocationHistoryRequest(); // MiataruGetLocationHistoryRequest | the complex JSON formatted datastructure to get the location history of one device
apiInstance.getLocationHistory(body, (error, data, response) => {
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
 **body** | [**MiataruGetLocationHistoryRequest**](MiataruGetLocationHistoryRequest.md)| the complex JSON formatted datastructure to get the location history of one device | 

### Return type

[**MiataruGetLocationHistoryResponse**](MiataruGetLocationHistoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

