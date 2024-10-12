# DepartureboardIoApi.ServiceInformationApi

All URIs are relative to *https://api.departureboard.io/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getServiceDetailsByID**](ServiceInformationApi.md#getServiceDetailsByID) | **GET** /getServiceDetailsByID/{serviceID} | getServiceDetailsByID is used to get information on a service, by the Service ID. This will typically return a train service, but will also return a bus and ferry services. The Service ID must be provided in the serviceIDUrlSafe format that is provided in the response for Arrival and Departure Boards. A service ID is specific to a station, and can only be looked up for a short time after a train/bus/ferry arrives at, or departs from a station. This is a National Rail limitation.



## getServiceDetailsByID

> getServiceDetailsByID(serviceID, apiKey)

getServiceDetailsByID is used to get information on a service, by the Service ID. This will typically return a train service, but will also return a bus and ferry services. The Service ID must be provided in the serviceIDUrlSafe format that is provided in the response for Arrival and Departure Boards. A service ID is specific to a station, and can only be looked up for a short time after a train/bus/ferry arrives at, or departs from a station. This is a National Rail limitation.

### Example

```javascript
import DepartureboardIoApi from 'departureboard_io_api';

let apiInstance = new DepartureboardIoApi.ServiceInformationApi();
let serviceID = "serviceID_example"; // String | The Service ID for the Train Service you wish to look up in the URL Safe format. For example \"qsec4O8LW7k8ITcOt_ir4Q--\".
let apiKey = "apiKey_example"; // String | The National Rail OpenLDBWS API Key to use for looking up service information. You must register with National Rail to obtain this key and whitelist it with us. See https://api.departureboard.io/docs/registration for more information.
apiInstance.getServiceDetailsByID(serviceID, apiKey, (error, data, response) => {
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
 **serviceID** | **String**| The Service ID for the Train Service you wish to look up in the URL Safe format. For example \&quot;qsec4O8LW7k8ITcOt_ir4Q--\&quot;. | 
 **apiKey** | **String**| The National Rail OpenLDBWS API Key to use for looking up service information. You must register with National Rail to obtain this key and whitelist it with us. See https://api.departureboard.io/docs/registration for more information. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

