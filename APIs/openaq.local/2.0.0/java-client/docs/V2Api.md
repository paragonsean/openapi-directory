# V2Api

All URIs are relative to *http://openaq.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**averagesV2GetV2AveragesGet**](V2Api.md#averagesV2GetV2AveragesGet) | **GET** /v2/averages | Averages V2 Get |
| [**citiesGetV2CitiesGet**](V2Api.md#citiesGetV2CitiesGet) | **GET** /v2/cities | Provides a simple listing of cities within the platform |
| [**countriesGetV2CountriesCountryIdGet**](V2Api.md#countriesGetV2CountriesCountryIdGet) | **GET** /v2/countries/{country_id} | Countries Get |
| [**countriesGetV2CountriesGet**](V2Api.md#countriesGetV2CountriesGet) | **GET** /v2/countries | Countries Get |
| [**demoV2LocationsTilesViewerGet**](V2Api.md#demoV2LocationsTilesViewerGet) | **GET** /v2/locations/tiles/viewer | Demo |
| [**getMobilegentileV2LocationsTilesMobileGeneralizedZXYPbfGet**](V2Api.md#getMobilegentileV2LocationsTilesMobileGeneralizedZXYPbfGet) | **GET** /v2/locations/tiles/mobile-generalized/{z}/{x}/{y}.pbf | Get Mobilegentile |
| [**getMobiletileV2LocationsTilesMobileZXYPbfGet**](V2Api.md#getMobiletileV2LocationsTilesMobileZXYPbfGet) | **GET** /v2/locations/tiles/mobile/{z}/{x}/{y}.pbf | Get Mobiletile |
| [**getTileV2LocationsTilesZXYPbfGet**](V2Api.md#getTileV2LocationsTilesZXYPbfGet) | **GET** /v2/locations/tiles/{z}/{x}/{y}.pbf | Get Tile |
| [**latestGetV2LatestGet**](V2Api.md#latestGetV2LatestGet) | **GET** /v2/latest | Latest Get |
| [**latestGetV2LatestLocationIdGet**](V2Api.md#latestGetV2LatestLocationIdGet) | **GET** /v2/latest/{location_id} | Latest Get |
| [**locationsGetV2LocationsGet**](V2Api.md#locationsGetV2LocationsGet) | **GET** /v2/locations | Locations Get |
| [**locationsGetV2LocationsLocationIdGet**](V2Api.md#locationsGetV2LocationsLocationIdGet) | **GET** /v2/locations/{location_id} | Locations Get |
| [**measurementsGetV2MeasurementsGet**](V2Api.md#measurementsGetV2MeasurementsGet) | **GET** /v2/measurements | Measurements Get |
| [**mfrGetV2ManufacturersGet**](V2Api.md#mfrGetV2ManufacturersGet) | **GET** /v2/manufacturers | Mfr Get |
| [**mobilegentilejsonV2LocationsTilesMobileGeneralizedTilesJsonGet**](V2Api.md#mobilegentilejsonV2LocationsTilesMobileGeneralizedTilesJsonGet) | **GET** /v2/locations/tiles/mobile-generalized/tiles.json | Mobilegentilejson |
| [**mobiletilejsonV2LocationsTilesMobileTilesJsonGet**](V2Api.md#mobiletilejsonV2LocationsTilesMobileTilesJsonGet) | **GET** /v2/locations/tiles/mobile/tiles.json | Mobiletilejson |
| [**modelGetV2ModelsGet**](V2Api.md#modelGetV2ModelsGet) | **GET** /v2/models | Model Get |
| [**parametersGetV2ParametersGet**](V2Api.md#parametersGetV2ParametersGet) | **GET** /v2/parameters | Parameters Get |
| [**projectsGetV2ProjectsGet**](V2Api.md#projectsGetV2ProjectsGet) | **GET** /v2/projects | Projects Get |
| [**projectsGetV2ProjectsProjectIdGet**](V2Api.md#projectsGetV2ProjectsProjectIdGet) | **GET** /v2/projects/{project_id} | Projects Get |
| [**readmeGetV2SourcesReadmeSlugGet**](V2Api.md#readmeGetV2SourcesReadmeSlugGet) | **GET** /v2/sources/readme/{slug} | Readme Get |
| [**sourcesGetV2SourcesGet**](V2Api.md#sourcesGetV2SourcesGet) | **GET** /v2/sources | Sources Get |
| [**summaryGetV2SummaryGet**](V2Api.md#summaryGetV2SummaryGet) | **GET** /v2/summary | Summary Get |
| [**tilejsonV2LocationsTilesTilesJsonGet**](V2Api.md#tilejsonV2LocationsTilesTilesJsonGet) | **GET** /v2/locations/tiles/tiles.json | Tilejson |


<a id="averagesV2GetV2AveragesGet"></a>
# **averagesV2GetV2AveragesGet**
> OpenAQResult averagesV2GetV2AveragesGet(spatial, temporal, dateFrom, dateTo, parameterId, parameter, unit, projectId, project, countryId, country, limit, page, offset, sort, location, group)

Averages V2 Get

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V2Api apiInstance = new V2Api(defaultClient);
    Spatial spatial = Spatial.fromValue("country"); // Spatial | 
    Temporal temporal = Temporal.fromValue("day"); // Temporal | 
    DateFrom dateFrom = new DateFrom(); // DateFrom | 
    DateTo dateTo = new DateTo(); // DateTo | 
    Integer parameterId = 56; // Integer | 
    List<ParameterInner> parameter = Arrays.asList(); // List<ParameterInner> | 
    List<String> unit = Arrays.asList(); // List<String> | 
    Integer projectId = 56; // Integer | 
    List<ParameterInner> project = Arrays.asList(); // List<ParameterInner> | 
    String countryId = "countryId_example"; // String |          Limit results by a certain country using two letter country code.         (ex. /US)         
    List<String> country = Arrays.asList(); // List<String> |          Limit results by a certain country using two letter country code.         (ex. ?country=US or ?country=US&country=MX)         
    Integer limit = 100; // Integer | Change the number of results returned.
    Integer page = 1; // Integer | Paginate through results.
    Integer offset = 0; // Integer | 
    Sort sort = Sort.fromValue("asc"); // Sort | Define sort order.
    List<String> location = Arrays.asList(); // List<String> | 
    Boolean group = false; // Boolean | 
    try {
      OpenAQResult result = apiInstance.averagesV2GetV2AveragesGet(spatial, temporal, dateFrom, dateTo, parameterId, parameter, unit, projectId, project, countryId, country, limit, page, offset, sort, location, group);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#averagesV2GetV2AveragesGet");
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
| **spatial** | [**Spatial**](.md)|  | [enum: country, location, project, total] |
| **temporal** | [**Temporal**](.md)|  | [enum: day, month, year, moy, dow, hour, hod] |
| **dateFrom** | [**DateFrom**](.md)|  | [optional] [default to 2000-01-01T00:00:00+00:00] |
| **dateTo** | [**DateTo**](.md)|  | [optional] [default to 2021-08-23T09:48:00+00:00] |
| **parameterId** | **Integer**|  | [optional] |
| **parameter** | [**List&lt;ParameterInner&gt;**](ParameterInner.md)|  | [optional] |
| **unit** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **projectId** | **Integer**|  | [optional] |
| **project** | [**List&lt;ParameterInner&gt;**](ParameterInner.md)|  | [optional] |
| **countryId** | **String**|          Limit results by a certain country using two letter country code.         (ex. /US)          | [optional] |
| **country** | [**List&lt;String&gt;**](String.md)|          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)          | [optional] |
| **limit** | **Integer**| Change the number of results returned. | [optional] [default to 100] |
| **page** | **Integer**| Paginate through results. | [optional] [default to 1] |
| **offset** | **Integer**|  | [optional] [default to 0] |
| **sort** | [**Sort**](.md)| Define sort order. | [optional] [default to desc] [enum: asc, desc] |
| **location** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **group** | **Boolean**|  | [optional] [default to false] |

### Return type

[**OpenAQResult**](OpenAQResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="citiesGetV2CitiesGet"></a>
# **citiesGetV2CitiesGet**
> OpenAQCitiesResult citiesGetV2CitiesGet(limit, page, offset, sort, countryId, country, city, orderBy, entity)

Provides a simple listing of cities within the platform

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V2Api apiInstance = new V2Api(defaultClient);
    Integer limit = 100; // Integer | Change the number of results returned.
    Integer page = 1; // Integer | Paginate through results.
    Integer offset = 0; // Integer | 
    Sort sort = Sort.fromValue("asc"); // Sort | Define sort order.
    String countryId = "countryId_example"; // String |          Limit results by a certain country using two letter country code.         (ex. /US)         
    List<String> country = Arrays.asList(); // List<String> |          Limit results by a certain country using two letter country code.         (ex. ?country=US or ?country=US&country=MX)         
    List<String> city = Arrays.asList(); // List<String> |          Limit results by a certain city or cities.         (ex. ?city=Chicago or ?city=Chicago&city=Boston)         
    CitiesOrder orderBy = CitiesOrder.fromValue("city"); // CitiesOrder | Order by a field
    String entity = "entity_example"; // String | 
    try {
      OpenAQCitiesResult result = apiInstance.citiesGetV2CitiesGet(limit, page, offset, sort, countryId, country, city, orderBy, entity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#citiesGetV2CitiesGet");
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
| **limit** | **Integer**| Change the number of results returned. | [optional] [default to 100] |
| **page** | **Integer**| Paginate through results. | [optional] [default to 1] |
| **offset** | **Integer**|  | [optional] [default to 0] |
| **sort** | [**Sort**](.md)| Define sort order. | [optional] [default to asc] [enum: asc, desc] |
| **countryId** | **String**|          Limit results by a certain country using two letter country code.         (ex. /US)          | [optional] |
| **country** | [**List&lt;String&gt;**](String.md)|          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)          | [optional] |
| **city** | [**List&lt;String&gt;**](String.md)|          Limit results by a certain city or cities.         (ex. ?city&#x3D;Chicago or ?city&#x3D;Chicago&amp;city&#x3D;Boston)          | [optional] |
| **orderBy** | [**CitiesOrder**](.md)| Order by a field | [optional] [default to city] [enum: city, country, firstUpdated, lastUpdated] |
| **entity** | **String**|  | [optional] |

### Return type

[**OpenAQCitiesResult**](OpenAQCitiesResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="countriesGetV2CountriesCountryIdGet"></a>
# **countriesGetV2CountriesCountryIdGet**
> OpenAQCountriesResult countriesGetV2CountriesCountryIdGet(countryId, limit, page, offset, sort, country, orderBy)

Countries Get

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V2Api apiInstance = new V2Api(defaultClient);
    String countryId = "countryId_example"; // String | 
    Integer limit = 200; // Integer | 
    Integer page = 1; // Integer | Paginate through results.
    Integer offset = 0; // Integer | 
    Sort sort = Sort.fromValue("asc"); // Sort | Define sort order.
    List<String> country = Arrays.asList(); // List<String> |          Limit results by a certain country using two letter country code.         (ex. ?country=US or ?country=US&country=MX)         
    CountriesOrder orderBy = CountriesOrder.fromValue("country"); // CountriesOrder | 
    try {
      OpenAQCountriesResult result = apiInstance.countriesGetV2CountriesCountryIdGet(countryId, limit, page, offset, sort, country, orderBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#countriesGetV2CountriesCountryIdGet");
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
| **countryId** | **String**|  | |
| **limit** | **Integer**|  | [optional] [default to 200] |
| **page** | **Integer**| Paginate through results. | [optional] [default to 1] |
| **offset** | **Integer**|  | [optional] [default to 0] |
| **sort** | [**Sort**](.md)| Define sort order. | [optional] [default to asc] [enum: asc, desc] |
| **country** | [**List&lt;String&gt;**](String.md)|          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)          | [optional] |
| **orderBy** | [**CountriesOrder**](.md)|  | [optional] [default to country] [enum: country, firstUpdated, lastUpdated, locations, count] |

### Return type

[**OpenAQCountriesResult**](OpenAQCountriesResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="countriesGetV2CountriesGet"></a>
# **countriesGetV2CountriesGet**
> OpenAQCountriesResult countriesGetV2CountriesGet(limit, page, offset, sort, countryId, country, orderBy)

Countries Get

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V2Api apiInstance = new V2Api(defaultClient);
    Integer limit = 200; // Integer | 
    Integer page = 1; // Integer | Paginate through results.
    Integer offset = 0; // Integer | 
    Sort sort = Sort.fromValue("asc"); // Sort | Define sort order.
    String countryId = "countryId_example"; // String |          Limit results by a certain country using two letter country code.         (ex. /US)         
    List<String> country = Arrays.asList(); // List<String> |          Limit results by a certain country using two letter country code.         (ex. ?country=US or ?country=US&country=MX)         
    CountriesOrder orderBy = CountriesOrder.fromValue("country"); // CountriesOrder | 
    try {
      OpenAQCountriesResult result = apiInstance.countriesGetV2CountriesGet(limit, page, offset, sort, countryId, country, orderBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#countriesGetV2CountriesGet");
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
| **limit** | **Integer**|  | [optional] [default to 200] |
| **page** | **Integer**| Paginate through results. | [optional] [default to 1] |
| **offset** | **Integer**|  | [optional] [default to 0] |
| **sort** | [**Sort**](.md)| Define sort order. | [optional] [default to asc] [enum: asc, desc] |
| **countryId** | **String**|          Limit results by a certain country using two letter country code.         (ex. /US)          | [optional] |
| **country** | [**List&lt;String&gt;**](String.md)|          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)          | [optional] |
| **orderBy** | [**CountriesOrder**](.md)|  | [optional] [default to country] [enum: country, firstUpdated, lastUpdated, locations, count] |

### Return type

[**OpenAQCountriesResult**](OpenAQCountriesResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="demoV2LocationsTilesViewerGet"></a>
# **demoV2LocationsTilesViewerGet**
> String demoV2LocationsTilesViewerGet()

Demo

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V2Api apiInstance = new V2Api(defaultClient);
    try {
      String result = apiInstance.demoV2LocationsTilesViewerGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#demoV2LocationsTilesViewerGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getMobilegentileV2LocationsTilesMobileGeneralizedZXYPbfGet"></a>
# **getMobilegentileV2LocationsTilesMobileGeneralizedZXYPbfGet**
> getMobilegentileV2LocationsTilesMobileGeneralizedZXYPbfGet(z, x, y, parameter, location, lastUpdatedFrom, lastUpdatedTo, isMobile, project, isAnalysis)

Get Mobilegentile

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V2Api apiInstance = new V2Api(defaultClient);
    Integer z = 56; // Integer | 
    Integer x = 56; // Integer | 
    Integer y = 56; // Integer | 
    Parameter parameter = new Parameter(); // Parameter | 
    List<Integer> location = Arrays.asList(); // List<Integer> | limit data to location id
    Lastupdatedfrom lastUpdatedFrom = new Lastupdatedfrom(); // Lastupdatedfrom | 
    Lastupdatedto lastUpdatedTo = new Lastupdatedto(); // Lastupdatedto | 
    Boolean isMobile = true; // Boolean | 
    Integer project = 56; // Integer | 
    Boolean isAnalysis = true; // Boolean | 
    try {
      apiInstance.getMobilegentileV2LocationsTilesMobileGeneralizedZXYPbfGet(z, x, y, parameter, location, lastUpdatedFrom, lastUpdatedTo, isMobile, project, isAnalysis);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#getMobilegentileV2LocationsTilesMobileGeneralizedZXYPbfGet");
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
| **z** | **Integer**|  | |
| **x** | **Integer**|  | |
| **y** | **Integer**|  | |
| **parameter** | [**Parameter**](.md)|  | [optional] |
| **location** | [**List&lt;Integer&gt;**](Integer.md)| limit data to location id | [optional] |
| **lastUpdatedFrom** | [**Lastupdatedfrom**](.md)|  | [optional] |
| **lastUpdatedTo** | [**Lastupdatedto**](.md)|  | [optional] |
| **isMobile** | **Boolean**|  | [optional] |
| **project** | **Integer**|  | [optional] |
| **isAnalysis** | **Boolean**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-protobuf, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="getMobiletileV2LocationsTilesMobileZXYPbfGet"></a>
# **getMobiletileV2LocationsTilesMobileZXYPbfGet**
> getMobiletileV2LocationsTilesMobileZXYPbfGet(z, x, y, dateFrom, dateTo, parameter, location, lastUpdatedFrom, lastUpdatedTo, isMobile, project, isAnalysis)

Get Mobiletile

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V2Api apiInstance = new V2Api(defaultClient);
    Integer z = 56; // Integer | 
    Integer x = 56; // Integer | 
    Integer y = 56; // Integer | 
    Datefrom dateFrom = new Datefrom(); // Datefrom | 
    Dateto dateTo = new Dateto(); // Dateto | 
    Parameter parameter = new Parameter(); // Parameter | 
    List<Integer> location = Arrays.asList(); // List<Integer> | limit data to location id
    Lastupdatedfrom lastUpdatedFrom = new Lastupdatedfrom(); // Lastupdatedfrom | 
    Lastupdatedto lastUpdatedTo = new Lastupdatedto(); // Lastupdatedto | 
    Boolean isMobile = true; // Boolean | 
    Integer project = 56; // Integer | 
    Boolean isAnalysis = true; // Boolean | 
    try {
      apiInstance.getMobiletileV2LocationsTilesMobileZXYPbfGet(z, x, y, dateFrom, dateTo, parameter, location, lastUpdatedFrom, lastUpdatedTo, isMobile, project, isAnalysis);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#getMobiletileV2LocationsTilesMobileZXYPbfGet");
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
| **z** | **Integer**|  | |
| **x** | **Integer**|  | |
| **y** | **Integer**|  | |
| **dateFrom** | [**Datefrom**](.md)|  | |
| **dateTo** | [**Dateto**](.md)|  | |
| **parameter** | [**Parameter**](.md)|  | [optional] |
| **location** | [**List&lt;Integer&gt;**](Integer.md)| limit data to location id | [optional] |
| **lastUpdatedFrom** | [**Lastupdatedfrom**](.md)|  | [optional] |
| **lastUpdatedTo** | [**Lastupdatedto**](.md)|  | [optional] |
| **isMobile** | **Boolean**|  | [optional] |
| **project** | **Integer**|  | [optional] |
| **isAnalysis** | **Boolean**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-protobuf, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="getTileV2LocationsTilesZXYPbfGet"></a>
# **getTileV2LocationsTilesZXYPbfGet**
> getTileV2LocationsTilesZXYPbfGet(z, x, y, parameter, location, lastUpdatedFrom, lastUpdatedTo, isMobile, project, isAnalysis)

Get Tile

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V2Api apiInstance = new V2Api(defaultClient);
    Integer z = 56; // Integer | 
    Integer x = 56; // Integer | 
    Integer y = 56; // Integer | 
    Parameter parameter = new Parameter(); // Parameter | 
    List<Integer> location = Arrays.asList(); // List<Integer> | limit data to location id
    Lastupdatedfrom lastUpdatedFrom = new Lastupdatedfrom(); // Lastupdatedfrom | 
    Lastupdatedto lastUpdatedTo = new Lastupdatedto(); // Lastupdatedto | 
    Boolean isMobile = true; // Boolean | 
    Integer project = 56; // Integer | 
    Boolean isAnalysis = true; // Boolean | 
    try {
      apiInstance.getTileV2LocationsTilesZXYPbfGet(z, x, y, parameter, location, lastUpdatedFrom, lastUpdatedTo, isMobile, project, isAnalysis);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#getTileV2LocationsTilesZXYPbfGet");
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
| **z** | **Integer**|  | |
| **x** | **Integer**|  | |
| **y** | **Integer**|  | |
| **parameter** | [**Parameter**](.md)|  | [optional] |
| **location** | [**List&lt;Integer&gt;**](Integer.md)| limit data to location id | [optional] |
| **lastUpdatedFrom** | [**Lastupdatedfrom**](.md)|  | [optional] |
| **lastUpdatedTo** | [**Lastupdatedto**](.md)|  | [optional] |
| **isMobile** | **Boolean**|  | [optional] |
| **project** | **Integer**|  | [optional] |
| **isAnalysis** | **Boolean**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-protobuf, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="latestGetV2LatestGet"></a>
# **latestGetV2LatestGet**
> OpenAQResult latestGetV2LatestGet(limit, page, offset, sort, hasGeo, parameterId, parameter, unit, coordinates, radius, countryId, country, city, locationId, location, orderBy, isMobile, isAnalysis, sourceName, entity, sensorType, modelName, manufacturerName, dumpRaw)

Latest Get

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V2Api apiInstance = new V2Api(defaultClient);
    Integer limit = 100; // Integer | Change the number of results returned.
    Integer page = 1; // Integer | Paginate through results.
    Integer offset = 0; // Integer | 
    Sort sort = Sort.fromValue("asc"); // Sort | Sort Direction
    Boolean hasGeo = true; // Boolean | 
    Integer parameterId = 56; // Integer | 
    List<ParameterInner> parameter = Arrays.asList(); // List<ParameterInner> | 
    List<String> unit = Arrays.asList(); // List<String> | 
    String coordinates = "coordinates_example"; // String | 
    Integer radius = 1000; // Integer | 
    String countryId = "countryId_example"; // String |          Limit results by a certain country using two letter country code.         (ex. /US)         
    List<String> country = Arrays.asList(); // List<String> |          Limit results by a certain country using two letter country code.         (ex. ?country=US or ?country=US&country=MX)         
    List<String> city = Arrays.asList(); // List<String> |          Limit results by a certain city or cities.         (ex. ?city=Chicago or ?city=Chicago&city=Boston)         
    Integer locationId = 56; // Integer | 
    List<LocationInner> location = Arrays.asList(); // List<LocationInner> | 
    LocationsOrder orderBy = LocationsOrder.fromValue("city"); // LocationsOrder | Order by a field
    Boolean isMobile = true; // Boolean | Location is mobile
    Boolean isAnalysis = true; // Boolean | Data is the product of a previous analysis/aggregation and not raw measurements
    List<String> sourceName = Arrays.asList(); // List<String> | Name of the data source
    EntityTypes entity = EntityTypes.fromValue("government"); // EntityTypes | Source entity type.
    SensorTypes sensorType = SensorTypes.fromValue("reference grade"); // SensorTypes | Type of Sensor
    List<String> modelName = Arrays.asList(); // List<String> | Model Name of Sensor
    List<String> manufacturerName = Arrays.asList(); // List<String> | Manufacturer of Sensor
    Boolean dumpRaw = false; // Boolean | 
    try {
      OpenAQResult result = apiInstance.latestGetV2LatestGet(limit, page, offset, sort, hasGeo, parameterId, parameter, unit, coordinates, radius, countryId, country, city, locationId, location, orderBy, isMobile, isAnalysis, sourceName, entity, sensorType, modelName, manufacturerName, dumpRaw);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#latestGetV2LatestGet");
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
| **limit** | **Integer**| Change the number of results returned. | [optional] [default to 100] |
| **page** | **Integer**| Paginate through results. | [optional] [default to 1] |
| **offset** | **Integer**|  | [optional] [default to 0] |
| **sort** | [**Sort**](.md)| Sort Direction | [optional] [default to desc] [enum: asc, desc] |
| **hasGeo** | **Boolean**|  | [optional] |
| **parameterId** | **Integer**|  | [optional] |
| **parameter** | [**List&lt;ParameterInner&gt;**](ParameterInner.md)|  | [optional] |
| **unit** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **coordinates** | **String**|  | [optional] |
| **radius** | **Integer**|  | [optional] [default to 1000] |
| **countryId** | **String**|          Limit results by a certain country using two letter country code.         (ex. /US)          | [optional] |
| **country** | [**List&lt;String&gt;**](String.md)|          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)          | [optional] |
| **city** | [**List&lt;String&gt;**](String.md)|          Limit results by a certain city or cities.         (ex. ?city&#x3D;Chicago or ?city&#x3D;Chicago&amp;city&#x3D;Boston)          | [optional] |
| **locationId** | **Integer**|  | [optional] |
| **location** | [**List&lt;LocationInner&gt;**](LocationInner.md)|  | [optional] |
| **orderBy** | [**LocationsOrder**](.md)| Order by a field | [optional] [default to lastUpdated] [enum: city, country, location, sourceName, firstUpdated, lastUpdated, count, random] |
| **isMobile** | **Boolean**| Location is mobile | [optional] |
| **isAnalysis** | **Boolean**| Data is the product of a previous analysis/aggregation and not raw measurements | [optional] |
| **sourceName** | [**List&lt;String&gt;**](String.md)| Name of the data source | [optional] |
| **entity** | [**EntityTypes**](.md)| Source entity type. | [optional] [enum: government, community, research] |
| **sensorType** | [**SensorTypes**](.md)| Type of Sensor | [optional] [enum: reference grade, low-cost sensor] |
| **modelName** | [**List&lt;String&gt;**](String.md)| Model Name of Sensor | [optional] |
| **manufacturerName** | [**List&lt;String&gt;**](String.md)| Manufacturer of Sensor | [optional] |
| **dumpRaw** | **Boolean**|  | [optional] [default to false] |

### Return type

[**OpenAQResult**](OpenAQResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="latestGetV2LatestLocationIdGet"></a>
# **latestGetV2LatestLocationIdGet**
> OpenAQResult latestGetV2LatestLocationIdGet(locationId, limit, page, offset, sort, hasGeo, parameterId, parameter, unit, coordinates, radius, countryId, country, city, location, orderBy, isMobile, isAnalysis, sourceName, entity, sensorType, modelName, manufacturerName, dumpRaw)

Latest Get

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V2Api apiInstance = new V2Api(defaultClient);
    Integer locationId = 56; // Integer | 
    Integer limit = 100; // Integer | Change the number of results returned.
    Integer page = 1; // Integer | Paginate through results.
    Integer offset = 0; // Integer | 
    Sort sort = Sort.fromValue("asc"); // Sort | Sort Direction
    Boolean hasGeo = true; // Boolean | 
    Integer parameterId = 56; // Integer | 
    List<ParameterInner> parameter = Arrays.asList(); // List<ParameterInner> | 
    List<String> unit = Arrays.asList(); // List<String> | 
    String coordinates = "coordinates_example"; // String | 
    Integer radius = 1000; // Integer | 
    String countryId = "countryId_example"; // String |          Limit results by a certain country using two letter country code.         (ex. /US)         
    List<String> country = Arrays.asList(); // List<String> |          Limit results by a certain country using two letter country code.         (ex. ?country=US or ?country=US&country=MX)         
    List<String> city = Arrays.asList(); // List<String> |          Limit results by a certain city or cities.         (ex. ?city=Chicago or ?city=Chicago&city=Boston)         
    List<LocationInner> location = Arrays.asList(); // List<LocationInner> | 
    LocationsOrder orderBy = LocationsOrder.fromValue("city"); // LocationsOrder | Order by a field
    Boolean isMobile = true; // Boolean | Location is mobile
    Boolean isAnalysis = true; // Boolean | Data is the product of a previous analysis/aggregation and not raw measurements
    List<String> sourceName = Arrays.asList(); // List<String> | Name of the data source
    EntityTypes entity = EntityTypes.fromValue("government"); // EntityTypes | Source entity type.
    SensorTypes sensorType = SensorTypes.fromValue("reference grade"); // SensorTypes | Type of Sensor
    List<String> modelName = Arrays.asList(); // List<String> | Model Name of Sensor
    List<String> manufacturerName = Arrays.asList(); // List<String> | Manufacturer of Sensor
    Boolean dumpRaw = false; // Boolean | 
    try {
      OpenAQResult result = apiInstance.latestGetV2LatestLocationIdGet(locationId, limit, page, offset, sort, hasGeo, parameterId, parameter, unit, coordinates, radius, countryId, country, city, location, orderBy, isMobile, isAnalysis, sourceName, entity, sensorType, modelName, manufacturerName, dumpRaw);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#latestGetV2LatestLocationIdGet");
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
| **locationId** | **Integer**|  | |
| **limit** | **Integer**| Change the number of results returned. | [optional] [default to 100] |
| **page** | **Integer**| Paginate through results. | [optional] [default to 1] |
| **offset** | **Integer**|  | [optional] [default to 0] |
| **sort** | [**Sort**](.md)| Sort Direction | [optional] [default to desc] [enum: asc, desc] |
| **hasGeo** | **Boolean**|  | [optional] |
| **parameterId** | **Integer**|  | [optional] |
| **parameter** | [**List&lt;ParameterInner&gt;**](ParameterInner.md)|  | [optional] |
| **unit** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **coordinates** | **String**|  | [optional] |
| **radius** | **Integer**|  | [optional] [default to 1000] |
| **countryId** | **String**|          Limit results by a certain country using two letter country code.         (ex. /US)          | [optional] |
| **country** | [**List&lt;String&gt;**](String.md)|          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)          | [optional] |
| **city** | [**List&lt;String&gt;**](String.md)|          Limit results by a certain city or cities.         (ex. ?city&#x3D;Chicago or ?city&#x3D;Chicago&amp;city&#x3D;Boston)          | [optional] |
| **location** | [**List&lt;LocationInner&gt;**](LocationInner.md)|  | [optional] |
| **orderBy** | [**LocationsOrder**](.md)| Order by a field | [optional] [default to lastUpdated] [enum: city, country, location, sourceName, firstUpdated, lastUpdated, count, random] |
| **isMobile** | **Boolean**| Location is mobile | [optional] |
| **isAnalysis** | **Boolean**| Data is the product of a previous analysis/aggregation and not raw measurements | [optional] |
| **sourceName** | [**List&lt;String&gt;**](String.md)| Name of the data source | [optional] |
| **entity** | [**EntityTypes**](.md)| Source entity type. | [optional] [enum: government, community, research] |
| **sensorType** | [**SensorTypes**](.md)| Type of Sensor | [optional] [enum: reference grade, low-cost sensor] |
| **modelName** | [**List&lt;String&gt;**](String.md)| Model Name of Sensor | [optional] |
| **manufacturerName** | [**List&lt;String&gt;**](String.md)| Manufacturer of Sensor | [optional] |
| **dumpRaw** | **Boolean**|  | [optional] [default to false] |

### Return type

[**OpenAQResult**](OpenAQResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="locationsGetV2LocationsGet"></a>
# **locationsGetV2LocationsGet**
> OpenAQResult locationsGetV2LocationsGet(limit, page, offset, sort, hasGeo, parameterId, parameter, unit, coordinates, radius, countryId, country, city, locationId, location, orderBy, isMobile, isAnalysis, sourceName, entity, sensorType, modelName, manufacturerName, dumpRaw)

Locations Get

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V2Api apiInstance = new V2Api(defaultClient);
    Integer limit = 100; // Integer | Change the number of results returned.
    Integer page = 1; // Integer | Paginate through results.
    Integer offset = 0; // Integer | 
    Sort sort = Sort.fromValue("asc"); // Sort | Sort Direction
    Boolean hasGeo = true; // Boolean | 
    Integer parameterId = 56; // Integer | 
    List<ParameterInner> parameter = Arrays.asList(); // List<ParameterInner> | 
    List<String> unit = Arrays.asList(); // List<String> | 
    String coordinates = "coordinates_example"; // String | 
    Integer radius = 1000; // Integer | 
    String countryId = "countryId_example"; // String |          Limit results by a certain country using two letter country code.         (ex. /US)         
    List<String> country = Arrays.asList(); // List<String> |          Limit results by a certain country using two letter country code.         (ex. ?country=US or ?country=US&country=MX)         
    List<String> city = Arrays.asList(); // List<String> |          Limit results by a certain city or cities.         (ex. ?city=Chicago or ?city=Chicago&city=Boston)         
    Integer locationId = 56; // Integer | 
    List<LocationInner> location = Arrays.asList(); // List<LocationInner> | 
    LocationsOrder orderBy = LocationsOrder.fromValue("city"); // LocationsOrder | Order by a field
    Boolean isMobile = true; // Boolean | Location is mobile
    Boolean isAnalysis = true; // Boolean | Data is the product of a previous analysis/aggregation and not raw measurements
    List<String> sourceName = Arrays.asList(); // List<String> | Name of the data source
    EntityTypes entity = EntityTypes.fromValue("government"); // EntityTypes | Source entity type.
    SensorTypes sensorType = SensorTypes.fromValue("reference grade"); // SensorTypes | Type of Sensor
    List<String> modelName = Arrays.asList(); // List<String> | Model Name of Sensor
    List<String> manufacturerName = Arrays.asList(); // List<String> | Manufacturer of Sensor
    Boolean dumpRaw = false; // Boolean | 
    try {
      OpenAQResult result = apiInstance.locationsGetV2LocationsGet(limit, page, offset, sort, hasGeo, parameterId, parameter, unit, coordinates, radius, countryId, country, city, locationId, location, orderBy, isMobile, isAnalysis, sourceName, entity, sensorType, modelName, manufacturerName, dumpRaw);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#locationsGetV2LocationsGet");
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
| **limit** | **Integer**| Change the number of results returned. | [optional] [default to 100] |
| **page** | **Integer**| Paginate through results. | [optional] [default to 1] |
| **offset** | **Integer**|  | [optional] [default to 0] |
| **sort** | [**Sort**](.md)| Sort Direction | [optional] [default to desc] [enum: asc, desc] |
| **hasGeo** | **Boolean**|  | [optional] |
| **parameterId** | **Integer**|  | [optional] |
| **parameter** | [**List&lt;ParameterInner&gt;**](ParameterInner.md)|  | [optional] |
| **unit** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **coordinates** | **String**|  | [optional] |
| **radius** | **Integer**|  | [optional] [default to 1000] |
| **countryId** | **String**|          Limit results by a certain country using two letter country code.         (ex. /US)          | [optional] |
| **country** | [**List&lt;String&gt;**](String.md)|          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)          | [optional] |
| **city** | [**List&lt;String&gt;**](String.md)|          Limit results by a certain city or cities.         (ex. ?city&#x3D;Chicago or ?city&#x3D;Chicago&amp;city&#x3D;Boston)          | [optional] |
| **locationId** | **Integer**|  | [optional] |
| **location** | [**List&lt;LocationInner&gt;**](LocationInner.md)|  | [optional] |
| **orderBy** | [**LocationsOrder**](.md)| Order by a field | [optional] [default to lastUpdated] [enum: city, country, location, sourceName, firstUpdated, lastUpdated, count, random] |
| **isMobile** | **Boolean**| Location is mobile | [optional] |
| **isAnalysis** | **Boolean**| Data is the product of a previous analysis/aggregation and not raw measurements | [optional] |
| **sourceName** | [**List&lt;String&gt;**](String.md)| Name of the data source | [optional] |
| **entity** | [**EntityTypes**](.md)| Source entity type. | [optional] [enum: government, community, research] |
| **sensorType** | [**SensorTypes**](.md)| Type of Sensor | [optional] [enum: reference grade, low-cost sensor] |
| **modelName** | [**List&lt;String&gt;**](String.md)| Model Name of Sensor | [optional] |
| **manufacturerName** | [**List&lt;String&gt;**](String.md)| Manufacturer of Sensor | [optional] |
| **dumpRaw** | **Boolean**|  | [optional] [default to false] |

### Return type

[**OpenAQResult**](OpenAQResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="locationsGetV2LocationsLocationIdGet"></a>
# **locationsGetV2LocationsLocationIdGet**
> OpenAQResult locationsGetV2LocationsLocationIdGet(locationId, limit, page, offset, sort, hasGeo, parameterId, parameter, unit, coordinates, radius, countryId, country, city, location, orderBy, isMobile, isAnalysis, sourceName, entity, sensorType, modelName, manufacturerName, dumpRaw)

Locations Get

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V2Api apiInstance = new V2Api(defaultClient);
    Integer locationId = 56; // Integer | 
    Integer limit = 100; // Integer | Change the number of results returned.
    Integer page = 1; // Integer | Paginate through results.
    Integer offset = 0; // Integer | 
    Sort sort = Sort.fromValue("asc"); // Sort | Sort Direction
    Boolean hasGeo = true; // Boolean | 
    Integer parameterId = 56; // Integer | 
    List<ParameterInner> parameter = Arrays.asList(); // List<ParameterInner> | 
    List<String> unit = Arrays.asList(); // List<String> | 
    String coordinates = "coordinates_example"; // String | 
    Integer radius = 1000; // Integer | 
    String countryId = "countryId_example"; // String |          Limit results by a certain country using two letter country code.         (ex. /US)         
    List<String> country = Arrays.asList(); // List<String> |          Limit results by a certain country using two letter country code.         (ex. ?country=US or ?country=US&country=MX)         
    List<String> city = Arrays.asList(); // List<String> |          Limit results by a certain city or cities.         (ex. ?city=Chicago or ?city=Chicago&city=Boston)         
    List<LocationInner> location = Arrays.asList(); // List<LocationInner> | 
    LocationsOrder orderBy = LocationsOrder.fromValue("city"); // LocationsOrder | Order by a field
    Boolean isMobile = true; // Boolean | Location is mobile
    Boolean isAnalysis = true; // Boolean | Data is the product of a previous analysis/aggregation and not raw measurements
    List<String> sourceName = Arrays.asList(); // List<String> | Name of the data source
    EntityTypes entity = EntityTypes.fromValue("government"); // EntityTypes | Source entity type.
    SensorTypes sensorType = SensorTypes.fromValue("reference grade"); // SensorTypes | Type of Sensor
    List<String> modelName = Arrays.asList(); // List<String> | Model Name of Sensor
    List<String> manufacturerName = Arrays.asList(); // List<String> | Manufacturer of Sensor
    Boolean dumpRaw = false; // Boolean | 
    try {
      OpenAQResult result = apiInstance.locationsGetV2LocationsLocationIdGet(locationId, limit, page, offset, sort, hasGeo, parameterId, parameter, unit, coordinates, radius, countryId, country, city, location, orderBy, isMobile, isAnalysis, sourceName, entity, sensorType, modelName, manufacturerName, dumpRaw);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#locationsGetV2LocationsLocationIdGet");
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
| **locationId** | **Integer**|  | |
| **limit** | **Integer**| Change the number of results returned. | [optional] [default to 100] |
| **page** | **Integer**| Paginate through results. | [optional] [default to 1] |
| **offset** | **Integer**|  | [optional] [default to 0] |
| **sort** | [**Sort**](.md)| Sort Direction | [optional] [default to desc] [enum: asc, desc] |
| **hasGeo** | **Boolean**|  | [optional] |
| **parameterId** | **Integer**|  | [optional] |
| **parameter** | [**List&lt;ParameterInner&gt;**](ParameterInner.md)|  | [optional] |
| **unit** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **coordinates** | **String**|  | [optional] |
| **radius** | **Integer**|  | [optional] [default to 1000] |
| **countryId** | **String**|          Limit results by a certain country using two letter country code.         (ex. /US)          | [optional] |
| **country** | [**List&lt;String&gt;**](String.md)|          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)          | [optional] |
| **city** | [**List&lt;String&gt;**](String.md)|          Limit results by a certain city or cities.         (ex. ?city&#x3D;Chicago or ?city&#x3D;Chicago&amp;city&#x3D;Boston)          | [optional] |
| **location** | [**List&lt;LocationInner&gt;**](LocationInner.md)|  | [optional] |
| **orderBy** | [**LocationsOrder**](.md)| Order by a field | [optional] [default to lastUpdated] [enum: city, country, location, sourceName, firstUpdated, lastUpdated, count, random] |
| **isMobile** | **Boolean**| Location is mobile | [optional] |
| **isAnalysis** | **Boolean**| Data is the product of a previous analysis/aggregation and not raw measurements | [optional] |
| **sourceName** | [**List&lt;String&gt;**](String.md)| Name of the data source | [optional] |
| **entity** | [**EntityTypes**](.md)| Source entity type. | [optional] [enum: government, community, research] |
| **sensorType** | [**SensorTypes**](.md)| Type of Sensor | [optional] [enum: reference grade, low-cost sensor] |
| **modelName** | [**List&lt;String&gt;**](String.md)| Model Name of Sensor | [optional] |
| **manufacturerName** | [**List&lt;String&gt;**](String.md)| Manufacturer of Sensor | [optional] |
| **dumpRaw** | **Boolean**|  | [optional] [default to false] |

### Return type

[**OpenAQResult**](OpenAQResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="measurementsGetV2MeasurementsGet"></a>
# **measurementsGetV2MeasurementsGet**
> Object measurementsGetV2MeasurementsGet(format, dateFrom, dateTo, limit, page, offset, sort, hasGeo, parameterId, parameter, unit, coordinates, radius, countryId, country, city, locationId, location, orderBy, isMobile, isAnalysis, project, entity, sensorType, valueFrom, valueTo, includeFields)

Measurements Get

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V2Api apiInstance = new V2Api(defaultClient);
    String format = "format_example"; // String | 
    DateFrom dateFrom = new DateFrom(); // DateFrom | 
    DateTo dateTo = new DateTo(); // DateTo | 
    Integer limit = 100; // Integer | Change the number of results returned.
    Integer page = 1; // Integer | Paginate through results.
    Integer offset = 0; // Integer | 
    Sort sort = Sort.fromValue("asc"); // Sort | 
    Boolean hasGeo = true; // Boolean | 
    Integer parameterId = 56; // Integer | 
    List<ParameterInner> parameter = Arrays.asList(); // List<ParameterInner> | 
    List<String> unit = Arrays.asList(); // List<String> | 
    String coordinates = "coordinates_example"; // String | 
    Integer radius = 1000; // Integer | 
    String countryId = "countryId_example"; // String |          Limit results by a certain country using two letter country code.         (ex. /US)         
    List<String> country = Arrays.asList(); // List<String> |          Limit results by a certain country using two letter country code.         (ex. ?country=US or ?country=US&country=MX)         
    List<String> city = Arrays.asList(); // List<String> |          Limit results by a certain city or cities.         (ex. ?city=Chicago or ?city=Chicago&city=Boston)         
    Integer locationId = 56; // Integer | 
    List<LocationInner> location = Arrays.asList(); // List<LocationInner> | 
    MeasOrder orderBy = MeasOrder.fromValue("city"); // MeasOrder | 
    Boolean isMobile = true; // Boolean | 
    Boolean isAnalysis = true; // Boolean | 
    Integer project = 56; // Integer | 
    EntityTypes entity = EntityTypes.fromValue("government"); // EntityTypes | 
    SensorTypes sensorType = SensorTypes.fromValue("reference grade"); // SensorTypes | 
    BigDecimal valueFrom = new BigDecimal(78); // BigDecimal | 
    BigDecimal valueTo = new BigDecimal(78); // BigDecimal | 
    String includeFields = "includeFields_example"; // String | 
    try {
      Object result = apiInstance.measurementsGetV2MeasurementsGet(format, dateFrom, dateTo, limit, page, offset, sort, hasGeo, parameterId, parameter, unit, coordinates, radius, countryId, country, city, locationId, location, orderBy, isMobile, isAnalysis, project, entity, sensorType, valueFrom, valueTo, includeFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#measurementsGetV2MeasurementsGet");
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
| **format** | **String**|  | [optional] |
| **dateFrom** | [**DateFrom**](.md)|  | [optional] [default to 2000-01-01T00:00:00+00:00] |
| **dateTo** | [**DateTo**](.md)|  | [optional] [default to 2021-08-23T09:48:00+00:00] |
| **limit** | **Integer**| Change the number of results returned. | [optional] [default to 100] |
| **page** | **Integer**| Paginate through results. | [optional] [default to 1] |
| **offset** | **Integer**|  | [optional] [default to 0] |
| **sort** | [**Sort**](.md)|  | [optional] [default to desc] [enum: asc, desc] |
| **hasGeo** | **Boolean**|  | [optional] |
| **parameterId** | **Integer**|  | [optional] |
| **parameter** | [**List&lt;ParameterInner&gt;**](ParameterInner.md)|  | [optional] |
| **unit** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **coordinates** | **String**|  | [optional] |
| **radius** | **Integer**|  | [optional] [default to 1000] |
| **countryId** | **String**|          Limit results by a certain country using two letter country code.         (ex. /US)          | [optional] |
| **country** | [**List&lt;String&gt;**](String.md)|          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)          | [optional] |
| **city** | [**List&lt;String&gt;**](String.md)|          Limit results by a certain city or cities.         (ex. ?city&#x3D;Chicago or ?city&#x3D;Chicago&amp;city&#x3D;Boston)          | [optional] |
| **locationId** | **Integer**|  | [optional] |
| **location** | [**List&lt;LocationInner&gt;**](LocationInner.md)|  | [optional] |
| **orderBy** | [**MeasOrder**](.md)|  | [optional] [default to datetime] [enum: city, country, location, datetime] |
| **isMobile** | **Boolean**|  | [optional] |
| **isAnalysis** | **Boolean**|  | [optional] |
| **project** | **Integer**|  | [optional] |
| **entity** | [**EntityTypes**](.md)|  | [optional] [enum: government, community, research] |
| **sensorType** | [**SensorTypes**](.md)|  | [optional] [enum: reference grade, low-cost sensor] |
| **valueFrom** | **BigDecimal**|  | [optional] |
| **valueTo** | **BigDecimal**|  | [optional] |
| **includeFields** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="mfrGetV2ManufacturersGet"></a>
# **mfrGetV2ManufacturersGet**
> OpenAQResult mfrGetV2ManufacturersGet()

Mfr Get

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V2Api apiInstance = new V2Api(defaultClient);
    try {
      OpenAQResult result = apiInstance.mfrGetV2ManufacturersGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#mfrGetV2ManufacturersGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OpenAQResult**](OpenAQResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="mobilegentilejsonV2LocationsTilesMobileGeneralizedTilesJsonGet"></a>
# **mobilegentilejsonV2LocationsTilesMobileGeneralizedTilesJsonGet**
> TileJSON mobilegentilejsonV2LocationsTilesMobileGeneralizedTilesJsonGet()

Mobilegentilejson

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V2Api apiInstance = new V2Api(defaultClient);
    try {
      TileJSON result = apiInstance.mobilegentilejsonV2LocationsTilesMobileGeneralizedTilesJsonGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#mobilegentilejsonV2LocationsTilesMobileGeneralizedTilesJsonGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TileJSON**](TileJSON.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return a tilejson |  -  |

<a id="mobiletilejsonV2LocationsTilesMobileTilesJsonGet"></a>
# **mobiletilejsonV2LocationsTilesMobileTilesJsonGet**
> TileJSON mobiletilejsonV2LocationsTilesMobileTilesJsonGet()

Mobiletilejson

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V2Api apiInstance = new V2Api(defaultClient);
    try {
      TileJSON result = apiInstance.mobiletilejsonV2LocationsTilesMobileTilesJsonGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#mobiletilejsonV2LocationsTilesMobileTilesJsonGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TileJSON**](TileJSON.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return a tilejson |  -  |

<a id="modelGetV2ModelsGet"></a>
# **modelGetV2ModelsGet**
> OpenAQResult modelGetV2ModelsGet()

Model Get

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V2Api apiInstance = new V2Api(defaultClient);
    try {
      OpenAQResult result = apiInstance.modelGetV2ModelsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#modelGetV2ModelsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OpenAQResult**](OpenAQResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="parametersGetV2ParametersGet"></a>
# **parametersGetV2ParametersGet**
> OpenAQParametersResult parametersGetV2ParametersGet(limit, page, offset, sort, sourceName, sourceId, sourceSlug, orderBy)

Parameters Get

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V2Api apiInstance = new V2Api(defaultClient);
    Integer limit = 100; // Integer | Change the number of results returned.
    Integer page = 1; // Integer | Paginate through results.
    Integer offset = 0; // Integer | 
    Sort sort = Sort.fromValue("asc"); // Sort | Define sort order.
    List<String> sourceName = Arrays.asList(); // List<String> | 
    List<Integer> sourceId = Arrays.asList(); // List<Integer> | 
    List<String> sourceSlug = Arrays.asList(); // List<String> | 
    OrderBy orderBy = new OrderBy(); // OrderBy | 
    try {
      OpenAQParametersResult result = apiInstance.parametersGetV2ParametersGet(limit, page, offset, sort, sourceName, sourceId, sourceSlug, orderBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#parametersGetV2ParametersGet");
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
| **limit** | **Integer**| Change the number of results returned. | [optional] [default to 100] |
| **page** | **Integer**| Paginate through results. | [optional] [default to 1] |
| **offset** | **Integer**|  | [optional] [default to 0] |
| **sort** | [**Sort**](.md)| Define sort order. | [optional] [default to asc] [enum: asc, desc] |
| **sourceName** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **sourceId** | [**List&lt;Integer&gt;**](Integer.md)|  | [optional] |
| **sourceSlug** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **orderBy** | [**OrderBy**](.md)|  | [optional] [default to id] |

### Return type

[**OpenAQParametersResult**](OpenAQParametersResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="projectsGetV2ProjectsGet"></a>
# **projectsGetV2ProjectsGet**
> OpenAQProjectsResult projectsGetV2ProjectsGet(countryId, country, limit, page, offset, sort, parameterId, parameter, unit, projectId, project, orderBy, isMobile, isAnalysis, entity, sensorType, sourceName)

Projects Get

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V2Api apiInstance = new V2Api(defaultClient);
    String countryId = "countryId_example"; // String |          Limit results by a certain country using two letter country code.         (ex. /US)         
    List<String> country = Arrays.asList(); // List<String> |          Limit results by a certain country using two letter country code.         (ex. ?country=US or ?country=US&country=MX)         
    Integer limit = 100; // Integer | Change the number of results returned.
    Integer page = 1; // Integer | Paginate through results.
    Integer offset = 0; // Integer | 
    Sort sort = Sort.fromValue("asc"); // Sort | Define sort order.
    Integer parameterId = 56; // Integer | 
    List<ParameterInner> parameter = Arrays.asList(); // List<ParameterInner> | 
    List<String> unit = Arrays.asList(); // List<String> | 
    Integer projectId = 56; // Integer | 
    List<ParameterInner> project = Arrays.asList(); // List<ParameterInner> | 
    ProjectsOrder orderBy = ProjectsOrder.fromValue("id"); // ProjectsOrder | 
    Boolean isMobile = true; // Boolean | 
    Boolean isAnalysis = true; // Boolean | 
    String entity = "entity_example"; // String | 
    String sensorType = "sensorType_example"; // String | 
    List<String> sourceName = Arrays.asList(); // List<String> | 
    try {
      OpenAQProjectsResult result = apiInstance.projectsGetV2ProjectsGet(countryId, country, limit, page, offset, sort, parameterId, parameter, unit, projectId, project, orderBy, isMobile, isAnalysis, entity, sensorType, sourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#projectsGetV2ProjectsGet");
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
| **countryId** | **String**|          Limit results by a certain country using two letter country code.         (ex. /US)          | [optional] |
| **country** | [**List&lt;String&gt;**](String.md)|          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)          | [optional] |
| **limit** | **Integer**| Change the number of results returned. | [optional] [default to 100] |
| **page** | **Integer**| Paginate through results. | [optional] [default to 1] |
| **offset** | **Integer**|  | [optional] [default to 0] |
| **sort** | [**Sort**](.md)| Define sort order. | [optional] [default to asc] [enum: asc, desc] |
| **parameterId** | **Integer**|  | [optional] |
| **parameter** | [**List&lt;ParameterInner&gt;**](ParameterInner.md)|  | [optional] |
| **unit** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **projectId** | **Integer**|  | [optional] |
| **project** | [**List&lt;ParameterInner&gt;**](ParameterInner.md)|  | [optional] |
| **orderBy** | [**ProjectsOrder**](.md)|  | [optional] [default to lastUpdated] [enum: id, name, subtitle, firstUpdated, lastUpdated] |
| **isMobile** | **Boolean**|  | [optional] |
| **isAnalysis** | **Boolean**|  | [optional] |
| **entity** | **String**|  | [optional] |
| **sensorType** | **String**|  | [optional] |
| **sourceName** | [**List&lt;String&gt;**](String.md)|  | [optional] |

### Return type

[**OpenAQProjectsResult**](OpenAQProjectsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="projectsGetV2ProjectsProjectIdGet"></a>
# **projectsGetV2ProjectsProjectIdGet**
> OpenAQProjectsResult projectsGetV2ProjectsProjectIdGet(projectId, countryId, country, limit, page, offset, sort, parameterId, parameter, unit, project, orderBy, isMobile, isAnalysis, entity, sensorType, sourceName)

Projects Get

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V2Api apiInstance = new V2Api(defaultClient);
    Integer projectId = 56; // Integer | 
    String countryId = "countryId_example"; // String |          Limit results by a certain country using two letter country code.         (ex. /US)         
    List<String> country = Arrays.asList(); // List<String> |          Limit results by a certain country using two letter country code.         (ex. ?country=US or ?country=US&country=MX)         
    Integer limit = 100; // Integer | Change the number of results returned.
    Integer page = 1; // Integer | Paginate through results.
    Integer offset = 0; // Integer | 
    Sort sort = Sort.fromValue("asc"); // Sort | Define sort order.
    Integer parameterId = 56; // Integer | 
    List<ParameterInner> parameter = Arrays.asList(); // List<ParameterInner> | 
    List<String> unit = Arrays.asList(); // List<String> | 
    List<ParameterInner> project = Arrays.asList(); // List<ParameterInner> | 
    ProjectsOrder orderBy = ProjectsOrder.fromValue("id"); // ProjectsOrder | 
    Boolean isMobile = true; // Boolean | 
    Boolean isAnalysis = true; // Boolean | 
    String entity = "entity_example"; // String | 
    String sensorType = "sensorType_example"; // String | 
    List<String> sourceName = Arrays.asList(); // List<String> | 
    try {
      OpenAQProjectsResult result = apiInstance.projectsGetV2ProjectsProjectIdGet(projectId, countryId, country, limit, page, offset, sort, parameterId, parameter, unit, project, orderBy, isMobile, isAnalysis, entity, sensorType, sourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#projectsGetV2ProjectsProjectIdGet");
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
| **projectId** | **Integer**|  | |
| **countryId** | **String**|          Limit results by a certain country using two letter country code.         (ex. /US)          | [optional] |
| **country** | [**List&lt;String&gt;**](String.md)|          Limit results by a certain country using two letter country code.         (ex. ?country&#x3D;US or ?country&#x3D;US&amp;country&#x3D;MX)          | [optional] |
| **limit** | **Integer**| Change the number of results returned. | [optional] [default to 100] |
| **page** | **Integer**| Paginate through results. | [optional] [default to 1] |
| **offset** | **Integer**|  | [optional] [default to 0] |
| **sort** | [**Sort**](.md)| Define sort order. | [optional] [default to asc] [enum: asc, desc] |
| **parameterId** | **Integer**|  | [optional] |
| **parameter** | [**List&lt;ParameterInner&gt;**](ParameterInner.md)|  | [optional] |
| **unit** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **project** | [**List&lt;ParameterInner&gt;**](ParameterInner.md)|  | [optional] |
| **orderBy** | [**ProjectsOrder**](.md)|  | [optional] [default to lastUpdated] [enum: id, name, subtitle, firstUpdated, lastUpdated] |
| **isMobile** | **Boolean**|  | [optional] |
| **isAnalysis** | **Boolean**|  | [optional] |
| **entity** | **String**|  | [optional] |
| **sensorType** | **String**|  | [optional] |
| **sourceName** | [**List&lt;String&gt;**](String.md)|  | [optional] |

### Return type

[**OpenAQProjectsResult**](OpenAQProjectsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="readmeGetV2SourcesReadmeSlugGet"></a>
# **readmeGetV2SourcesReadmeSlugGet**
> Object readmeGetV2SourcesReadmeSlugGet(slug)

Readme Get

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V2Api apiInstance = new V2Api(defaultClient);
    String slug = "slug_example"; // String | 
    try {
      Object result = apiInstance.readmeGetV2SourcesReadmeSlugGet(slug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#readmeGetV2SourcesReadmeSlugGet");
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
| **slug** | **String**|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="sourcesGetV2SourcesGet"></a>
# **sourcesGetV2SourcesGet**
> OpenAQResult sourcesGetV2SourcesGet(limit, page, offset, sort, sourceName, sourceId, sourceSlug, orderBy)

Sources Get

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V2Api apiInstance = new V2Api(defaultClient);
    Integer limit = 100; // Integer | Change the number of results returned.
    Integer page = 1; // Integer | Paginate through results.
    Integer offset = 0; // Integer | 
    Sort sort = Sort.fromValue("asc"); // Sort | Define sort order.
    List<String> sourceName = Arrays.asList(); // List<String> | 
    List<Integer> sourceId = Arrays.asList(); // List<Integer> | 
    List<String> sourceSlug = Arrays.asList(); // List<String> | 
    SourcesOrder orderBy = SourcesOrder.fromValue("sourceName"); // SourcesOrder | 
    try {
      OpenAQResult result = apiInstance.sourcesGetV2SourcesGet(limit, page, offset, sort, sourceName, sourceId, sourceSlug, orderBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#sourcesGetV2SourcesGet");
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
| **limit** | **Integer**| Change the number of results returned. | [optional] [default to 100] |
| **page** | **Integer**| Paginate through results. | [optional] [default to 1] |
| **offset** | **Integer**|  | [optional] [default to 0] |
| **sort** | [**Sort**](.md)| Define sort order. | [optional] [default to asc] [enum: asc, desc] |
| **sourceName** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **sourceId** | [**List&lt;Integer&gt;**](Integer.md)|  | [optional] |
| **sourceSlug** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **orderBy** | [**SourcesOrder**](.md)|  | [optional] [default to sourceName] [enum: sourceName, firstUpdated, lastUpdated] |

### Return type

[**OpenAQResult**](OpenAQResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="summaryGetV2SummaryGet"></a>
# **summaryGetV2SummaryGet**
> OpenAQResult summaryGetV2SummaryGet()

Summary Get

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V2Api apiInstance = new V2Api(defaultClient);
    try {
      OpenAQResult result = apiInstance.summaryGetV2SummaryGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#summaryGetV2SummaryGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OpenAQResult**](OpenAQResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="tilejsonV2LocationsTilesTilesJsonGet"></a>
# **tilejsonV2LocationsTilesTilesJsonGet**
> TileJSON tilejsonV2LocationsTilesTilesJsonGet()

Tilejson

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V2Api apiInstance = new V2Api(defaultClient);
    try {
      TileJSON result = apiInstance.tilejsonV2LocationsTilesTilesJsonGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#tilejsonV2LocationsTilesTilesJsonGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TileJSON**](TileJSON.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return a tilejson |  -  |

