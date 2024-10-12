# VehicleApi

All URIs are relative to *https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getVehicleDetailsByRegistrationNumber**](VehicleApi.md#getVehicleDetailsByRegistrationNumber) | **POST** /v1/vehicles | Get vehicle details by registration number |


<a id="getVehicleDetailsByRegistrationNumber"></a>
# **getVehicleDetailsByRegistrationNumber**
> Vehicle getVehicleDetailsByRegistrationNumber(xApiKey, vehicleRequest, xCorrelationId)

Get vehicle details by registration number

Returns vehicle details based on registration number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VehicleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry");

    VehicleApi apiInstance = new VehicleApi(defaultClient);
    String xApiKey = "xApiKey_example"; // String | Client Specific API Key
    VehicleRequest vehicleRequest = new VehicleRequest(); // VehicleRequest | Registration number of the vehicle to find details for
    String xCorrelationId = "xCorrelationId_example"; // String | Consumer Correlation ID
    try {
      Vehicle result = apiInstance.getVehicleDetailsByRegistrationNumber(xApiKey, vehicleRequest, xCorrelationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VehicleApi#getVehicleDetailsByRegistrationNumber");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xApiKey** | **String**| Client Specific API Key | |
| **vehicleRequest** | [**VehicleRequest**](VehicleRequest.md)| Registration number of the vehicle to find details for | |
| **xCorrelationId** | **String**| Consumer Correlation ID | [optional] |

### Return type

[**Vehicle**](Vehicle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **400** | Bad Request |  -  |
| **404** | Vehicle Not Found |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

