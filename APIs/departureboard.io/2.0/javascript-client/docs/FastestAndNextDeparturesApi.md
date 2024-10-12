# DepartureboardIoApi.FastestAndNextDeparturesApi

All URIs are relative to *https://api.departureboard.io/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getFastestDeparturesByCRS**](FastestAndNextDeparturesApi.md#getFastestDeparturesByCRS) | **GET** /getFastestDeparturesByCRS/{CRS} | getFastestDeparturesByCRS is used to get the fastest next service running between two stations. Multiple destinations can be specified. This will typically return a single train service, but will also return a replacement bus or ferry service if in place.
[**getNextDeparturesByCRS**](FastestAndNextDeparturesApi.md#getNextDeparturesByCRS) | **GET** /getNextDeparturesByCRS/{CRS} | getNextDeparturesByCRS is used to get the next service running between two stations. Multiple destinations can be specified. This will typically return a single train service, but will also return a replacement bus or ferry service if in place. This will return the next departures for each of the filterList stations specified. It may not return the fastest next service. To get the fastest next service use the getFastestDeparturesByCRS endpoint.



## getFastestDeparturesByCRS

> getFastestDeparturesByCRS(CRS, apiKey, filterList, opts)

getFastestDeparturesByCRS is used to get the fastest next service running between two stations. Multiple destinations can be specified. This will typically return a single train service, but will also return a replacement bus or ferry service if in place.

### Example

```javascript
import DepartureboardIoApi from 'departureboard_io_api';

let apiInstance = new DepartureboardIoApi.FastestAndNextDeparturesApi();
let CRS = "CRS_example"; // String | The CRS (Computer Reservation System) for the station you wish to get departure information for, e.g. KGX for London Kings Cross.
let apiKey = "apiKey_example"; // String | The National Rail OpenLDBWS API Key to use for looking up service information. You must register with National Rail to obtain this key and whitelist it with us. See https://api.departureboard.io/docs/registration for more information.
let filterList = "filterList_example"; // String | The CRS (Computer Reservation System) codes to show the fastest departing services to. Up to 20 destination stations can be specified. These should be split by a comma, for example HAY,EAL,PAD.
let opts = {
  'timeOffset': 0, // Number | The time window in minutes to offset the departure information by. For example, a value of 20 will show the fastest services departing after 20 minutes.
  'timeWindow': 120, // Number | The time window to show train services for in minutes. For example, a value of 60 will show the fastest services departing the station in the next 60 minutes.
  'serviceDetails': true // Boolean | Should the response contain information on the calling points for each service? If set to false, calling points will not be returned.
};
apiInstance.getFastestDeparturesByCRS(CRS, apiKey, filterList, opts, (error, data, response) => {
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
 **filterList** | **String**| The CRS (Computer Reservation System) codes to show the fastest departing services to. Up to 20 destination stations can be specified. These should be split by a comma, for example HAY,EAL,PAD. | 
 **timeOffset** | **Number**| The time window in minutes to offset the departure information by. For example, a value of 20 will show the fastest services departing after 20 minutes. | [optional] [default to 0]
 **timeWindow** | **Number**| The time window to show train services for in minutes. For example, a value of 60 will show the fastest services departing the station in the next 60 minutes. | [optional] [default to 120]
 **serviceDetails** | **Boolean**| Should the response contain information on the calling points for each service? If set to false, calling points will not be returned. | [optional] [default to true]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNextDeparturesByCRS

> getNextDeparturesByCRS(CRS, apiKey, filterList, opts)

getNextDeparturesByCRS is used to get the next service running between two stations. Multiple destinations can be specified. This will typically return a single train service, but will also return a replacement bus or ferry service if in place. This will return the next departures for each of the filterList stations specified. It may not return the fastest next service. To get the fastest next service use the getFastestDeparturesByCRS endpoint.

### Example

```javascript
import DepartureboardIoApi from 'departureboard_io_api';

let apiInstance = new DepartureboardIoApi.FastestAndNextDeparturesApi();
let CRS = "CRS_example"; // String | The CRS (Computer Reservation System) for the station you wish to get departure information for, e.g. KGX for London Kings Cross.
let apiKey = "apiKey_example"; // String | The National Rail OpenLDBWS API Key to use for looking up service information. You must register with National Rail to obtain this key and whitelist it with us. See https://api.departureboard.io/docs/registration for more information.
let filterList = "filterList_example"; // String | The CRS (Computer Reservation System) codes to show departing services to. Up to 20 destination stations can be specified. These should be split by a comma, for example HAY,EAL,PAD.
let opts = {
  'timeOffset': 0, // Number | The time window in minutes to offset the arrival and departure information by. For example, a value of 20 will not show services arriving to or departing from the station within the next 20 minutes.
  'timeWindow': 120, // Number | The time window in minutes to offset the arrival and departure information by. For example, a value of 20 will not show services arriving to or departing from the selected station within the next 20 minutes.
  'serviceDetails': true // Boolean | Should the response contain information on the calling points for each service? If set to false, calling points will not be returned.
};
apiInstance.getNextDeparturesByCRS(CRS, apiKey, filterList, opts, (error, data, response) => {
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
 **filterList** | **String**| The CRS (Computer Reservation System) codes to show departing services to. Up to 20 destination stations can be specified. These should be split by a comma, for example HAY,EAL,PAD. | 
 **timeOffset** | **Number**| The time window in minutes to offset the arrival and departure information by. For example, a value of 20 will not show services arriving to or departing from the station within the next 20 minutes. | [optional] [default to 0]
 **timeWindow** | **Number**| The time window in minutes to offset the arrival and departure information by. For example, a value of 20 will not show services arriving to or departing from the selected station within the next 20 minutes. | [optional] [default to 120]
 **serviceDetails** | **Boolean**| Should the response contain information on the calling points for each service? If set to false, calling points will not be returned. | [optional] [default to true]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

