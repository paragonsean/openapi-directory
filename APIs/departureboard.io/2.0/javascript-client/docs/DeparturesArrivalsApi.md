# DepartureboardIoApi.DeparturesArrivalsApi

All URIs are relative to *https://api.departureboard.io/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getArrivalsAndDeparturesByCRS**](DeparturesArrivalsApi.md#getArrivalsAndDeparturesByCRS) | **GET** /getArrivalsAndDeparturesByCRS/{CRS} | getArrivalsAndDeparturesByCRS is used to get a list of services arriving to and departing from a UK train station by the CRS (Computer Reservation System) code. This will typically return a list of train services, but will also return any replacement bus or ferry services that are in place.
[**getArrivalsByCRS**](DeparturesArrivalsApi.md#getArrivalsByCRS) | **GET** /getArrivalsByCRS/{CRS} | getArrivalsByCRS is used to get a list of services arriving to a UK train station by the CRS (Computer Reservation System) code. This will typically return a list of train services, but will also return any replacement bus or ferry services that are in place.
[**getDeparturesByCRS**](DeparturesArrivalsApi.md#getDeparturesByCRS) | **GET** /getDeparturesByCRS/{CRS} | getDeparturesByCRS is used to get a list of services departing from a UK train station by the CRS (Computer Reservation System) code. This will typically return a list of train services, but will also return any replacement bus or ferry services that are in place.



## getArrivalsAndDeparturesByCRS

> getArrivalsAndDeparturesByCRS(CRS, apiKey, opts)

getArrivalsAndDeparturesByCRS is used to get a list of services arriving to and departing from a UK train station by the CRS (Computer Reservation System) code. This will typically return a list of train services, but will also return any replacement bus or ferry services that are in place.

### Example

```javascript
import DepartureboardIoApi from 'departureboard_io_api';

let apiInstance = new DepartureboardIoApi.DeparturesArrivalsApi();
let CRS = "CRS_example"; // String | The CRS (Computer Reservation System) for the Station you wish to get departure and arrival information for, e.g. KGX for London Kings Cross.
let apiKey = "apiKey_example"; // String | The National Rail OpenLDBWS API Key to use for looking up service information. You must register with National Rail to obtain this key and whitelist it with us. See https://api.departureboard.io/docs/registration for more information.
let opts = {
  'numServices': 10, // Number | The number of arriving and departing services to return. This is a maximum value, less may be returned if there is not a sufficient amount of services arriving to or departing from this station within the time window specified.
  'timeOffset': 0, // Number | The time window in minutes to offset the arrival and departure information by. For example, a value of 20 will not show services arriving to or departing from the station within the next 20 minutes.
  'timeWindow': 120, // Number | The time window in minutes to offset the arrival and departure information by. For example, a value of 20 will not show services arriving to or departing from the selected station within the next 20 minutes.
  'serviceDetails': true, // Boolean | Should the response contain information on the calling points for each service? If set to false, calling points will not be returned.
  'filterStation': "filterStation_example", // String | The CRS (Computer Reservation System) code to filter the results by. When setting this you must also set the filterType parameter. For example, performing a lookup for PAD (London Paddington) and setting filterStation to RED (Reading) and filterType to from, will only show services arriving to London Paddington that stopped at Reading. Setting a filter for getArrivalsAndDeparturesByCRS is similar to performing a getArrivalsByCRS or getDeparturesByCRS lookup, with the appropriate filterStation parameter. However using the getArrivalsAndDeparturesByCRS endpoint shows more details for each of the returned services.
  'filterType': "filterType_example" // String | Determines if the filterStation parameter should be applied for services arriving to, or leaving from the selected station. Required if filterStation is set.
};
apiInstance.getArrivalsAndDeparturesByCRS(CRS, apiKey, opts, (error, data, response) => {
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
 **CRS** | **String**| The CRS (Computer Reservation System) for the Station you wish to get departure and arrival information for, e.g. KGX for London Kings Cross. | 
 **apiKey** | **String**| The National Rail OpenLDBWS API Key to use for looking up service information. You must register with National Rail to obtain this key and whitelist it with us. See https://api.departureboard.io/docs/registration for more information. | 
 **numServices** | **Number**| The number of arriving and departing services to return. This is a maximum value, less may be returned if there is not a sufficient amount of services arriving to or departing from this station within the time window specified. | [optional] [default to 10]
 **timeOffset** | **Number**| The time window in minutes to offset the arrival and departure information by. For example, a value of 20 will not show services arriving to or departing from the station within the next 20 minutes. | [optional] [default to 0]
 **timeWindow** | **Number**| The time window in minutes to offset the arrival and departure information by. For example, a value of 20 will not show services arriving to or departing from the selected station within the next 20 minutes. | [optional] [default to 120]
 **serviceDetails** | **Boolean**| Should the response contain information on the calling points for each service? If set to false, calling points will not be returned. | [optional] [default to true]
 **filterStation** | **String**| The CRS (Computer Reservation System) code to filter the results by. When setting this you must also set the filterType parameter. For example, performing a lookup for PAD (London Paddington) and setting filterStation to RED (Reading) and filterType to from, will only show services arriving to London Paddington that stopped at Reading. Setting a filter for getArrivalsAndDeparturesByCRS is similar to performing a getArrivalsByCRS or getDeparturesByCRS lookup, with the appropriate filterStation parameter. However using the getArrivalsAndDeparturesByCRS endpoint shows more details for each of the returned services. | [optional] 
 **filterType** | **String**| Determines if the filterStation parameter should be applied for services arriving to, or leaving from the selected station. Required if filterStation is set. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getArrivalsByCRS

> getArrivalsByCRS(CRS, apiKey, opts)

getArrivalsByCRS is used to get a list of services arriving to a UK train station by the CRS (Computer Reservation System) code. This will typically return a list of train services, but will also return any replacement bus or ferry services that are in place.

### Example

```javascript
import DepartureboardIoApi from 'departureboard_io_api';

let apiInstance = new DepartureboardIoApi.DeparturesArrivalsApi();
let CRS = "CRS_example"; // String | The CRS (Computer Reservation System) for the Station you wish to get arrival information for, e.g. KGX for London Kings Cross.
let apiKey = "apiKey_example"; // String | The National Rail OpenLDBWS API Key to use for looking up service information. You must register with National Rail to obtain this key and whitelist it with us. See https://api.departureboard.io/docs/registration for more information.
let opts = {
  'numServices': 10, // Number | The number of arriving train services to return. This is a maximum value, less may be returned if there is not a sufficient amount of services running to this station within the time window specified.
  'timeOffset': 0, // Number | The time window in minutes to offset the arrival information by. For example, a value of 20 will not show services arriving within the next 20 minutes.
  'timeWindow': 120, // Number | The time window to show train services for in minutes. For example, a value of 60 will show services arriving to the station in the next 60 minutes.
  'serviceDetails': true, // Boolean | Should the response contain information on the calling points for each service? If set to false, calling points will not be returned.
  'filterStation': "filterStation_example" // String | The CRS (Computer Reservation System) code to filter the results by. For example, performing a lookup for PAD (London Paddington) and setting filterStation to RED (Reading), will only show services arriving to Paddington that stopped at Reading.
};
apiInstance.getArrivalsByCRS(CRS, apiKey, opts, (error, data, response) => {
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
 **CRS** | **String**| The CRS (Computer Reservation System) for the Station you wish to get arrival information for, e.g. KGX for London Kings Cross. | 
 **apiKey** | **String**| The National Rail OpenLDBWS API Key to use for looking up service information. You must register with National Rail to obtain this key and whitelist it with us. See https://api.departureboard.io/docs/registration for more information. | 
 **numServices** | **Number**| The number of arriving train services to return. This is a maximum value, less may be returned if there is not a sufficient amount of services running to this station within the time window specified. | [optional] [default to 10]
 **timeOffset** | **Number**| The time window in minutes to offset the arrival information by. For example, a value of 20 will not show services arriving within the next 20 minutes. | [optional] [default to 0]
 **timeWindow** | **Number**| The time window to show train services for in minutes. For example, a value of 60 will show services arriving to the station in the next 60 minutes. | [optional] [default to 120]
 **serviceDetails** | **Boolean**| Should the response contain information on the calling points for each service? If set to false, calling points will not be returned. | [optional] [default to true]
 **filterStation** | **String**| The CRS (Computer Reservation System) code to filter the results by. For example, performing a lookup for PAD (London Paddington) and setting filterStation to RED (Reading), will only show services arriving to Paddington that stopped at Reading. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDeparturesByCRS

> getDeparturesByCRS(CRS, apiKey, opts)

getDeparturesByCRS is used to get a list of services departing from a UK train station by the CRS (Computer Reservation System) code. This will typically return a list of train services, but will also return any replacement bus or ferry services that are in place.

### Example

```javascript
import DepartureboardIoApi from 'departureboard_io_api';

let apiInstance = new DepartureboardIoApi.DeparturesArrivalsApi();
let CRS = "CRS_example"; // String | The CRS (Computer Reservation System) for the station you wish to get departure information for, e.g. KGX for London Kings Cross.
let apiKey = "apiKey_example"; // String | The National Rail OpenLDBWS API Key to use for looking up service information. You must register with National Rail to obtain this key and whitelist it with us. See https://api.departureboard.io/docs/registration for more information.
let opts = {
  'numServices': 10, // Number | The number of departing services to return. This is a maximum value, less may be returned if there is not a sufficient amount of services running from the selected station within the time window specified.
  'timeOffset': 0, // Number | The time window in minutes to offset the departure information by. For example, a value of 20 will not show services departing within the next 20 minutes.
  'timeWindow': 120, // Number | The time window to show services for in minutes. For example, a value of 60 will show services departing the station in the next 60 minutes.
  'serviceDetails': true, // Boolean | Should the response contain information on the calling points for each service? If set to false, calling points will not be returned.
  'filterStation': "filterStation_example" // String | The CRS (Computer Reservation System) code to filter the results by. For example, performing a lookup for PAD (London Paddington) and setting filterStation to RED (Reading), will only show services departing from Paddington that stop at Reading.
};
apiInstance.getDeparturesByCRS(CRS, apiKey, opts, (error, data, response) => {
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
 **CRS** | **String**| The CRS (Computer Reservation System) for the station you wish to get departure information for, e.g. KGX for London Kings Cross. | 
 **apiKey** | **String**| The National Rail OpenLDBWS API Key to use for looking up service information. You must register with National Rail to obtain this key and whitelist it with us. See https://api.departureboard.io/docs/registration for more information. | 
 **numServices** | **Number**| The number of departing services to return. This is a maximum value, less may be returned if there is not a sufficient amount of services running from the selected station within the time window specified. | [optional] [default to 10]
 **timeOffset** | **Number**| The time window in minutes to offset the departure information by. For example, a value of 20 will not show services departing within the next 20 minutes. | [optional] [default to 0]
 **timeWindow** | **Number**| The time window to show services for in minutes. For example, a value of 60 will show services departing the station in the next 60 minutes. | [optional] [default to 120]
 **serviceDetails** | **Boolean**| Should the response contain information on the calling points for each service? If set to false, calling points will not be returned. | [optional] [default to true]
 **filterStation** | **String**| The CRS (Computer Reservation System) code to filter the results by. For example, performing a lookup for PAD (London Paddington) and setting filterStation to RED (Reading), will only show services departing from Paddington that stop at Reading. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

