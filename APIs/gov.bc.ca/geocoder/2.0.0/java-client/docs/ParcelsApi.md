# ParcelsApi

All URIs are relative to *https://geocoder.api.gov.bc.ca*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**parcelsPidsSiteIDOutputFormatGet**](ParcelsApi.md#parcelsPidsSiteIDOutputFormatGet) | **GET** /parcels/pids/{siteID}.{outputFormat} | Get a comma-separated string of all pids for a given site |


<a id="parcelsPidsSiteIDOutputFormatGet"></a>
# **parcelsPidsSiteIDOutputFormatGet**
> parcelsPidsSiteIDOutputFormatGet(siteID, outputFormat)

Get a comma-separated string of all pids for a given site

Represents all parcel identifiers associated with an individual site

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ParcelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://geocoder.api.gov.bc.ca");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    ParcelsApi apiInstance = new ParcelsApi(defaultClient);
    String siteID = "siteID_example"; // String | A unique, but not immutable, site identifier.
    String outputFormat = "json"; // String | Results format. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputFormat target=\"_blank\">outputFormat</a>.   Note: GeoJSON and KML formats only support EPSG:4326 (outputSRS=4326)
    try {
      apiInstance.parcelsPidsSiteIDOutputFormatGet(siteID, outputFormat);
    } catch (ApiException e) {
      System.err.println("Exception when calling ParcelsApi#parcelsPidsSiteIDOutputFormatGet");
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
| **siteID** | **String**| A unique, but not immutable, site identifier. | |
| **outputFormat** | **String**| Results format. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputFormat target&#x3D;\&quot;_blank\&quot;&gt;outputFormat&lt;/a&gt;.   Note: GeoJSON and KML formats only support EPSG:4326 (outputSRS&#x3D;4326) | [default to json] [enum: json, geojson, xhtml, kml, gml, csv, shpz] |

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A comma-separated string containing all the parcel identifiers associated with the requested siteID |  -  |

