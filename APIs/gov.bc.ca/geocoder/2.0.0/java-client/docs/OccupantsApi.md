# OccupantsApi

All URIs are relative to *https://geocoder.api.gov.bc.ca*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**occupantsAddressesOutputFormatGet**](OccupantsApi.md#occupantsAddressesOutputFormatGet) | **GET** /occupants/addresses.{outputFormat} | Geocode an address and identify site occupants |
| [**occupantsNearOutputFormatGet**](OccupantsApi.md#occupantsNearOutputFormatGet) | **GET** /occupants/near.{outputFormat} | Find occupants of sites near to a geographic point |
| [**occupantsNearestOutputFormatGet**](OccupantsApi.md#occupantsNearestOutputFormatGet) | **GET** /occupants/nearest.{outputFormat} | Find occupants of the site nearest to a geographic point |
| [**occupantsOccupantIDOutputFormatGet**](OccupantsApi.md#occupantsOccupantIDOutputFormatGet) | **GET** /occupants/{occupantID}.{outputFormat} | Get an occupant (of a site) by its unique ID |
| [**occupantsWithinOutputFormatGet**](OccupantsApi.md#occupantsWithinOutputFormatGet) | **GET** /occupants/within.{outputFormat} | Find occupants of sites in a geographic area |


<a id="occupantsAddressesOutputFormatGet"></a>
# **occupantsAddressesOutputFormatGet**
> occupantsAddressesOutputFormatGet(outputFormat, addressString, tags, locationDescriptor, maxResults, interpolation, echo, brief, autoComplete, setBack, outputSRS, minScore, matchPrecision, matchPrecisionNot, siteName, unitDesignator, unitNumber, unitNumberSuffix, civicNumber, civicNumberSuffix, streetName, streetType, streetDirection, streetQualifier, localityName, provinceCode, localities, notLocalities, bbox, centre, maxDistance, extrapolate, parcelPoint)

Geocode an address and identify site occupants

Represents the set of occupants whose addresses best match a given query address. Every occupant has an associated site which has a standardized address and a coordinate location on the Earth.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OccupantsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://geocoder.api.gov.bc.ca");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    OccupantsApi apiInstance = new OccupantsApi(defaultClient);
    String outputFormat = "json"; // String | Results format. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputFormat target=\"_blank\">outputFormat</a>.   Note: GeoJSON and KML formats only support EPSG:4326 (outputSRS=4326)
    String addressString = "Sir James Douglas Elementary"; // String | Occupant name OR Occupant name ** address
    String tags = "tags_example"; // String | Example: schools;courts;employment<br>A list of tags separated by semicolons.
    String locationDescriptor = "any"; // String | Describes the nature of the address location. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#locationDescriptor target=\"_blank\">locationDescriptor</a>
    Integer maxResults = 1; // Integer | The maximum number of search results to return.
    String interpolation = "adaptive"; // String | accessPoint interpolation method. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#interpolation target=\"_blank\">interpolation</a>
    Boolean echo = false; // Boolean | If true, include unmatched address details such as site name in results.
    Boolean brief = false; // Boolean | If true, include only basic match and address details in results. Not supported for shp, csv, and gml formats.
    Boolean autoComplete = false; // Boolean | If true, addressString is expected to contain a partial address that requires completion. Not supported for shp, csv, gml formats.
    Integer setBack = 0; // Integer | The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint.
    Integer outputSRS = 4326; // Integer | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
    Integer minScore = 1; // Integer | The minimum score required for a match to be returned. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#minScore target=\"_blank\">minScore</a>
    String matchPrecision = "OCCUPANT"; // String | Example: street,locality.  A comma separated list of individual match precision levels to include in results. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#matchPrecision target=\"_blank\">matchPrecision</a>
    String matchPrecisionNot = "matchPrecisionNot_example"; // String | Example: street,locality.  A comma separated list of individual match precision levels to exclude from results. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#matchPrecisionNot target=\"_blank\">matchPrecisionNot</a>
    String siteName = "siteName_example"; // String | A string containing the name of the building, facility, or institution (e.g., Duck Building, Casa Del Mar, Crystal Garden, Bluebird House).See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#siteName target=\"_blank\">siteName</a>
    String unitDesignator = "APT"; // String | The type of unit within a house or building. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#unitDesignator target=\"_blank\">unitDesignator</a>
    String unitNumber = "unitNumber_example"; // String | The number of the unit, suite, or apartment within a house or building.
    String unitNumberSuffix = "unitNumberSuffix_example"; // String | A letter that follows the unit number as in Unit 1A or Suite 302B.
    String civicNumber = "civicNumber_example"; // String | The official number assigned to a site by an address authority. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#civicNumber target=\"_blank\">civicNumber</a>
    String civicNumberSuffix = "civicNumberSuffix_example"; // String | A letter or fraction that follows the civic number (e.g., the A in 1039A Bledsoe St). See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#civicNumberSuffix target=\"_blank\">civicNumberSuffix</a>
    String streetName = "streetName_example"; // String | The official name of the street as assigned by an address authority (e.g., the Douglas in 1175 Douglas Street). See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#streetName target=\"_blank\">streetName</a>
    String streetType = "streetType_example"; // String | The type of street as assigned by a municipality (e.g., the ST in 1175 DOUGLAS St). See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#streetType target=\"_blank\">streetType</a>
    String streetDirection = "N"; // String | The abbreviated compass direction as defined by Canada Post and B.C. civic addressing authorities. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#streetDirection target=\"_blank\">streetDirection</a>
    String streetQualifier = "streetQualifier_example"; // String | The qualifier of a street name (e.g., the Bridge in Johnson St Bridge)
    String localityName = "localityName_example"; // String | The name of the locality assigned to a given site by an address authority. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#streetDirection target=\"_blank\">streetDirection</a>
    String provinceCode = "BC"; // String | The ISO 3166-2 Sub-Country Code. The code for British Columbia is BC.
    String localities = "localities_example"; // String | A comma separated list of locality names that matched addresses must belong to. For example, setting localities to Nanaimo only returns addresses in Nanaimo
    String notLocalities = "notLocalities_example"; // String | A comma-separated list of localities to exclude from the search.
    String bbox = "bbox_example"; // String | Example: -126.07929,49.7628,-126.0163,49.7907.  A bounding box (xmin,ymin,xmax,ymax) that limits the search area. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#bbox target=\"_blank\">bbox</a>
    String centre = "centre_example"; // String | Example: -124.0165926,49.2296251 .  The coordinates of a centre point (x,y) used to define a bounding circle that will limit the search area. This parameter must be specified together with 'maxDistance'. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#centre target='_blank'>centre</a>
    BigDecimal maxDistance = new BigDecimal(78); // BigDecimal | The maximum distance (in metres) to search from the given point.  If not specified, the search distance is unlimited.
    Boolean extrapolate = true; // Boolean | If true, uses supplied parcelPoint to derive an appropriate accessPoint.           See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#extrapolate target=\"_blank\">extrapolate</a>
    String parcelPoint = "parcelPoint_example"; // String | The coordinates of a point (x,y) known to be inside the parcel containing a given address. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#parcelPoint target=\"_blank\">parcelPoint</a>
    try {
      apiInstance.occupantsAddressesOutputFormatGet(outputFormat, addressString, tags, locationDescriptor, maxResults, interpolation, echo, brief, autoComplete, setBack, outputSRS, minScore, matchPrecision, matchPrecisionNot, siteName, unitDesignator, unitNumber, unitNumberSuffix, civicNumber, civicNumberSuffix, streetName, streetType, streetDirection, streetQualifier, localityName, provinceCode, localities, notLocalities, bbox, centre, maxDistance, extrapolate, parcelPoint);
    } catch (ApiException e) {
      System.err.println("Exception when calling OccupantsApi#occupantsAddressesOutputFormatGet");
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
| **outputFormat** | **String**| Results format. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputFormat target&#x3D;\&quot;_blank\&quot;&gt;outputFormat&lt;/a&gt;.   Note: GeoJSON and KML formats only support EPSG:4326 (outputSRS&#x3D;4326) | [default to json] [enum: json, geojson, xhtml, kml, gml, csv, shpz] |
| **addressString** | **String**| Occupant name OR Occupant name ** address | [optional] |
| **tags** | **String**| Example: schools;courts;employment&lt;br&gt;A list of tags separated by semicolons. | [optional] |
| **locationDescriptor** | **String**| Describes the nature of the address location. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#locationDescriptor target&#x3D;\&quot;_blank\&quot;&gt;locationDescriptor&lt;/a&gt; | [optional] [default to any] [enum: any, accessPoint, frontDoorPoint, parcelPoint, rooftopPoint, routingPoint] |
| **maxResults** | **Integer**| The maximum number of search results to return. | [optional] [default to 1] |
| **interpolation** | **String**| accessPoint interpolation method. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#interpolation target&#x3D;\&quot;_blank\&quot;&gt;interpolation&lt;/a&gt; | [optional] [default to adaptive] [enum: adaptive, linear, none] |
| **echo** | **Boolean**| If true, include unmatched address details such as site name in results. | [optional] [default to false] |
| **brief** | **Boolean**| If true, include only basic match and address details in results. Not supported for shp, csv, and gml formats. | [optional] [default to false] |
| **autoComplete** | **Boolean**| If true, addressString is expected to contain a partial address that requires completion. Not supported for shp, csv, gml formats. | [optional] [default to false] |
| **setBack** | **Integer**| The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint. | [optional] [default to 0] |
| **outputSRS** | **Integer**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326] [enum: 4326, 4269, 3005, 26907, 26908, 26909, 26910, 26911] |
| **minScore** | **Integer**| The minimum score required for a match to be returned. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#minScore target&#x3D;\&quot;_blank\&quot;&gt;minScore&lt;/a&gt; | [optional] [default to 1] |
| **matchPrecision** | **String**| Example: street,locality.  A comma separated list of individual match precision levels to include in results. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#matchPrecision target&#x3D;\&quot;_blank\&quot;&gt;matchPrecision&lt;/a&gt; | [optional] [default to OCCUPANT] |
| **matchPrecisionNot** | **String**| Example: street,locality.  A comma separated list of individual match precision levels to exclude from results. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#matchPrecisionNot target&#x3D;\&quot;_blank\&quot;&gt;matchPrecisionNot&lt;/a&gt; | [optional] |
| **siteName** | **String**| A string containing the name of the building, facility, or institution (e.g., Duck Building, Casa Del Mar, Crystal Garden, Bluebird House).See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#siteName target&#x3D;\&quot;_blank\&quot;&gt;siteName&lt;/a&gt; | [optional] |
| **unitDesignator** | **String**| The type of unit within a house or building. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#unitDesignator target&#x3D;\&quot;_blank\&quot;&gt;unitDesignator&lt;/a&gt; | [optional] [enum: APT, BLDG, BSMT, FLR, LOBBY, LWR, PAD, PH, REAR, RM, SIDE, SITE, SUITE, TH, UNIT, UPPR] |
| **unitNumber** | **String**| The number of the unit, suite, or apartment within a house or building. | [optional] |
| **unitNumberSuffix** | **String**| A letter that follows the unit number as in Unit 1A or Suite 302B. | [optional] |
| **civicNumber** | **String**| The official number assigned to a site by an address authority. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#civicNumber target&#x3D;\&quot;_blank\&quot;&gt;civicNumber&lt;/a&gt; | [optional] |
| **civicNumberSuffix** | **String**| A letter or fraction that follows the civic number (e.g., the A in 1039A Bledsoe St). See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#civicNumberSuffix target&#x3D;\&quot;_blank\&quot;&gt;civicNumberSuffix&lt;/a&gt; | [optional] |
| **streetName** | **String**| The official name of the street as assigned by an address authority (e.g., the Douglas in 1175 Douglas Street). See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#streetName target&#x3D;\&quot;_blank\&quot;&gt;streetName&lt;/a&gt; | [optional] |
| **streetType** | **String**| The type of street as assigned by a municipality (e.g., the ST in 1175 DOUGLAS St). See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#streetType target&#x3D;\&quot;_blank\&quot;&gt;streetType&lt;/a&gt; | [optional] |
| **streetDirection** | **String**| The abbreviated compass direction as defined by Canada Post and B.C. civic addressing authorities. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#streetDirection target&#x3D;\&quot;_blank\&quot;&gt;streetDirection&lt;/a&gt; | [optional] [enum: N, S, E, W, O, NE, false, NW, SE, SO, SW] |
| **streetQualifier** | **String**| The qualifier of a street name (e.g., the Bridge in Johnson St Bridge) | [optional] |
| **localityName** | **String**| The name of the locality assigned to a given site by an address authority. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#streetDirection target&#x3D;\&quot;_blank\&quot;&gt;streetDirection&lt;/a&gt; | [optional] |
| **provinceCode** | **String**| The ISO 3166-2 Sub-Country Code. The code for British Columbia is BC. | [optional] [default to BC] |
| **localities** | **String**| A comma separated list of locality names that matched addresses must belong to. For example, setting localities to Nanaimo only returns addresses in Nanaimo | [optional] |
| **notLocalities** | **String**| A comma-separated list of localities to exclude from the search. | [optional] |
| **bbox** | **String**| Example: -126.07929,49.7628,-126.0163,49.7907.  A bounding box (xmin,ymin,xmax,ymax) that limits the search area. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#bbox target&#x3D;\&quot;_blank\&quot;&gt;bbox&lt;/a&gt; | [optional] |
| **centre** | **String**| Example: -124.0165926,49.2296251 .  The coordinates of a centre point (x,y) used to define a bounding circle that will limit the search area. This parameter must be specified together with &#39;maxDistance&#39;. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#centre target&#x3D;&#39;_blank&#39;&gt;centre&lt;/a&gt; | [optional] |
| **maxDistance** | **BigDecimal**| The maximum distance (in metres) to search from the given point.  If not specified, the search distance is unlimited. | [optional] |
| **extrapolate** | **Boolean**| If true, uses supplied parcelPoint to derive an appropriate accessPoint.           See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#extrapolate target&#x3D;\&quot;_blank\&quot;&gt;extrapolate&lt;/a&gt; | [optional] |
| **parcelPoint** | **String**| The coordinates of a point (x,y) known to be inside the parcel containing a given address. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#parcelPoint target&#x3D;\&quot;_blank\&quot;&gt;parcelPoint&lt;/a&gt; | [optional] |

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
| **200** | A list of matching occupants, sites, and their physical locations. Response document will contain one &lt;a href&#x3D;\&quot;https://github.com/bcgov/ols-geocoder/blob/gh-pages/geocoder-developer-guide.md#about-query-representation\&quot; target&#x3D;\&quot;_blank\&quot;&gt;About Query Representation&lt;/a&gt; and one &lt;a href&#x3D;\&quot;https://github.com/bcgov/ols-geocoder/blob/gh-pages/geocoder-developer-guide.md#site-address-representation\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Site Address Representation&lt;/a&gt; plus &lt;a href&#x3D;\&quot;https://github.com/bcgov/ols-geocoder/blob/gh-pages/geocoder-developer-guide.md#occupant-representation\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Occupant Representation&lt;/a&gt; for each matching occupant. |  -  |

<a id="occupantsNearOutputFormatGet"></a>
# **occupantsNearOutputFormatGet**
> occupantsNearOutputFormatGet(outputFormat, point, tags, maxDistance, outputSRS, maxResults, locationDescriptor, brief, setBack)

Find occupants of sites near to a geographic point

Represents occupants near a given point in order of closest to farthest

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OccupantsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://geocoder.api.gov.bc.ca");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    OccupantsApi apiInstance = new OccupantsApi(defaultClient);
    String outputFormat = "json"; // String | Results format. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputFormat target=\"_blank\">outputFormat</a>.   Note: GeoJSON and KML formats only support EPSG:4326 (outputSRS=4326)
    String point = "-122.377,50.121"; // String | The point (x,y) from which the nearest site will be identified. The coordinates must be specified in the same SRS as given by the 'outputSRS' parameter.
    String tags = "tags_example"; // String | Example: schools;courts;employment<br>A list of tags separated by semicolons.
    Integer maxDistance = 56; // Integer | The maximum distance (in metres) to search from the given point.  If not specified, the search distance is unlimited.
    Integer outputSRS = 4326; // Integer | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
    Integer maxResults = 1; // Integer | The maximum number of search results to return.
    String locationDescriptor = "any"; // String | Describes the nature of the address location. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#locationDescriptor target=\"_blank\">locationDescriptor</a>
    Boolean brief = false; // Boolean | If true, include only basic match and address details in results. Not supported for shp, csv, and gml formats.
    Integer setBack = 0; // Integer | The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint.
    try {
      apiInstance.occupantsNearOutputFormatGet(outputFormat, point, tags, maxDistance, outputSRS, maxResults, locationDescriptor, brief, setBack);
    } catch (ApiException e) {
      System.err.println("Exception when calling OccupantsApi#occupantsNearOutputFormatGet");
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
| **outputFormat** | **String**| Results format. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputFormat target&#x3D;\&quot;_blank\&quot;&gt;outputFormat&lt;/a&gt;.   Note: GeoJSON and KML formats only support EPSG:4326 (outputSRS&#x3D;4326) | [default to json] [enum: json, geojson, xhtml, kml, gml, csv, shpz] |
| **point** | **String**| The point (x,y) from which the nearest site will be identified. The coordinates must be specified in the same SRS as given by the &#39;outputSRS&#39; parameter. | |
| **tags** | **String**| Example: schools;courts;employment&lt;br&gt;A list of tags separated by semicolons. | [optional] |
| **maxDistance** | **Integer**| The maximum distance (in metres) to search from the given point.  If not specified, the search distance is unlimited. | [optional] |
| **outputSRS** | **Integer**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326] [enum: 4326, 4269, 3005, 26907, 26908, 26909, 26910, 26911] |
| **maxResults** | **Integer**| The maximum number of search results to return. | [optional] [default to 1] |
| **locationDescriptor** | **String**| Describes the nature of the address location. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#locationDescriptor target&#x3D;\&quot;_blank\&quot;&gt;locationDescriptor&lt;/a&gt; | [optional] [default to any] [enum: any, accessPoint, frontDoorPoint, parcelPoint, rooftopPoint, routingPoint] |
| **brief** | **Boolean**| If true, include only basic match and address details in results. Not supported for shp, csv, and gml formats. | [optional] [default to false] |
| **setBack** | **Integer**| The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint. | [optional] [default to 0] |

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
| **200** | A list of selected occupants that are near a given point in order of closest to farther. Each occupant is returned as a &lt;a href&#x3D;\&quot;https://github.com/bcgov/ols-geocoder/blob/gh-pages/geocoder-developer-guide.md#site-address-representation\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Site Address Representation&lt;/a&gt; plus a &lt;a href&#x3D;\&quot;https://github.com/bcgov/ols-geocoder/blob/gh-pages/geocoder-developer-guide.md#occupant-representation\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Occupant Representation&lt;/a&gt; |  -  |

<a id="occupantsNearestOutputFormatGet"></a>
# **occupantsNearestOutputFormatGet**
> occupantsNearestOutputFormatGet(outputFormat, point, maxDistance, tags, outputSRS, locationDescriptor, brief, setBack)

Find occupants of the site nearest to a geographic point

Represents the closest occupant to a given point

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OccupantsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://geocoder.api.gov.bc.ca");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    OccupantsApi apiInstance = new OccupantsApi(defaultClient);
    String outputFormat = "json"; // String | Results format. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputFormat target=\"_blank\">outputFormat</a>.   Note: GeoJSON and KML formats only support EPSG:4326 (outputSRS=4326)
    String point = "-122.377,50.121"; // String | The point (x,y) from which the nearest site will be identified. The coordinates must be specified in the same SRS as given by the 'outputSRS' parameter.
    Integer maxDistance = 56; // Integer | The maximum distance (in metres) to search from the given point.  If not specified, the search distance is unlimited.
    String tags = "tags_example"; // String | Example: schools;courts;employment<br>A list of tags separated by semicolons.
    Integer outputSRS = 4326; // Integer | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
    String locationDescriptor = "any"; // String | Describes the nature of the address location. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#locationDescriptor target=\"_blank\">locationDescriptor</a>
    Boolean brief = false; // Boolean | If true, include only basic match and address details in results. Not supported for shp, csv, and gml formats.
    Integer setBack = 0; // Integer | The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint.
    try {
      apiInstance.occupantsNearestOutputFormatGet(outputFormat, point, maxDistance, tags, outputSRS, locationDescriptor, brief, setBack);
    } catch (ApiException e) {
      System.err.println("Exception when calling OccupantsApi#occupantsNearestOutputFormatGet");
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
| **outputFormat** | **String**| Results format. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputFormat target&#x3D;\&quot;_blank\&quot;&gt;outputFormat&lt;/a&gt;.   Note: GeoJSON and KML formats only support EPSG:4326 (outputSRS&#x3D;4326) | [default to json] [enum: json, geojson, xhtml, kml, gml, csv, shpz] |
| **point** | **String**| The point (x,y) from which the nearest site will be identified. The coordinates must be specified in the same SRS as given by the &#39;outputSRS&#39; parameter. | |
| **maxDistance** | **Integer**| The maximum distance (in metres) to search from the given point.  If not specified, the search distance is unlimited. | [optional] |
| **tags** | **String**| Example: schools;courts;employment&lt;br&gt;A list of tags separated by semicolons. | [optional] |
| **outputSRS** | **Integer**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326] [enum: 4326, 4269, 3005, 26907, 26908, 26909, 26910, 26911] |
| **locationDescriptor** | **String**| Describes the nature of the address location. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#locationDescriptor target&#x3D;\&quot;_blank\&quot;&gt;locationDescriptor&lt;/a&gt; | [optional] [default to any] [enum: any, accessPoint, frontDoorPoint, parcelPoint, rooftopPoint, routingPoint] |
| **brief** | **Boolean**| If true, include only basic match and address details in results. Not supported for shp, csv, and gml formats. | [optional] [default to false] |
| **setBack** | **Integer**| The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint. | [optional] [default to 0] |

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
| **200** | The nearest occupant in &lt;a href&#x3D;\&quot;https://github.com/bcgov/ols-geocoder/blob/gh-pages/geocoder-developer-guide.md#site-address-representation\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Site Address Representation&lt;/a&gt; plus &lt;a href&#x3D;\&quot;https://github.com/bcgov/ols-geocoder/blob/gh-pages/geocoder-developer-guide.md#occupant-representation\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Occupant Representation&lt;/a&gt; |  -  |

<a id="occupantsOccupantIDOutputFormatGet"></a>
# **occupantsOccupantIDOutputFormatGet**
> occupantsOccupantIDOutputFormatGet(occupantID, outputFormat, outputSRS, locationDescriptor, brief, setBack)

Get an occupant (of a site) by its unique ID

Represents an individual occupant

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OccupantsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://geocoder.api.gov.bc.ca");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    OccupantsApi apiInstance = new OccupantsApi(defaultClient);
    String occupantID = "occupantID_example"; // String | Occupant identifier
    String outputFormat = "json"; // String | Results format. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputFormat target=\"_blank\">outputFormat</a>.   Note: GeoJSON and KML formats only support EPSG:4326 (outputSRS=4326)
    Integer outputSRS = 4326; // Integer | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
    String locationDescriptor = "any"; // String | Describes the nature of the address location. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#locationDescriptor target=\"_blank\">locationDescriptor</a>
    Boolean brief = false; // Boolean | If true, include only basic match and address details in results. Not supported for shp, csv, and gml formats.
    Integer setBack = 0; // Integer | The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint.
    try {
      apiInstance.occupantsOccupantIDOutputFormatGet(occupantID, outputFormat, outputSRS, locationDescriptor, brief, setBack);
    } catch (ApiException e) {
      System.err.println("Exception when calling OccupantsApi#occupantsOccupantIDOutputFormatGet");
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
| **occupantID** | **String**| Occupant identifier | |
| **outputFormat** | **String**| Results format. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputFormat target&#x3D;\&quot;_blank\&quot;&gt;outputFormat&lt;/a&gt;.   Note: GeoJSON and KML formats only support EPSG:4326 (outputSRS&#x3D;4326) | [default to json] [enum: json, geojson, xhtml, kml, gml, csv, shpz] |
| **outputSRS** | **Integer**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326] [enum: 4326, 4269, 3005, 26907, 26908, 26909, 26910, 26911] |
| **locationDescriptor** | **String**| Describes the nature of the address location. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#locationDescriptor target&#x3D;\&quot;_blank\&quot;&gt;locationDescriptor&lt;/a&gt; | [optional] [default to any] [enum: any, accessPoint, frontDoorPoint, parcelPoint, rooftopPoint, routingPoint] |
| **brief** | **Boolean**| If true, include only basic match and address details in results. Not supported for shp, csv, and gml formats. | [optional] [default to false] |
| **setBack** | **Integer**| The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint. | [optional] [default to 0] |

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
| **200** | The occupant with the requested occupantID in &lt;a href&#x3D;\&quot;https://github.com/bcgov/ols-geocoder/blob/gh-pages/geocoder-developer-guide.md#site-address-representation\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Site Address Representation&lt;/a&gt; plus &lt;a href&#x3D;\&quot;https://github.com/bcgov/ols-geocoder/blob/gh-pages/geocoder-developer-guide.md#occupant-representation\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Occupant Representation&lt;/a&gt; |  -  |

<a id="occupantsWithinOutputFormatGet"></a>
# **occupantsWithinOutputFormatGet**
> occupantsWithinOutputFormatGet(outputFormat, bbox, tags, outputSRS, maxResults, locationDescriptor, brief, setBack)

Find occupants of sites in a geographic area

Represents all occupants within a given area

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OccupantsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://geocoder.api.gov.bc.ca");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    OccupantsApi apiInstance = new OccupantsApi(defaultClient);
    String outputFormat = "json"; // String | Results format. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputFormat target=\"_blank\">outputFormat</a>.   Note: GeoJSON and KML formats only support EPSG:4326 (outputSRS=4326)
    String bbox = "-123.14,49.28,-123.13,49.29"; // String | A bounding box (xmin,ymin,xmax,ymax) used to limit the search area. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#bbox target=\"_blank\">bbox</a>
    String tags = "tags_example"; // String | Example: schools;courts;employment<br>A list of tags separated by semicolons.
    Integer outputSRS = 4326; // Integer | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
    Integer maxResults = 200; // Integer | The maximum number of search results to return.
    String locationDescriptor = "any"; // String | Describes the nature of the address location. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#locationDescriptor target=\"_blank\">locationDescriptor</a>
    Boolean brief = false; // Boolean | If true, include only basic match and address details in results. Not supported for shp, csv, and gml formats.
    Integer setBack = 0; // Integer | The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint.
    try {
      apiInstance.occupantsWithinOutputFormatGet(outputFormat, bbox, tags, outputSRS, maxResults, locationDescriptor, brief, setBack);
    } catch (ApiException e) {
      System.err.println("Exception when calling OccupantsApi#occupantsWithinOutputFormatGet");
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
| **outputFormat** | **String**| Results format. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputFormat target&#x3D;\&quot;_blank\&quot;&gt;outputFormat&lt;/a&gt;.   Note: GeoJSON and KML formats only support EPSG:4326 (outputSRS&#x3D;4326) | [default to json] [enum: json, geojson, xhtml, kml, gml, csv, shpz] |
| **bbox** | **String**| A bounding box (xmin,ymin,xmax,ymax) used to limit the search area. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#bbox target&#x3D;\&quot;_blank\&quot;&gt;bbox&lt;/a&gt; | |
| **tags** | **String**| Example: schools;courts;employment&lt;br&gt;A list of tags separated by semicolons. | [optional] |
| **outputSRS** | **Integer**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326] [enum: 4326, 4269, 3005, 26907, 26908, 26909, 26910, 26911] |
| **maxResults** | **Integer**| The maximum number of search results to return. | [optional] [default to 200] |
| **locationDescriptor** | **String**| Describes the nature of the address location. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#locationDescriptor target&#x3D;\&quot;_blank\&quot;&gt;locationDescriptor&lt;/a&gt; | [optional] [default to any] [enum: any, accessPoint, frontDoorPoint, parcelPoint, rooftopPoint, routingPoint] |
| **brief** | **Boolean**| If true, include only basic match and address details in results. Not supported for shp, csv, and gml formats. | [optional] [default to false] |
| **setBack** | **Integer**| The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint. | [optional] [default to 0] |

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
| **200** | A list of selected occupants within the given area. Each occupant is returned in a &lt;a href&#x3D;\&quot;https://github.com/bcgov/ols-geocoder/blob/gh-pages/geocoder-developer-guide.md#site-address-representation\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Site Address Representation&lt;/a&gt; plus &lt;a href&#x3D;\&quot;https://github.com/bcgov/ols-geocoder/blob/gh-pages/geocoder-developer-guide.md#occupant-representation\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Occupant Representation&lt;/a&gt; |  -  |

