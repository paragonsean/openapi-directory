# GeometriesApiApi

All URIs are relative to *https://idealspot-geodata.p.rapidapi.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchAdministrativeRegionsusingLatLng**](GeometriesApiApi.md#fetchAdministrativeRegionsusingLatLng) | **GET** /geometries/regions/intersecting/{latitude}/{longitude} | Fetch Administrative Regions using Lat/Lng |
| [**fetchGeometries**](GeometriesApiApi.md#fetchGeometries) | **GET** /geometries/geometry | Fetch Geometries |


<a id="fetchAdministrativeRegionsusingLatLng"></a>
# **fetchAdministrativeRegionsusingLatLng**
> FetchAdministrativeRegionsusingLatLng fetchAdministrativeRegionsusingLatLng(latitude, longitude, xRapidAPIKey, xRapidAPIHost)

Fetch Administrative Regions using Lat/Lng

For given latitude and longitude, find intersecting administrative regions. Region polygons are simplified for web mapping.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeometriesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://idealspot-geodata.p.rapidapi.com/api/v1");

    GeometriesApiApi apiInstance = new GeometriesApiApi(defaultClient);
    Double latitude = 3.4D; // Double | (Required) Search coordinate latitude
    Double longitude = 3.4D; // Double | (Required) Search coordinate longitude
    String xRapidAPIKey = "xRapidAPIKey_example"; // String | (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata
    String xRapidAPIHost = "xRapidAPIHost_example"; // String | 
    try {
      FetchAdministrativeRegionsusingLatLng result = apiInstance.fetchAdministrativeRegionsusingLatLng(latitude, longitude, xRapidAPIKey, xRapidAPIHost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeometriesApiApi#fetchAdministrativeRegionsusingLatLng");
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
| **latitude** | **Double**| (Required) Search coordinate latitude | |
| **longitude** | **Double**| (Required) Search coordinate longitude | |
| **xRapidAPIKey** | **String**| (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata | |
| **xRapidAPIHost** | **String**|  | |

### Return type

[**FetchAdministrativeRegionsusingLatLng**](FetchAdministrativeRegionsusingLatLng.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Server -  <br>  * Vary -  <br>  * Via -  <br>  * X-RapidAPI-Region -  <br>  * X-RapidAPI-Version -  <br>  * access-control-allow-credentials -  <br>  * access-control-allow-origin -  <br>  * access-control-expose-headers -  <br>  * cache-control -  <br>  * transfer-encoding -  <br>  |

<a id="fetchGeometries"></a>
# **fetchGeometries**
> Describetheregionwithin5minutedriveTimeofageographicpoint fetchGeometries(location, xRapidAPIKey, xRapidAPIHost)

Fetch Geometries

Fetch location GeoJSON

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeometriesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://idealspot-geodata.p.rapidapi.com/api/v1");

    GeometriesApiApi apiInstance = new GeometriesApiApi(defaultClient);
    String location = "location_example"; // String | (Required) Represents a buffer, region, or custom polygon specification. Accepts the `Location` model (as a `Buffer`, `Region`, or `Custom Polygon`) formatted as a JSON string. Multiple `location` query parameters are allowed. NOTE: When requesting multiple locations, you must include brackets(i.e. `?location[]=...&location[]=...`). If not included, only the last location will be used.
    String xRapidAPIKey = "xRapidAPIKey_example"; // String | (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata
    String xRapidAPIHost = "xRapidAPIHost_example"; // String | 
    try {
      Describetheregionwithin5minutedriveTimeofageographicpoint result = apiInstance.fetchGeometries(location, xRapidAPIKey, xRapidAPIHost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeometriesApiApi#fetchGeometries");
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
| **location** | **String**| (Required) Represents a buffer, region, or custom polygon specification. Accepts the &#x60;Location&#x60; model (as a &#x60;Buffer&#x60;, &#x60;Region&#x60;, or &#x60;Custom Polygon&#x60;) formatted as a JSON string. Multiple &#x60;location&#x60; query parameters are allowed. NOTE: When requesting multiple locations, you must include brackets(i.e. &#x60;?location[]&#x3D;...&amp;location[]&#x3D;...&#x60;). If not included, only the last location will be used. | |
| **xRapidAPIKey** | **String**| (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata | |
| **xRapidAPIHost** | **String**|  | |

### Return type

[**Describetheregionwithin5minutedriveTimeofageographicpoint**](Describetheregionwithin5minutedriveTimeofageographicpoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Length -  <br>  * Date -  <br>  * Server -  <br>  * Vary -  <br>  * Via -  <br>  * X-RapidAPI-Region -  <br>  * X-RapidAPI-Version -  <br>  * access-control-allow-credentials -  <br>  * access-control-allow-origin -  <br>  * access-control-expose-headers -  <br>  * cache-control -  <br>  |

