# CargoApi

All URIs are relative to *https://api.lufthansa.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cargoGetRouteFromDateProductCodeByOriginAndDestinationGet**](CargoApi.md#cargoGetRouteFromDateProductCodeByOriginAndDestinationGet) | **GET** /cargo/getRoute/{origin}-{destination}/{fromDate}/{productCode} | Retrieve all flights |
| [**cargoShipmentTrackingByAWBPrefixAndAWBNumberGet**](CargoApi.md#cargoShipmentTrackingByAWBPrefixAndAWBNumberGet) | **GET** /cargo/shipmentTracking/{aWBPrefix}-{aWBNumber} | Shipment Tracking |


<a id="cargoGetRouteFromDateProductCodeByOriginAndDestinationGet"></a>
# **cargoGetRouteFromDateProductCodeByOriginAndDestinationGet**
> Object cargoGetRouteFromDateProductCodeByOriginAndDestinationGet(origin, destination, fromDate, productCode, accept)

Retrieve all flights

Retrieve a list of all possible flights (both direct and connecting) between two airports on a given date. Routes are available for today and up to days in the future.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CargoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.lufthansa.com/v1");
    
    // Configure OAuth2 access token for authorization: auth
    OAuth auth = (OAuth) defaultClient.getAuthentication("auth");
    auth.setAccessToken("YOUR ACCESS TOKEN");

    CargoApi apiInstance = new CargoApi(defaultClient);
    String origin = "origin_example"; // String | Departure Airport : 3-letter IATA airport code, e.g. FRA.
    String destination = "destination_example"; // String | Arrival airport : 3-letter IATA airport code, e.g. HKG.
    String fromDate = "fromDate_example"; // String | Departure date in the local time of the departure airport. Based on LAT (Latest Acceptance Time). format : yyyy-MM-dd eg : 2017-07-15
    String productCode = "FAN"; // String | Product code for requested service and specials : 3-letter eg: YNZ
    String accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
    try {
      Object result = apiInstance.cargoGetRouteFromDateProductCodeByOriginAndDestinationGet(origin, destination, fromDate, productCode, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CargoApi#cargoGetRouteFromDateProductCodeByOriginAndDestinationGet");
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
| **origin** | **String**| Departure Airport : 3-letter IATA airport code, e.g. FRA. | |
| **destination** | **String**| Arrival airport : 3-letter IATA airport code, e.g. HKG. | |
| **fromDate** | **String**| Departure date in the local time of the departure airport. Based on LAT (Latest Acceptance Time). format : yyyy-MM-dd eg : 2017-07-15 | |
| **productCode** | **String**| Product code for requested service and specials : 3-letter eg: YNZ | [enum: FAN, FCO, FCP, FDG, FTF, FUN, FWN, YCO, YCP, YDG, YNB, YNZ, YTF, YUN, ZXB, ZXF, ZXR] |
| **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | |

### Return type

**Object**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="cargoShipmentTrackingByAWBPrefixAndAWBNumberGet"></a>
# **cargoShipmentTrackingByAWBPrefixAndAWBNumberGet**
> Object cargoShipmentTrackingByAWBPrefixAndAWBNumberGet(aWBPrefix, aWBNumber, accept)

Shipment Tracking

With this tracking service you can easily retrieve your shipment or flight status information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CargoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.lufthansa.com/v1");
    
    // Configure OAuth2 access token for authorization: auth
    OAuth auth = (OAuth) defaultClient.getAuthentication("auth");
    auth.setAccessToken("YOUR ACCESS TOKEN");

    CargoApi apiInstance = new CargoApi(defaultClient);
    String aWBPrefix = "aWBPrefix_example"; // String | aWBPrefix : Represents the airline that is the owner of this AWB, i.e. \"020\" = Lufthansa Cargo, format : [0-9]{3} e.g. 020
    String aWBNumber = "aWBNumber_example"; // String | aWBNumber : The Air Waybill Number , format : [0-9]{8} e.g. 08002050
    String accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
    try {
      Object result = apiInstance.cargoShipmentTrackingByAWBPrefixAndAWBNumberGet(aWBPrefix, aWBNumber, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CargoApi#cargoShipmentTrackingByAWBPrefixAndAWBNumberGet");
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
| **aWBPrefix** | **String**| aWBPrefix : Represents the airline that is the owner of this AWB, i.e. \&quot;020\&quot; &#x3D; Lufthansa Cargo, format : [0-9]{3} e.g. 020 | |
| **aWBNumber** | **String**| aWBNumber : The Air Waybill Number , format : [0-9]{8} e.g. 08002050 | |
| **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | |

### Return type

**Object**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

