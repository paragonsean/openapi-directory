# DefaultApi

All URIs are relative to *https://api.getthedata.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bng2latlongEastingNorthingGet**](DefaultApi.md#bng2latlongEastingNorthingGet) | **GET** /bng2latlong/{easting}/{northing} | Returns latitude and longitude for the given easting and northing. |


<a id="bng2latlongEastingNorthingGet"></a>
# **bng2latlongEastingNorthingGet**
> Bng2latlongEastingNorthingGet200Response bng2latlongEastingNorthingGet(easting, northing)

Returns latitude and longitude for the given easting and northing.

Takes an OSGB36 easting and northing (British National Grid) and returns the geographically equivalent WGS84 latitude and longitude. #### A successful request returns the following fields: * status - this will be &#x60;ok&#x60; * easting - the easting provided in the request * northing - the northing provided in the request * latitude - the latitude of the converted coordinates * longitude - the longitude of the converted coordinates #### An unsuccessful request returns the following fields: * status - this will be &#x60;error&#x60; * error - an error message 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getthedata.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer easting = 326897; // Integer | An OSGB36 (British National Grid) easting.
    Integer northing = 673919; // Integer | An OSGB36 (British National Grid) northing.
    try {
      Bng2latlongEastingNorthingGet200Response result = apiInstance.bng2latlongEastingNorthingGet(easting, northing);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#bng2latlongEastingNorthingGet");
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
| **easting** | **Integer**| An OSGB36 (British National Grid) easting. | |
| **northing** | **Integer**| An OSGB36 (British National Grid) northing. | |

### Return type

[**Bng2latlongEastingNorthingGet200Response**](Bng2latlongEastingNorthingGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON object containing the original easting and northing, and the converted latitude and longitude. |  -  |

