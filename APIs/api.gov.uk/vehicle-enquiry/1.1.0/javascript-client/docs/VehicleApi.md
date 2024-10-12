# VehicleEnquiryApi.VehicleApi

All URIs are relative to *https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getVehicleDetailsByRegistrationNumber**](VehicleApi.md#getVehicleDetailsByRegistrationNumber) | **POST** /v1/vehicles | Get vehicle details by registration number



## getVehicleDetailsByRegistrationNumber

> Vehicle getVehicleDetailsByRegistrationNumber(xApiKey, vehicleRequest, opts)

Get vehicle details by registration number

Returns vehicle details based on registration number

### Example

```javascript
import VehicleEnquiryApi from 'vehicle_enquiry_api';

let apiInstance = new VehicleEnquiryApi.VehicleApi();
let xApiKey = "xApiKey_example"; // String | Client Specific API Key
let vehicleRequest = new VehicleEnquiryApi.VehicleRequest(); // VehicleRequest | Registration number of the vehicle to find details for
let opts = {
  'xCorrelationId': "xCorrelationId_example" // String | Consumer Correlation ID
};
apiInstance.getVehicleDetailsByRegistrationNumber(xApiKey, vehicleRequest, opts, (error, data, response) => {
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
 **xApiKey** | **String**| Client Specific API Key | 
 **vehicleRequest** | [**VehicleRequest**](VehicleRequest.md)| Registration number of the vehicle to find details for | 
 **xCorrelationId** | **String**| Consumer Correlation ID | [optional] 

### Return type

[**Vehicle**](Vehicle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

