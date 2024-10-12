# CloudRfApi.ManageApi

All URIs are relative to *https://api.cloudrf.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addClutter**](ManageApi.md#addClutter) | **POST** /clutter/add | Upload clutter data as GeoJSON
[**callDelete**](ManageApi.md#callDelete) | **GET** /archive/delete | Delete a calculation from the database.
[**callExport**](ManageApi.md#callExport) | **GET** /archive/export | Export a calculation in a GIS file format
[**deleteNetwork**](ManageApi.md#deleteNetwork) | **GET** /archive/delete/network | Delete an entire network
[**list**](ManageApi.md#list) | **GET** /archive/list | List calculations from your archive



## addClutter

> addClutter(addClutterRequest)

Upload clutter data as GeoJSON

Upload GeoJSON lineString and polygon features to your account. The height property is in metres and the material code / type / attenuation are.. 1 Trees – 0.25,2Trees + 0.5,3 Timber – 1.0,4 Timber + 1.5,5 Brick –  1.5,6 Brick + 2.0,7 Concrete – 3.0,8 Concrete + 4.0,9 Metal 6.0

### Example

```javascript
import CloudRfApi from 'cloud_rf_api';
let defaultClient = CloudRfApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CloudRfApi.ManageApi();
let addClutterRequest = new CloudRfApi.AddClutterRequest(); // AddClutterRequest | 
apiInstance.addClutter(addClutterRequest, (error, data, response) => {
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
 **addClutterRequest** | [**AddClutterRequest**](AddClutterRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## callDelete

> callDelete(cid)

Delete a calculation from the database.

Warning! you could lose data. This function will delete the entry from the database and the file from the disk. Accidental deletion can be reversed by contacting support with biscuits who maintain an offsite backup.

### Example

```javascript
import CloudRfApi from 'cloud_rf_api';
let defaultClient = CloudRfApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CloudRfApi.ManageApi();
let cid = 56; // Number | Unique calculation ID number
apiInstance.callDelete(cid, (error, data, response) => {
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
 **cid** | **Number**| Unique calculation ID number | 

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## callExport

> callExport(file, fmt)

Export a calculation in a GIS file format

Download your data in a format suitable for a third party viewer like Google Earth or ESRI Arcmap.

### Example

```javascript
import CloudRfApi from 'cloud_rf_api';
let defaultClient = CloudRfApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CloudRfApi.ManageApi();
let file = "file_example"; // String | Calculation file name
let fmt = "fmt_example"; // String | Raster/Vector file format: KML, KMZ, SHP, GeoTIFF
apiInstance.callExport(file, fmt, (error, data, response) => {
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
 **file** | **String**| Calculation file name | 
 **fmt** | **String**| Raster/Vector file format: KML, KMZ, SHP, GeoTIFF | 

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetwork

> deleteNetwork(nid)

Delete an entire network

Warning! you could lose data. This function will delete the entry from the database and the file from the disk. Accidental deletion can be reversed by contacting support with biscuits who maintain an offsite backup.

### Example

```javascript
import CloudRfApi from 'cloud_rf_api';
let defaultClient = CloudRfApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CloudRfApi.ManageApi();
let nid = "nid_example"; // String | Network name
apiInstance.deleteNetwork(nid, (error, data, response) => {
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
 **nid** | **String**| Network name | 

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## list

> list(opts)

List calculations from your archive

List your area and path calculations, sorted by time and limited to the last few hundred. To fetch all for a given network append a &#39;net&#39; filter with the network name.

### Example

```javascript
import CloudRfApi from 'cloud_rf_api';
let defaultClient = CloudRfApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CloudRfApi.ManageApi();
let opts = {
  'n': 3.4, // Number | North bounding box
  'e': 3.4, // Number | East bounding box
  's': 3.4, // Number | South bounding box
  'w': 3.4 // Number | West bounding box
};
apiInstance.list(opts, (error, data, response) => {
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
 **n** | **Number**| North bounding box | [optional] 
 **e** | **Number**| East bounding box | [optional] 
 **s** | **Number**| South bounding box | [optional] 
 **w** | **Number**| West bounding box | [optional] 

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

