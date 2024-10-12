# EDrvApi.ChargeStationsApi

All URIs are relative to *http://api.edrv.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteChargeStation**](ChargeStationsApi.md#deleteChargeStation) | **DELETE** /v1/chargestations/{id} | 
[**getChargeStation**](ChargeStationsApi.md#getChargeStation) | **GET** /v1/chargestations/{id} | 
[**getChargeStationConnectors**](ChargeStationsApi.md#getChargeStationConnectors) | **GET** /v1/chargestations/{id}/connectors | 
[**getChargeStations**](ChargeStationsApi.md#getChargeStations) | **GET** /v1/chargestations | 
[**patchChargeStation**](ChargeStationsApi.md#patchChargeStation) | **PATCH** /v1/chargestations/{id} | 
[**postChargeStations**](ChargeStationsApi.md#postChargeStations) | **POST** /v1/chargestations | 



## deleteChargeStation

> deleteChargeStation(id)



Use to delete a charge station

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.ChargeStationsApi();
let id = "id_example"; // String | The charge station id that needs to be deleted
apiInstance.deleteChargeStation(id, (error, data, response) => {
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
 **id** | **String**| The charge station id that needs to be deleted | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getChargeStation

> getChargeStation(id, opts)



Get a single charge station&#39;s data

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.ChargeStationsApi();
let id = "id_example"; // String | The charge station id that needs to be fetched
let opts = {
  'includeLocation': true, // Boolean | Populate location
  'includeEvses': true, // Boolean | Populate evses
  'includeOrganization': true // Boolean | Populate organization
};
apiInstance.getChargeStation(id, opts, (error, data, response) => {
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
 **id** | **String**| The charge station id that needs to be fetched | 
 **includeLocation** | **Boolean**| Populate location | [optional] 
 **includeEvses** | **Boolean**| Populate evses | [optional] 
 **includeOrganization** | **Boolean**| Populate organization | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getChargeStationConnectors

> getChargeStationConnectors(id, opts)



List connectors for a chargestation

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.ChargeStationsApi();
let id = "id_example"; // String | chargeStation id
let opts = {
  'includeEvse': true, // Boolean | Populate evse
  'includeOrganization': true // Boolean | Populate organization
};
apiInstance.getChargeStationConnectors(id, opts, (error, data, response) => {
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
 **id** | **String**| chargeStation id | 
 **includeEvse** | **Boolean**| Populate evse | [optional] 
 **includeOrganization** | **Boolean**| Populate organization | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getChargeStations

> getChargeStations(opts)



List all Chargestations

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.ChargeStationsApi();
let opts = {
  'organization': "organization_example", // String | Filter by Org. Id
  'location': "location_example", // String | Filter by Location Id
  'online': true, // Boolean | Filter by Online Status
  'active': true, // Boolean | Chargestations that have been activated/deactivated by the admin
  '_public': true, // Boolean | Chargestations that are public
  'paginateLimit': 20, // Number | Number of results per page
  'paginatePage': "paginatePage_example", // String | The queried page index
  'paginateEnabled': true, // Boolean | Enable pagination
  'sortBy': "'createdAt'", // String | Sort data by this key
  'sortOrder': "'desc'", // String | asc to sort ascending (default is desc - descending)
  'createdAtGte': new Date("2013-10-20T19:20:30+01:00"), // Date | Date as ISO String
  'createdAtLte': new Date("2013-10-20T19:20:30+01:00"), // Date | Date as ISO String
  'updatedAtGte': new Date("2013-10-20T19:20:30+01:00"), // Date | Date as ISO String
  'updatedAtLte': new Date("2013-10-20T19:20:30+01:00"), // Date | Date as ISO String
  'includeLocation': true, // Boolean | Populate location
  'includeEvses': true, // Boolean | Populate evses
  'includeOrganization': true // Boolean | Populate organization
};
apiInstance.getChargeStations(opts, (error, data, response) => {
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
 **organization** | **String**| Filter by Org. Id | [optional] 
 **location** | **String**| Filter by Location Id | [optional] 
 **online** | **Boolean**| Filter by Online Status | [optional] 
 **active** | **Boolean**| Chargestations that have been activated/deactivated by the admin | [optional] 
 **_public** | **Boolean**| Chargestations that are public | [optional] 
 **paginateLimit** | **Number**| Number of results per page | [optional] [default to 20]
 **paginatePage** | **String**| The queried page index | [optional] 
 **paginateEnabled** | **Boolean**| Enable pagination | [optional] [default to true]
 **sortBy** | **String**| Sort data by this key | [optional] [default to &#39;createdAt&#39;]
 **sortOrder** | **String**| asc to sort ascending (default is desc - descending) | [optional] [default to &#39;desc&#39;]
 **createdAtGte** | **Date**| Date as ISO String | [optional] 
 **createdAtLte** | **Date**| Date as ISO String | [optional] 
 **updatedAtGte** | **Date**| Date as ISO String | [optional] 
 **updatedAtLte** | **Date**| Date as ISO String | [optional] 
 **includeLocation** | **Boolean**| Populate location | [optional] 
 **includeEvses** | **Boolean**| Populate evses | [optional] 
 **includeOrganization** | **Boolean**| Populate organization | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## patchChargeStation

> PatchChargeStation200Response patchChargeStation(id, schema1)



Update a charge station&#39;s data

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.ChargeStationsApi();
let id = "id_example"; // String | ID of charge station that needs to be updated
let schema1 = new EDrvApi.Schema1(); // Schema1 | Include charge station properties to update here
apiInstance.patchChargeStation(id, schema1, (error, data, response) => {
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
 **id** | **String**| ID of charge station that needs to be updated | 
 **schema1** | [**Schema1**](Schema1.md)| Include charge station properties to update here | 

### Return type

[**PatchChargeStation200Response**](PatchChargeStation200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postChargeStations

> PostChargeStations201Response postChargeStations(schema1)



Create a new charge station

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.ChargeStationsApi();
let schema1 = new EDrvApi.Schema1(); // Schema1 | Include charge station properties to create here
apiInstance.postChargeStations(schema1, (error, data, response) => {
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
 **schema1** | [**Schema1**](Schema1.md)| Include charge station properties to create here | 

### Return type

[**PostChargeStations201Response**](PostChargeStations201Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

