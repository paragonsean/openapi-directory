# LocationsApi

All URIs are relative to *https://bikewise.org/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**gETVersionLocationsFormat**](LocationsApi.md#gETVersionLocationsFormat) | **GET** /v2/locations | Unpaginated geojson response |
| [**gETVersionLocationsMarkersFormat**](LocationsApi.md#gETVersionLocationsMarkersFormat) | **GET** /v2/locations/markers | Unpaginated geojson response with simplestyled markers |


<a id="gETVersionLocationsFormat"></a>
# **gETVersionLocationsFormat**
> gETVersionLocationsFormat(occurredBefore, occurredAfter, incidentType, proximity, proximitySquare, query, limit, all)

Unpaginated geojson response

&lt;p&gt;&lt;strong&gt;This endpoint behaves exactly like&lt;/strong&gt; &lt;code&gt;incidents&lt;/code&gt;, but returns a valid geojson &lt;code&gt;FeatureCollection&lt;/code&gt; that looks like this:&lt;/p&gt;  &lt;pre&gt;&lt;code&gt;{   type: \&quot;FeatureCollection\&quot;,   features: [     {       type: \&quot;Feature\&quot;,       properties: {       id: 4474199,       type: \&quot;Theft\&quot;,       occurred_at: 1428536937     },       geometry: {       type: \&quot;Point\&quot;,       coordinates: [ -122.6244177, 45.5164386 ]     }   } } &lt;/code&gt;&lt;/pre&gt;  &lt;p&gt;It doesn’t paginate. If you pass the &lt;code&gt;all&lt;/code&gt; parameter it returns all matches (which can be big, &amp;gt; 4mb), otherwise it returns the 100 most recent.&lt;/p&gt;  &lt;p&gt;&lt;strong&gt;Go forth and make maps!&lt;/strong&gt;&lt;/p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://bikewise.org/api");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    Integer occurredBefore = 56; // Integer | <p>End of period</p> 
    Integer occurredAfter = 56; // Integer | <p>Start of period</p> 
    String incidentType = "crash"; // String | <p>Only incidents of specific type</p> 
    String proximity = "proximity_example"; // String | <p>Center of location for proximity search</p> 
    Integer proximitySquare = 100; // Integer | <p>Size of the proximity search</p> 
    String query = "query_example"; // String | <p>Full text search of incidents</p> 
    Integer limit = 56; // Integer | <p>Max number of results to return. Defaults to 100</p> 
    Boolean all = true; // Boolean | <p>Give ‘em all to me. Will ignore limit</p> 
    try {
      apiInstance.gETVersionLocationsFormat(occurredBefore, occurredAfter, incidentType, proximity, proximitySquare, query, limit, all);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#gETVersionLocationsFormat");
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
| **occurredBefore** | **Integer**| &lt;p&gt;End of period&lt;/p&gt;  | [optional] |
| **occurredAfter** | **Integer**| &lt;p&gt;Start of period&lt;/p&gt;  | [optional] |
| **incidentType** | **String**| &lt;p&gt;Only incidents of specific type&lt;/p&gt;  | [optional] [enum: crash, hazard, theft, unconfirmed, infrastructure_issue, chop_shop] |
| **proximity** | **String**| &lt;p&gt;Center of location for proximity search&lt;/p&gt;  | [optional] |
| **proximitySquare** | **Integer**| &lt;p&gt;Size of the proximity search&lt;/p&gt;  | [optional] [default to 100] |
| **query** | **String**| &lt;p&gt;Full text search of incidents&lt;/p&gt;  | [optional] |
| **limit** | **Integer**| &lt;p&gt;Max number of results to return. Defaults to 100&lt;/p&gt;  | [optional] |
| **all** | **Boolean**| &lt;p&gt;Give ‘em all to me. Will ignore limit&lt;/p&gt;  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="gETVersionLocationsMarkersFormat"></a>
# **gETVersionLocationsMarkersFormat**
> gETVersionLocationsMarkersFormat(occurredBefore, occurredAfter, incidentType, proximity, proximitySquare, query, limit, all)

Unpaginated geojson response with simplestyled markers

&lt;p&gt;This behaves exactly like the root &lt;code&gt;locations&lt;/code&gt; endpoint, but returns &lt;a href&#x3D;\&quot;https://github.com/mapbox/simplestyle-spec\&quot;&gt;simplestyled markers&lt;/a&gt; (&lt;a href&#x3D;\&quot;https://www.mapbox.com/guides/markers/#simple-style\&quot;&gt;mapbox styled markers&lt;/a&gt;)&lt;/p&gt;  &lt;p&gt;&lt;strong&gt;Go forth and make maps!&lt;/strong&gt;&lt;/p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://bikewise.org/api");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    Integer occurredBefore = 56; // Integer | <p>End of period</p> 
    Integer occurredAfter = 56; // Integer | <p>Start of period</p> 
    String incidentType = "crash"; // String | <p>Only incidents of specific type</p> 
    String proximity = "proximity_example"; // String | <p>Center of location for proximity search</p> 
    Integer proximitySquare = 100; // Integer | <p>Size of the proximity search</p> 
    String query = "query_example"; // String | <p>Full text search of incidents</p> 
    Integer limit = 56; // Integer | <p>Max number of results to return. Defaults to 100</p> 
    Boolean all = true; // Boolean | <p>Give ‘em all to me. Will ignore limit</p> 
    try {
      apiInstance.gETVersionLocationsMarkersFormat(occurredBefore, occurredAfter, incidentType, proximity, proximitySquare, query, limit, all);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#gETVersionLocationsMarkersFormat");
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
| **occurredBefore** | **Integer**| &lt;p&gt;End of period&lt;/p&gt;  | [optional] |
| **occurredAfter** | **Integer**| &lt;p&gt;Start of period&lt;/p&gt;  | [optional] |
| **incidentType** | **String**| &lt;p&gt;Only incidents of specific type&lt;/p&gt;  | [optional] [enum: crash, hazard, theft, unconfirmed, infrastructure_issue, chop_shop] |
| **proximity** | **String**| &lt;p&gt;Center of location for proximity search&lt;/p&gt;  | [optional] |
| **proximitySquare** | **Integer**| &lt;p&gt;Size of the proximity search&lt;/p&gt;  | [optional] [default to 100] |
| **query** | **String**| &lt;p&gt;Full text search of incidents&lt;/p&gt;  | [optional] |
| **limit** | **Integer**| &lt;p&gt;Max number of results to return. Defaults to 100&lt;/p&gt;  | [optional] |
| **all** | **Boolean**| &lt;p&gt;Give ‘em all to me. Will ignore limit&lt;/p&gt;  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

