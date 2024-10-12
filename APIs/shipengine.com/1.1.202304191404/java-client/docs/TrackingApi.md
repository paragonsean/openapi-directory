# TrackingApi

All URIs are relative to *https://api.shipengine.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getTrackingLog**](TrackingApi.md#getTrackingLog) | **GET** /v1/tracking | Get Tracking Information |
| [**startTracking**](TrackingApi.md#startTracking) | **POST** /v1/tracking/start | Start Tracking a Package |
| [**stopTracking**](TrackingApi.md#stopTracking) | **POST** /v1/tracking/stop | Stop Tracking a Package |


<a id="getTrackingLog"></a>
# **getTrackingLog**
> GetTrackingLogResponseBody getTrackingLog(carrierCode, trackingNumber)

Get Tracking Information

Retrieve package tracking information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrackingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    TrackingApi apiInstance = new TrackingApi(defaultClient);
    String carrierCode = "stamps_com"; // String | Carrier code used to retrieve tracking information
    String trackingNumber = "9405511899223197428490"; // String | The tracking number associated with a shipment
    try {
      GetTrackingLogResponseBody result = apiInstance.getTrackingLog(carrierCode, trackingNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrackingApi#getTrackingLog");
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
| **carrierCode** | **String**| Carrier code used to retrieve tracking information | [optional] |
| **trackingNumber** | **String**| The tracking number associated with a shipment | [optional] |

### Return type

[**GetTrackingLogResponseBody**](GetTrackingLogResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="startTracking"></a>
# **startTracking**
> String startTracking(carrierCode, trackingNumber)

Start Tracking a Package

Allows you to subscribe to tracking updates for a package. You specify the carrier_code and tracking_number of the package, and receive notifications via webhooks whenever the shipping status changes. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrackingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    TrackingApi apiInstance = new TrackingApi(defaultClient);
    String carrierCode = "stamps_com"; // String | Carrier code used to retrieve tracking information
    String trackingNumber = "9405511899223197428490"; // String | The tracking number associated with a shipment
    try {
      String result = apiInstance.startTracking(carrierCode, trackingNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrackingApi#startTracking");
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
| **carrierCode** | **String**| Carrier code used to retrieve tracking information | [optional] |
| **trackingNumber** | **String**| The tracking number associated with a shipment | [optional] |

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The request was successful. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="stopTracking"></a>
# **stopTracking**
> String stopTracking(carrierCode, trackingNumber)

Stop Tracking a Package

Unsubscribe from tracking updates for a package.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrackingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    TrackingApi apiInstance = new TrackingApi(defaultClient);
    String carrierCode = "stamps_com"; // String | Carrier code used to retrieve tracking information
    String trackingNumber = "9405511899223197428490"; // String | The tracking number associated with a shipment
    try {
      String result = apiInstance.stopTracking(carrierCode, trackingNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrackingApi#stopTracking");
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
| **carrierCode** | **String**| Carrier code used to retrieve tracking information | [optional] |
| **trackingNumber** | **String**| The tracking number associated with a shipment | [optional] |

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The request was successful. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

