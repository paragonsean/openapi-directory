# GetLocationApi

All URIs are relative to *http://service.miataru.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getLocation**](GetLocationApi.md#getLocation) | **POST** /GetLocation |  |
| [**getLocationGeoJSON**](GetLocationApi.md#getLocationGeoJSON) | **GET** /GetLocationGeoJSON/{deviceID} |  |
| [**getLocationHistory**](GetLocationApi.md#getLocationHistory) | **POST** /GetLocationHistory |  |


<a id="getLocation"></a>
# **getLocation**
> MiataruGetLocationResponse getLocation(body)



To retrieve a specific devices latest known location the /GetLocation method is used. Please note that the MiataruConfig portion is optional. RequestMiataruDeviceID should be the ID of the device the request is sent from (or an identifier like an URL).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetLocationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.miataru.com/v1");

    GetLocationApi apiInstance = new GetLocationApi(defaultClient);
    MiataruGetLocationRequest body = new MiataruGetLocationRequest(); // MiataruGetLocationRequest | the complex JSON formatted datastructure to get the location of one or more devices.
    try {
      MiataruGetLocationResponse result = apiInstance.getLocation(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetLocationApi#getLocation");
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
| **body** | [**MiataruGetLocationRequest**](MiataruGetLocationRequest.md)| the complex JSON formatted datastructure to get the location of one or more devices. | |

### Return type

[**MiataruGetLocationResponse**](MiataruGetLocationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | successful location responses |  -  |

<a id="getLocationGeoJSON"></a>
# **getLocationGeoJSON**
> MiataruGetLocationGeoJSONResponse getLocationGeoJSON(deviceID)



Retrieves a devices Location in GeoJSON format.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetLocationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.miataru.com/v1");

    GetLocationApi apiInstance = new GetLocationApi(defaultClient);
    String deviceID = "7b8e6e0ee5296db345162dc2ef652c1350761823"; // String | the unique device ID of the device the location is requested from
    try {
      MiataruGetLocationGeoJSONResponse result = apiInstance.getLocationGeoJSON(deviceID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetLocationApi#getLocationGeoJSON");
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
| **deviceID** | **String**| the unique device ID of the device the location is requested from | [default to 7b8e6e0ee5296db345162dc2ef652c1350761823] |

### Return type

[**MiataruGetLocationGeoJSONResponse**](MiataruGetLocationGeoJSONResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | geoJSON formatted device location |  -  |

<a id="getLocationHistory"></a>
# **getLocationHistory**
> MiataruGetLocationHistoryResponse getLocationHistory(body)



Location History is stored on the server only if the client told the server to do so using the “EnableLocationHistory” setting in the Location Update requests. For transitions of enabling/disabling that functionality - Everytime a Location Update is received by the server with “EnableLocationHistory&#x3D;false” the server removes all stored Location History till that point. There is a server-side setting that controls up to how many Location Updates the server is storing in the Location History before it removes the oldest one. To request the Location History of a particular device the client sends the following POST request to the GetLocationHistory service URL. Please note that the MiataruConfig portion is optional. RequestMiataruDeviceID should be the ID of the device the request is sent from (or an identifier like an URL).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetLocationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.miataru.com/v1");

    GetLocationApi apiInstance = new GetLocationApi(defaultClient);
    MiataruGetLocationHistoryRequest body = new MiataruGetLocationHistoryRequest(); // MiataruGetLocationHistoryRequest | the complex JSON formatted datastructure to get the location history of one device
    try {
      MiataruGetLocationHistoryResponse result = apiInstance.getLocationHistory(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetLocationApi#getLocationHistory");
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
| **body** | [**MiataruGetLocationHistoryRequest**](MiataruGetLocationHistoryRequest.md)| the complex JSON formatted datastructure to get the location history of one device | |

### Return type

[**MiataruGetLocationHistoryResponse**](MiataruGetLocationHistoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | successful location history response |  -  |

