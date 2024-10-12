# FaStaStationFacilitiesStatus.DefaultApi

All URIs are relative to *https://api.deutschebahn.com/fasta/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**findFacilities**](DefaultApi.md#findFacilities) | **GET** /facilities | 
[**findStationByStationNumber**](DefaultApi.md#findStationByStationNumber) | **GET** /stations/{stationnumber} | 
[**getFacilityByEquipmentNumber**](DefaultApi.md#getFacilityByEquipmentNumber) | **GET** /facilities/{equipmentnumber} | 



## findFacilities

> [Facility] findFacilities(opts)



Access to public facilities (escalators and elevators) in railway stations

### Example

```javascript
import FaStaStationFacilitiesStatus from 'fa_sta_station_facilities_status';
let defaultClient = FaStaStationFacilitiesStatus.ApiClient.instance;
// Configure API key authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//UserSecurity.apiKeyPrefix = 'Token';

let apiInstance = new FaStaStationFacilitiesStatus.DefaultApi();
let opts = {
  'type': ["null"], // [String] | Type of the facility.
  'state': ["null"], // [String] | Operational state of the facility.
  'equipmentnumbers': [null], // [Number] | List of equipmentnumbers to select.
  'stationnumber': 789, // Number | Number of the station the facilities belong to.
  'area': ["null"] // [String] | Geo coordinate rectangle in WGS84-format to filter facilities by geographical position. Parameters must be 4 numbers exactly as follows: longitudeWest, latitudeSouth, longitudeEast, latitudeNorth.
};
apiInstance.findFacilities(opts, (error, data, response) => {
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
 **type** | [**[String]**](String.md)| Type of the facility. | [optional] 
 **state** | [**[String]**](String.md)| Operational state of the facility. | [optional] 
 **equipmentnumbers** | [**[Number]**](Number.md)| List of equipmentnumbers to select. | [optional] 
 **stationnumber** | **Number**| Number of the station the facilities belong to. | [optional] 
 **area** | [**[String]**](String.md)| Geo coordinate rectangle in WGS84-format to filter facilities by geographical position. Parameters must be 4 numbers exactly as follows: longitudeWest, latitudeSouth, longitudeEast, latitudeNorth. | [optional] 

### Return type

[**[Facility]**](Facility.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findStationByStationNumber

> Station findStationByStationNumber(stationnumber)



Returns information about a station (and its corresponding facilities) identified by a stationnumber.

### Example

```javascript
import FaStaStationFacilitiesStatus from 'fa_sta_station_facilities_status';
let defaultClient = FaStaStationFacilitiesStatus.ApiClient.instance;
// Configure API key authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//UserSecurity.apiKeyPrefix = 'Token';

let apiInstance = new FaStaStationFacilitiesStatus.DefaultApi();
let stationnumber = 789; // Number | Number of the station to fetch.
apiInstance.findStationByStationNumber(stationnumber, (error, data, response) => {
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
 **stationnumber** | **Number**| Number of the station to fetch. | 

### Return type

[**Station**](Station.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFacilityByEquipmentNumber

> Facility getFacilityByEquipmentNumber(equipmentnumber)



Returns the facility identified by its equipmentnumber.

### Example

```javascript
import FaStaStationFacilitiesStatus from 'fa_sta_station_facilities_status';
let defaultClient = FaStaStationFacilitiesStatus.ApiClient.instance;
// Configure API key authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//UserSecurity.apiKeyPrefix = 'Token';

let apiInstance = new FaStaStationFacilitiesStatus.DefaultApi();
let equipmentnumber = 789; // Number | Equipmentnumber of the facility to fetch.
apiInstance.getFacilityByEquipmentNumber(equipmentnumber, (error, data, response) => {
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
 **equipmentnumber** | **Number**| Equipmentnumber of the facility to fetch. | 

### Return type

[**Facility**](Facility.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

