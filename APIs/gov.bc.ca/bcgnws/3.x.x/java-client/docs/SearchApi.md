# SearchApi

All URIs are relative to *https://apps.gov.bc.ca/pub/bcgnws*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**namesChangesGet**](SearchApi.md#namesChangesGet) | **GET** /names/changes | Search for names with metadata changes in a given period |
| [**namesDecisionsRecentGet**](SearchApi.md#namesDecisionsRecentGet) | **GET** /names/decisions/recent | Search for names affected by recent naming decision |
| [**namesDecisionsYearGet**](SearchApi.md#namesDecisionsYearGet) | **GET** /names/decisions/year | Search for names affected by naming decisions in a given year |
| [**namesInsideGet**](SearchApi.md#namesInsideGet) | **GET** /names/inside | Search in a geographic area |
| [**namesNearGet**](SearchApi.md#namesNearGet) | **GET** /names/near | Search near to a geographic point |
| [**namesNotOfficialSearchGet**](SearchApi.md#namesNotOfficialSearchGet) | **GET** /names/notOfficial/search | Search by name, limit to unofficial names only |
| [**namesOfficialSearchGet**](SearchApi.md#namesOfficialSearchGet) | **GET** /names/official/search | Search by name, limit to official names only |
| [**namesSearchGet**](SearchApi.md#namesSearchGet) | **GET** /names/search | Search by name |


<a id="namesChangesGet"></a>
# **namesChangesGet**
> namesChangesGet(outputFormat, fromDate, toDate, featureClass, featureCategory, featureType, sortBy, outputSRS, embed, outputStyle, itemsPerPage, startIndex)

Search for names with metadata changes in a given period

Search for information about geographical names which have changed most recently within a specified time window.  Changes may include status cupdates and metadata corrections.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apps.gov.bc.ca/pub/bcgnws");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String outputFormat = "json"; // String | The format of the output.
    Integer fromDate = 2017-01-01; // Integer | Defines the earliest date (YYYY-MM-DD format) of the change time window for the search
    Integer toDate = 2017-06-30; // Integer | Defines the latest date (YYYY-MM-DD format) of the change time window for the search
    String featureClass = "*"; // String | A filter to limit the search to names associated with features of a certain 'class'  The value of this parameter should be a 'featureClassCode' value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included.
    String featureCategory = "*"; // String | A filter to limit the search to names associated with features of a certain 'category'  The value of this parameter should be a 'featureCategoryCode' value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included.
    String featureType = "*"; // String | A filter to limit the search to names associated with features of a certain 'type'  The value of this parameter should be a 'featureTypeCode' value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included
    String sortBy = "name"; // String | The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint.
    Integer outputSRS = 4326; // Integer | The EPSG code of the spatial reference system (SRS) to use for output geometries.
    Integer embed = 0; // Integer | A flag to indicate whether to embed the corresponding 'feature' into each matching name
    String outputStyle = "summary"; // String | A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail)
    Integer itemsPerPage = 20; // Integer | The number of search results to return (1-200)
    Integer startIndex = 1; // Integer | The index of the first record to be returned (>= 1)
    try {
      apiInstance.namesChangesGet(outputFormat, fromDate, toDate, featureClass, featureCategory, featureType, sortBy, outputSRS, embed, outputStyle, itemsPerPage, startIndex);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#namesChangesGet");
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
| **outputFormat** | **String**| The format of the output. | [default to json] [enum: json, xml, kml, csv] |
| **fromDate** | **Integer**| Defines the earliest date (YYYY-MM-DD format) of the change time window for the search | |
| **toDate** | **Integer**| Defines the latest date (YYYY-MM-DD format) of the change time window for the search | |
| **featureClass** | **String**| A filter to limit the search to names associated with features of a certain &#39;class&#39;  The value of this parameter should be a &#39;featureClassCode&#39; value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included. | [optional] [default to *] |
| **featureCategory** | **String**| A filter to limit the search to names associated with features of a certain &#39;category&#39;  The value of this parameter should be a &#39;featureCategoryCode&#39; value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included. | [optional] [default to *] |
| **featureType** | **String**| A filter to limit the search to names associated with features of a certain &#39;type&#39;  The value of this parameter should be a &#39;featureTypeCode&#39; value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included | [optional] [default to *] |
| **sortBy** | **String**| The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint. | [optional] [default to name] [enum: name, featureType, decisionDate] |
| **outputSRS** | **Integer**| The EPSG code of the spatial reference system (SRS) to use for output geometries. | [optional] [default to 4326] [enum: 4326, 4269, 3005, 3857, 26907, 26908, 26909, 26910, 26911] |
| **embed** | **Integer**| A flag to indicate whether to embed the corresponding &#39;feature&#39; into each matching name | [optional] [enum: 0, 1] |
| **outputStyle** | **String**| A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail) | [optional] [default to summary] [enum: summary, detail] |
| **itemsPerPage** | **Integer**| The number of search results to return (1-200) | [optional] [default to 20] |
| **startIndex** | **Integer**| The index of the first record to be returned (&gt;&#x3D; 1) | [optional] [default to 1] |

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
| **200** | A list of names matching the search criteria |  -  |
| **400** | A required parameter is missing or invalid |  -  |

<a id="namesDecisionsRecentGet"></a>
# **namesDecisionsRecentGet**
> namesDecisionsRecentGet(outputFormat, days, featureClass, featureCategory, featureType, sortBy, outputSRS, embed, outputStyle, itemsPerPage, startIndex)

Search for names affected by recent naming decision

Search for information about geographical names affected by naming &#39;decisions&#39; made by the BC Geographical Names Office (naming authority) within the last X days.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apps.gov.bc.ca/pub/bcgnws");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String outputFormat = "json"; // String | The format of the output.
    Integer days = 30; // Integer | The number of days used to define the time window of naming decisions to search.  The number is interpreted as searching for 'names affected by decisions within the last X days'.
    String featureClass = "*"; // String | A filter to limit the search to names associated with features of a certain 'class'  The value of this parameter should be a 'featureClassCode' value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included.
    String featureCategory = "*"; // String | A filter to limit the search to names associated with features of a certain 'category'  The value of this parameter should be a 'featureCategoryCode' value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included.
    String featureType = "*"; // String | A filter to limit the search to names associated with features of a certain 'type'  The value of this parameter should be a 'featureTypeCode' value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included
    String sortBy = "name"; // String | The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint.
    Integer outputSRS = 4326; // Integer | The EPSG code of the spatial reference system (SRS) to use for output geometries.
    Integer embed = 0; // Integer | A flag to indicate whether to embed the corresponding 'feature' into each matching name
    String outputStyle = "summary"; // String | A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail)
    Integer itemsPerPage = 20; // Integer | The number of search results to return (1-200)
    Integer startIndex = 1; // Integer | The index of the first record to be returned (>= 1)
    try {
      apiInstance.namesDecisionsRecentGet(outputFormat, days, featureClass, featureCategory, featureType, sortBy, outputSRS, embed, outputStyle, itemsPerPage, startIndex);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#namesDecisionsRecentGet");
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
| **outputFormat** | **String**| The format of the output. | [default to json] [enum: json, xml, kml, csv] |
| **days** | **Integer**| The number of days used to define the time window of naming decisions to search.  The number is interpreted as searching for &#39;names affected by decisions within the last X days&#39;. | [default to 30] |
| **featureClass** | **String**| A filter to limit the search to names associated with features of a certain &#39;class&#39;  The value of this parameter should be a &#39;featureClassCode&#39; value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included. | [optional] [default to *] |
| **featureCategory** | **String**| A filter to limit the search to names associated with features of a certain &#39;category&#39;  The value of this parameter should be a &#39;featureCategoryCode&#39; value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included. | [optional] [default to *] |
| **featureType** | **String**| A filter to limit the search to names associated with features of a certain &#39;type&#39;  The value of this parameter should be a &#39;featureTypeCode&#39; value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included | [optional] [default to *] |
| **sortBy** | **String**| The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint. | [optional] [default to name] [enum: name, featureType, decisionDate] |
| **outputSRS** | **Integer**| The EPSG code of the spatial reference system (SRS) to use for output geometries. | [optional] [default to 4326] [enum: 4326, 4269, 3005, 3857, 26907, 26908, 26909, 26910, 26911] |
| **embed** | **Integer**| A flag to indicate whether to embed the corresponding &#39;feature&#39; into each matching name | [optional] [enum: 0, 1] |
| **outputStyle** | **String**| A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail) | [optional] [default to summary] [enum: summary, detail] |
| **itemsPerPage** | **Integer**| The number of search results to return (1-200) | [optional] [default to 20] |
| **startIndex** | **Integer**| The index of the first record to be returned (&gt;&#x3D; 1) | [optional] [default to 1] |

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
| **200** | A list of names matching the search criteria |  -  |
| **400** | A required parameter is missing or invalid |  -  |

<a id="namesDecisionsYearGet"></a>
# **namesDecisionsYearGet**
> namesDecisionsYearGet(outputFormat, year, featureClass, featureCategory, featureType, sortBy, outputSRS, embed, outputStyle, itemsPerPage, startIndex)

Search for names affected by naming decisions in a given year

Search for information about geographical names affected by naming &#39;decisions&#39; made by the BC Geographical Names Office (naming authority) in a given year.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apps.gov.bc.ca/pub/bcgnws");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String outputFormat = "json"; // String | The format of the output.
    Integer year = 2007; // Integer | The year in which to search for names affected by naming decisions'.
    String featureClass = "*"; // String | A filter to limit the search to names associated with features of a certain 'class'  The value of this parameter should be a 'featureClassCode' value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included.
    String featureCategory = "*"; // String | A filter to limit the search to names associated with features of a certain 'category'  The value of this parameter should be a 'featureCategoryCode' value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included.
    String featureType = "*"; // String | A filter to limit the search to names associated with features of a certain 'type'  The value of this parameter should be a 'featureTypeCode' value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included
    String sortBy = "name"; // String | The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint.
    Integer outputSRS = 4326; // Integer | The EPSG code of the spatial reference system (SRS) to use for output geometries.
    Integer embed = 0; // Integer | A flag to indicate whether to embed the corresponding 'feature' into each matching name
    String outputStyle = "summary"; // String | A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail)
    Integer itemsPerPage = 20; // Integer | The number of search results to return (1-200)
    Integer startIndex = 1; // Integer | The index of the first record to be returned (>= 1)
    try {
      apiInstance.namesDecisionsYearGet(outputFormat, year, featureClass, featureCategory, featureType, sortBy, outputSRS, embed, outputStyle, itemsPerPage, startIndex);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#namesDecisionsYearGet");
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
| **outputFormat** | **String**| The format of the output. | [default to json] [enum: json, xml, kml, csv] |
| **year** | **Integer**| The year in which to search for names affected by naming decisions&#39;. | |
| **featureClass** | **String**| A filter to limit the search to names associated with features of a certain &#39;class&#39;  The value of this parameter should be a &#39;featureClassCode&#39; value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included. | [optional] [default to *] |
| **featureCategory** | **String**| A filter to limit the search to names associated with features of a certain &#39;category&#39;  The value of this parameter should be a &#39;featureCategoryCode&#39; value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included. | [optional] [default to *] |
| **featureType** | **String**| A filter to limit the search to names associated with features of a certain &#39;type&#39;  The value of this parameter should be a &#39;featureTypeCode&#39; value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included | [optional] [default to *] |
| **sortBy** | **String**| The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint. | [optional] [default to name] [enum: name, featureType, decisionDate] |
| **outputSRS** | **Integer**| The EPSG code of the spatial reference system (SRS) to use for output geometries. | [optional] [default to 4326] [enum: 4326, 4269, 3005, 3857, 26907, 26908, 26909, 26910, 26911] |
| **embed** | **Integer**| A flag to indicate whether to embed the corresponding &#39;feature&#39; into each matching name | [optional] [enum: 0, 1] |
| **outputStyle** | **String**| A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail) | [optional] [default to summary] [enum: summary, detail] |
| **itemsPerPage** | **Integer**| The number of search results to return (1-200) | [optional] [default to 20] |
| **startIndex** | **Integer**| The index of the first record to be returned (&gt;&#x3D; 1) | [optional] [default to 1] |

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
| **200** | A list of names matching the search criteria |  -  |
| **400** | A required parameter is missing or invalid |  -  |

<a id="namesInsideGet"></a>
# **namesInsideGet**
> namesInsideGet(outputFormat, bbox, featureClass, featureCategory, featureType, sortBy, outputSRS, embed, outputStyle, itemsPerPage, startIndex)

Search in a geographic area

Search for information about geographical names that correspond to features within a geographic bounding box.  Various options and filter parameters are available to refine the search.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apps.gov.bc.ca/pub/bcgnws");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String outputFormat = "json"; // String | The format of the output.
    String bbox = "-119,49,-118,50"; // String | A geographic bounding box defining the search area.  Must be specified as a string of the form 'minLongitude,minLatitude,maxLongitude,maxLatitude' (WGS84). e.g. -119,49,-118,50
    String featureClass = "*"; // String | A filter to limit the search to names associated with features of a certain 'class'  The value of this parameter should be a 'featureClassCode' value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included.
    String featureCategory = "*"; // String | A filter to limit the search to names associated with features of a certain 'category'  The value of this parameter should be a 'featureCategoryCode' value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included.
    String featureType = "*"; // String | A filter to limit the search to names associated with features of a certain 'type'  The value of this parameter should be a 'featureTypeCode' value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included
    String sortBy = "name"; // String | The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint.
    Integer outputSRS = 4326; // Integer | The EPSG code of the spatial reference system (SRS) to use for output geometries.
    Integer embed = 0; // Integer | A flag to indicate whether to embed the corresponding 'feature' into each matching name
    String outputStyle = "summary"; // String | A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail)
    Integer itemsPerPage = 20; // Integer | The number of search results to return (1-200)
    Integer startIndex = 1; // Integer | The index of the first record to be returned (>= 1)
    try {
      apiInstance.namesInsideGet(outputFormat, bbox, featureClass, featureCategory, featureType, sortBy, outputSRS, embed, outputStyle, itemsPerPage, startIndex);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#namesInsideGet");
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
| **outputFormat** | **String**| The format of the output. | [default to json] [enum: json, xml, kml, csv] |
| **bbox** | **String**| A geographic bounding box defining the search area.  Must be specified as a string of the form &#39;minLongitude,minLatitude,maxLongitude,maxLatitude&#39; (WGS84). e.g. -119,49,-118,50 | |
| **featureClass** | **String**| A filter to limit the search to names associated with features of a certain &#39;class&#39;  The value of this parameter should be a &#39;featureClassCode&#39; value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included. | [optional] [default to *] |
| **featureCategory** | **String**| A filter to limit the search to names associated with features of a certain &#39;category&#39;  The value of this parameter should be a &#39;featureCategoryCode&#39; value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included. | [optional] [default to *] |
| **featureType** | **String**| A filter to limit the search to names associated with features of a certain &#39;type&#39;  The value of this parameter should be a &#39;featureTypeCode&#39; value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included | [optional] [default to *] |
| **sortBy** | **String**| The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint. | [optional] [default to name] [enum: name, featureType, decisionDate] |
| **outputSRS** | **Integer**| The EPSG code of the spatial reference system (SRS) to use for output geometries. | [optional] [default to 4326] [enum: 4326, 4269, 3005, 3857, 26907, 26908, 26909, 26910, 26911] |
| **embed** | **Integer**| A flag to indicate whether to embed the corresponding &#39;feature&#39; into each matching name | [optional] [enum: 0, 1] |
| **outputStyle** | **String**| A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail) | [optional] [default to summary] [enum: summary, detail] |
| **itemsPerPage** | **Integer**| The number of search results to return (1-200) | [optional] [default to 20] |
| **startIndex** | **Integer**| The index of the first record to be returned (&gt;&#x3D; 1) | [optional] [default to 1] |

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
| **200** | A list of names matching the search criteria |  -  |
| **400** | A required parameter is missing or invalid |  -  |

<a id="namesNearGet"></a>
# **namesNearGet**
> namesNearGet(outputFormat, featurePoint, distance, featureClass, featureCategory, featureType, sortBy, outputSRS, embed, outputStyle, itemsPerPage, startIndex)

Search near to a geographic point

Search for information about geographical names that correspond to features within a geographic area defined by a centre point and a radius.  Various options and filter parameters are available to refine the search.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apps.gov.bc.ca/pub/bcgnws");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String outputFormat = "json"; // String | The format of the output.
    String featurePoint = "-120,51"; // String | A geographic coordinate specifying the centre point of the search area.  Must be specified as a string of the form 'longitude,latitude' (WGS84).  e.g. -120,51
    String distance = "distance_example"; // String | A radius (in kilometres) around the centre point.
    String featureClass = "*"; // String | A filter to limit the search to names associated with features of a certain 'class'  The value of this parameter should be a 'featureClassCode' value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included.
    String featureCategory = "*"; // String | A filter to limit the search to names associated with features of a certain 'category'  The value of this parameter should be a 'featureCategoryCode' value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included.
    String featureType = "*"; // String | A filter to limit the search to names associated with features of a certain 'type'  The value of this parameter should be a 'featureTypeCode' value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included
    String sortBy = "name"; // String | The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint.
    Integer outputSRS = 4326; // Integer | The EPSG code of the spatial reference system (SRS) to use for output geometries.
    Integer embed = 0; // Integer | A flag to indicate whether to embed the corresponding 'feature' into each matching name
    String outputStyle = "summary"; // String | A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail)
    Integer itemsPerPage = 20; // Integer | The number of search results to return (1-200)
    Integer startIndex = 1; // Integer | The index of the first record to be returned (>= 1)
    try {
      apiInstance.namesNearGet(outputFormat, featurePoint, distance, featureClass, featureCategory, featureType, sortBy, outputSRS, embed, outputStyle, itemsPerPage, startIndex);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#namesNearGet");
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
| **outputFormat** | **String**| The format of the output. | [default to json] [enum: json, xml, kml, csv] |
| **featurePoint** | **String**| A geographic coordinate specifying the centre point of the search area.  Must be specified as a string of the form &#39;longitude,latitude&#39; (WGS84).  e.g. -120,51 | |
| **distance** | **String**| A radius (in kilometres) around the centre point. | |
| **featureClass** | **String**| A filter to limit the search to names associated with features of a certain &#39;class&#39;  The value of this parameter should be a &#39;featureClassCode&#39; value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included. | [optional] [default to *] |
| **featureCategory** | **String**| A filter to limit the search to names associated with features of a certain &#39;category&#39;  The value of this parameter should be a &#39;featureCategoryCode&#39; value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included. | [optional] [default to *] |
| **featureType** | **String**| A filter to limit the search to names associated with features of a certain &#39;type&#39;  The value of this parameter should be a &#39;featureTypeCode&#39; value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included | [optional] [default to *] |
| **sortBy** | **String**| The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint. | [optional] [default to name] [enum: name, featureType, decisionDate] |
| **outputSRS** | **Integer**| The EPSG code of the spatial reference system (SRS) to use for output geometries. | [optional] [default to 4326] [enum: 4326, 4269, 3005, 3857, 26907, 26908, 26909, 26910, 26911] |
| **embed** | **Integer**| A flag to indicate whether to embed the corresponding &#39;feature&#39; into each matching name | [optional] [enum: 0, 1] |
| **outputStyle** | **String**| A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail) | [optional] [default to summary] [enum: summary, detail] |
| **itemsPerPage** | **Integer**| The number of search results to return (1-200) | [optional] [default to 20] |
| **startIndex** | **Integer**| The index of the first record to be returned (&gt;&#x3D; 1) | [optional] [default to 1] |

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
| **200** | A list of names matching the search criteria |  -  |
| **400** | A required parameter is missing or invalid |  -  |

<a id="namesNotOfficialSearchGet"></a>
# **namesNotOfficialSearchGet**
> namesNotOfficialSearchGet(outputFormat, name, exactSpelling, featureClass, featureCategory, featureType, sortBy, outputSRS, embed, outputStyle, itemsPerPage, startIndex)

Search by name, limit to unofficial names only

Search for information about unofficial geographical names by the text of the name itself.  Various options and filter parameters are available to refine the search.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apps.gov.bc.ca/pub/bcgnws");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String outputFormat = "json"; // String | The format of the output.
    String name = "Victoria"; // String | A filter to search based on the the text of the name itself.  Use the asterisk (*) as a wildcard character.  For example 'vancouv*'
    Integer exactSpelling = 0; // Integer | If the 'name' parameter is specified, 'exactSpelling' specifies whether to include only names that exactly match the search text (exactSpelling=1), or whether to also include names with similar spellings (exactSpelling=0)
    String featureClass = "*"; // String | A filter to limit the search to names associated with features of a certain 'class'  The value of this parameter should be a 'featureClassCode' value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included.
    String featureCategory = "*"; // String | A filter to limit the search to names associated with features of a certain 'category'  The value of this parameter should be a 'featureCategoryCode' value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included.
    String featureType = "*"; // String | A filter to limit the search to names associated with features of a certain 'type'  The value of this parameter should be a 'featureTypeCode' value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included
    String sortBy = "relevance"; // String | The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint.
    Integer outputSRS = 4326; // Integer | The EPSG code of the spatial reference system (SRS) to use for output geometries.
    Integer embed = 0; // Integer | A flag to indicate whether to embed the corresponding 'feature' into each matching name
    String outputStyle = "summary"; // String | A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail)
    Integer itemsPerPage = 20; // Integer | The number of search results to return (1-200)
    Integer startIndex = 1; // Integer | The index of the first record to be returned (>= 1)
    try {
      apiInstance.namesNotOfficialSearchGet(outputFormat, name, exactSpelling, featureClass, featureCategory, featureType, sortBy, outputSRS, embed, outputStyle, itemsPerPage, startIndex);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#namesNotOfficialSearchGet");
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
| **outputFormat** | **String**| The format of the output. | [default to json] [enum: json, xml, kml, csv] |
| **name** | **String**| A filter to search based on the the text of the name itself.  Use the asterisk (*) as a wildcard character.  For example &#39;vancouv*&#39; | |
| **exactSpelling** | **Integer**| If the &#39;name&#39; parameter is specified, &#39;exactSpelling&#39; specifies whether to include only names that exactly match the search text (exactSpelling&#x3D;1), or whether to also include names with similar spellings (exactSpelling&#x3D;0) | [optional] [default to 0] [enum: 0, 1] |
| **featureClass** | **String**| A filter to limit the search to names associated with features of a certain &#39;class&#39;  The value of this parameter should be a &#39;featureClassCode&#39; value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included. | [optional] [default to *] |
| **featureCategory** | **String**| A filter to limit the search to names associated with features of a certain &#39;category&#39;  The value of this parameter should be a &#39;featureCategoryCode&#39; value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included. | [optional] [default to *] |
| **featureType** | **String**| A filter to limit the search to names associated with features of a certain &#39;type&#39;  The value of this parameter should be a &#39;featureTypeCode&#39; value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included | [optional] [default to *] |
| **sortBy** | **String**| The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint. | [optional] [default to relevance] [enum: relevance, name, featureType, decisionDate] |
| **outputSRS** | **Integer**| The EPSG code of the spatial reference system (SRS) to use for output geometries. | [optional] [default to 4326] [enum: 4326, 4269, 3005, 3857, 26907, 26908, 26909, 26910, 26911] |
| **embed** | **Integer**| A flag to indicate whether to embed the corresponding &#39;feature&#39; into each matching name | [optional] [enum: 0, 1] |
| **outputStyle** | **String**| A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail) | [optional] [default to summary] [enum: summary, detail] |
| **itemsPerPage** | **Integer**| The number of search results to return (1-200) | [optional] [default to 20] |
| **startIndex** | **Integer**| The index of the first record to be returned (&gt;&#x3D; 1) | [optional] [default to 1] |

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
| **200** | A list of names matching the search criteria |  -  |
| **400** | A required parameter is missing or invalid |  -  |

<a id="namesOfficialSearchGet"></a>
# **namesOfficialSearchGet**
> namesOfficialSearchGet(outputFormat, name, exactSpelling, featureClass, featureCategory, featureType, sortBy, outputSRS, embed, outputStyle, itemsPerPage, startIndex)

Search by name, limit to official names only

Search for information about official geographical names by the text of the name itself.  Various options and filter parameters are available to refine the search.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apps.gov.bc.ca/pub/bcgnws");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String outputFormat = "json"; // String | The format of the output.
    String name = "Victoria"; // String | A filter to search based on the the text of the name itself.  Use the asterisk (*) as a wildcard character.  For example 'vancouv*'
    Integer exactSpelling = 0; // Integer | If the 'name' parameter is specified, 'exactSpelling' specifies whether to include only names that exactly match the search text (exactSpelling=1), or whether to also include names with similar spellings (exactSpelling=0)
    String featureClass = "*"; // String | A filter to limit the search to names associated with features of a certain 'class'  The value of this parameter should be a 'featureClassCode' value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included.
    String featureCategory = "*"; // String | A filter to limit the search to names associated with features of a certain 'category'  The value of this parameter should be a 'featureCategoryCode' value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included.
    String featureType = "*"; // String | A filter to limit the search to names associated with features of a certain 'type'  The value of this parameter should be a 'featureTypeCode' value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included
    String sortBy = "relevance"; // String | The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint.
    Integer outputSRS = 4326; // Integer | The EPSG code of the spatial reference system (SRS) to use for output geometries.
    Integer embed = 0; // Integer | A flag to indicate whether to embed the corresponding 'feature' into each matching name
    String outputStyle = "summary"; // String | A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail)
    Integer itemsPerPage = 20; // Integer | The number of search results to return (1-200)
    Integer startIndex = 1; // Integer | The index of the first record to be returned (>= 1)
    try {
      apiInstance.namesOfficialSearchGet(outputFormat, name, exactSpelling, featureClass, featureCategory, featureType, sortBy, outputSRS, embed, outputStyle, itemsPerPage, startIndex);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#namesOfficialSearchGet");
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
| **outputFormat** | **String**| The format of the output. | [default to json] [enum: json, xml, kml, csv] |
| **name** | **String**| A filter to search based on the the text of the name itself.  Use the asterisk (*) as a wildcard character.  For example &#39;vancouv*&#39; | |
| **exactSpelling** | **Integer**| If the &#39;name&#39; parameter is specified, &#39;exactSpelling&#39; specifies whether to include only names that exactly match the search text (exactSpelling&#x3D;1), or whether to also include names with similar spellings (exactSpelling&#x3D;0) | [optional] [default to 0] [enum: 0, 1] |
| **featureClass** | **String**| A filter to limit the search to names associated with features of a certain &#39;class&#39;  The value of this parameter should be a &#39;featureClassCode&#39; value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included. | [optional] [default to *] |
| **featureCategory** | **String**| A filter to limit the search to names associated with features of a certain &#39;category&#39;  The value of this parameter should be a &#39;featureCategoryCode&#39; value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included. | [optional] [default to *] |
| **featureType** | **String**| A filter to limit the search to names associated with features of a certain &#39;type&#39;  The value of this parameter should be a &#39;featureTypeCode&#39; value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included | [optional] [default to *] |
| **sortBy** | **String**| The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint. | [optional] [default to relevance] [enum: relevance, name, featureType, decisionDate] |
| **outputSRS** | **Integer**| The EPSG code of the spatial reference system (SRS) to use for output geometries. | [optional] [default to 4326] [enum: 4326, 4269, 3005, 3857, 26907, 26908, 26909, 26910, 26911] |
| **embed** | **Integer**| A flag to indicate whether to embed the corresponding &#39;feature&#39; into each matching name | [optional] [enum: 0, 1] |
| **outputStyle** | **String**| A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail) | [optional] [default to summary] [enum: summary, detail] |
| **itemsPerPage** | **Integer**| The number of search results to return (1-200) | [optional] [default to 20] |
| **startIndex** | **Integer**| The index of the first record to be returned (&gt;&#x3D; 1) | [optional] [default to 1] |

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
| **200** | A list of names matching the search criteria |  -  |
| **400** | A required parameter is missing or invalid |  -  |

<a id="namesSearchGet"></a>
# **namesSearchGet**
> namesSearchGet(outputFormat, name, exactSpelling, featureClass, featureCategory, featureType, sortBy, outputSRS, embed, outputStyle, itemsPerPage, startIndex)

Search by name

Search for information about geographical names by the text of the name itself.  The response will include both official and unofficial names.  Various options and filter parameters are available to refine the search.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apps.gov.bc.ca/pub/bcgnws");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String outputFormat = "json"; // String | The format of the output.
    String name = "Victoria"; // String | A filter to search based on the the text of the name itself.  Use the asterisk (*) as a wildcard character.  For example 'vancouv*'
    Integer exactSpelling = 0; // Integer | If the 'name' parameter is specified, 'exactSpelling' specifies whether to include only names that exactly match the search text (exactSpelling=1), or whether to also include names with similar spellings (exactSpelling=0)
    String featureClass = "*"; // String | A filter to limit the search to names associated with features of a certain 'class'  The value of this parameter should be a 'featureClassCode' value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included.
    String featureCategory = "*"; // String | A filter to limit the search to names associated with features of a certain 'category'  The value of this parameter should be a 'featureCategoryCode' value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included.
    String featureType = "*"; // String | A filter to limit the search to names associated with features of a certain 'type'  The value of this parameter should be a 'featureTypeCode' value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included
    String sortBy = "relevance"; // String | The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint.
    Integer outputSRS = 4326; // Integer | The EPSG code of the spatial reference system (SRS) to use for output geometries.
    Integer embed = 0; // Integer | A flag to indicate whether to embed the corresponding 'feature' into each matching name
    String outputStyle = "summary"; // String | A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail)
    Integer itemsPerPage = 20; // Integer | The number of search results to return (1-200)
    Integer startIndex = 1; // Integer | The index of the first record to be returned (>= 1)
    try {
      apiInstance.namesSearchGet(outputFormat, name, exactSpelling, featureClass, featureCategory, featureType, sortBy, outputSRS, embed, outputStyle, itemsPerPage, startIndex);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#namesSearchGet");
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
| **outputFormat** | **String**| The format of the output. | [default to json] [enum: json, xml, kml, csv] |
| **name** | **String**| A filter to search based on the the text of the name itself.  Use the asterisk (*) as a wildcard character.  For example &#39;vancouv*&#39; | |
| **exactSpelling** | **Integer**| If the &#39;name&#39; parameter is specified, &#39;exactSpelling&#39; specifies whether to include only names that exactly match the search text (exactSpelling&#x3D;1), or whether to also include names with similar spellings (exactSpelling&#x3D;0) | [optional] [default to 0] [enum: 0, 1] |
| **featureClass** | **String**| A filter to limit the search to names associated with features of a certain &#39;class&#39;  The value of this parameter should be a &#39;featureClassCode&#39; value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included. | [optional] [default to *] |
| **featureCategory** | **String**| A filter to limit the search to names associated with features of a certain &#39;category&#39;  The value of this parameter should be a &#39;featureCategoryCode&#39; value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included. | [optional] [default to *] |
| **featureType** | **String**| A filter to limit the search to names associated with features of a certain &#39;type&#39;  The value of this parameter should be a &#39;featureTypeCode&#39; value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included | [optional] [default to *] |
| **sortBy** | **String**| The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint. | [optional] [default to relevance] [enum: relevance, name, featureType, decisionDate] |
| **outputSRS** | **Integer**| The EPSG code of the spatial reference system (SRS) to use for output geometries. | [optional] [default to 4326] [enum: 4326, 4269, 3005, 3857, 26907, 26908, 26909, 26910, 26911] |
| **embed** | **Integer**| A flag to indicate whether to embed the corresponding &#39;feature&#39; into each matching name | [optional] [enum: 0, 1] |
| **outputStyle** | **String**| A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail) | [optional] [default to summary] [enum: summary, detail] |
| **itemsPerPage** | **Integer**| The number of search results to return (1-200) | [optional] [default to 20] |
| **startIndex** | **Integer**| The index of the first record to be returned (&gt;&#x3D; 1) | [optional] [default to 1] |

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
| **200** | A list of names matching the search criteria |  -  |
| **400** | A required parameter is missing or invalid |  -  |

