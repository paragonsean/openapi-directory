# V1Api

All URIs are relative to *http://openaq.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**citiesGetv1V1CitiesGet**](V1Api.md#citiesGetv1V1CitiesGet) | **GET** /v1/cities | Provides a simple listing of cities within the platform |
| [**countriesGetV1CountriesCountryIdGet**](V1Api.md#countriesGetV1CountriesCountryIdGet) | **GET** /v1/countries/{country_id} | Countries Get |
| [**countriesGetv1V1CountriesGet**](V1Api.md#countriesGetv1V1CountriesGet) | **GET** /v1/countries | Countries Getv1 |
| [**latestV1GetV1LatestGet**](V1Api.md#latestV1GetV1LatestGet) | **GET** /v1/latest | Latest V1 Get |
| [**latestV1GetV1LatestLocationIdGet**](V1Api.md#latestV1GetV1LatestLocationIdGet) | **GET** /v1/latest/{location_id} | Latest V1 Get |
| [**locationsv1GetV1LocationsGet**](V1Api.md#locationsv1GetV1LocationsGet) | **GET** /v1/locations | Locationsv1 Get |
| [**locationsv1GetV1LocationsLocationIdGet**](V1Api.md#locationsv1GetV1LocationsLocationIdGet) | **GET** /v1/locations/{location_id} | Locationsv1 Get |
| [**measurementsGetV1V1MeasurementsGet**](V1Api.md#measurementsGetV1V1MeasurementsGet) | **GET** /v1/measurements | Measurements Get V1 |
| [**parametersGetv1V1ParametersGet**](V1Api.md#parametersGetv1V1ParametersGet) | **GET** /v1/parameters | Parameters Getv1 |
| [**sourcesV1GetV1SourcesGet**](V1Api.md#sourcesV1GetV1SourcesGet) | **GET** /v1/sources | Sources V1 Get |


<a id="citiesGetv1V1CitiesGet"></a>
# **citiesGetv1V1CitiesGet**
> OpenAQCitiesResult citiesGetv1V1CitiesGet(limit, page, offset, sort, countryId, country, city, orderBy, entity)

Provides a simple listing of cities within the platform

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V1Api apiInstance = new V1Api(defaultClient);
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
      OpenAQCitiesResult result = apiInstance.citiesGetv1V1CitiesGet(limit, page, offset, sort, countryId, country, city, orderBy, entity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#citiesGetv1V1CitiesGet");
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

<a id="countriesGetV1CountriesCountryIdGet"></a>
# **countriesGetV1CountriesCountryIdGet**
> OpenAQCountriesResult countriesGetV1CountriesCountryIdGet(countryId, limit, page, offset, sort, country, orderBy)

Countries Get

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V1Api apiInstance = new V1Api(defaultClient);
    String countryId = "countryId_example"; // String | 
    Integer limit = 200; // Integer | 
    Integer page = 1; // Integer | Paginate through results.
    Integer offset = 0; // Integer | 
    Sort sort = Sort.fromValue("asc"); // Sort | Define sort order.
    List<String> country = Arrays.asList(); // List<String> |          Limit results by a certain country using two letter country code.         (ex. ?country=US or ?country=US&country=MX)         
    CountriesOrder orderBy = CountriesOrder.fromValue("country"); // CountriesOrder | 
    try {
      OpenAQCountriesResult result = apiInstance.countriesGetV1CountriesCountryIdGet(countryId, limit, page, offset, sort, country, orderBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#countriesGetV1CountriesCountryIdGet");
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

<a id="countriesGetv1V1CountriesGet"></a>
# **countriesGetv1V1CountriesGet**
> OpenAQCountriesResult countriesGetv1V1CountriesGet(limit, page, offset, sort, countryId, country, orderBy)

Countries Getv1

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V1Api apiInstance = new V1Api(defaultClient);
    Integer limit = 200; // Integer | 
    Integer page = 1; // Integer | Paginate through results.
    Integer offset = 0; // Integer | 
    Sort sort = Sort.fromValue("asc"); // Sort | Define sort order.
    String countryId = "countryId_example"; // String |          Limit results by a certain country using two letter country code.         (ex. /US)         
    List<String> country = Arrays.asList(); // List<String> |          Limit results by a certain country using two letter country code.         (ex. ?country=US or ?country=US&country=MX)         
    CountriesOrder orderBy = CountriesOrder.fromValue("country"); // CountriesOrder | 
    try {
      OpenAQCountriesResult result = apiInstance.countriesGetv1V1CountriesGet(limit, page, offset, sort, countryId, country, orderBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#countriesGetv1V1CountriesGet");
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

<a id="latestV1GetV1LatestGet"></a>
# **latestV1GetV1LatestGet**
> OpenAQResult latestV1GetV1LatestGet(limit, page, offset, sort, hasGeo, parameterId, parameter, unit, coordinates, radius, countryId, country, city, locationId, location, orderBy, isMobile, isAnalysis, sourceName, entity, sensorType, modelName, manufacturerName, dumpRaw)

Latest V1 Get

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V1Api apiInstance = new V1Api(defaultClient);
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
      OpenAQResult result = apiInstance.latestV1GetV1LatestGet(limit, page, offset, sort, hasGeo, parameterId, parameter, unit, coordinates, radius, countryId, country, city, locationId, location, orderBy, isMobile, isAnalysis, sourceName, entity, sensorType, modelName, manufacturerName, dumpRaw);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#latestV1GetV1LatestGet");
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

<a id="latestV1GetV1LatestLocationIdGet"></a>
# **latestV1GetV1LatestLocationIdGet**
> OpenAQResult latestV1GetV1LatestLocationIdGet(locationId, limit, page, offset, sort, hasGeo, parameterId, parameter, unit, coordinates, radius, countryId, country, city, location, orderBy, isMobile, isAnalysis, sourceName, entity, sensorType, modelName, manufacturerName, dumpRaw)

Latest V1 Get

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V1Api apiInstance = new V1Api(defaultClient);
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
      OpenAQResult result = apiInstance.latestV1GetV1LatestLocationIdGet(locationId, limit, page, offset, sort, hasGeo, parameterId, parameter, unit, coordinates, radius, countryId, country, city, location, orderBy, isMobile, isAnalysis, sourceName, entity, sensorType, modelName, manufacturerName, dumpRaw);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#latestV1GetV1LatestLocationIdGet");
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

<a id="locationsv1GetV1LocationsGet"></a>
# **locationsv1GetV1LocationsGet**
> OpenAQResult locationsv1GetV1LocationsGet(limit, page, offset, sort, hasGeo, parameterId, parameter, unit, coordinates, radius, countryId, country, city, locationId, location, orderBy, isMobile, isAnalysis, sourceName, entity, sensorType, modelName, manufacturerName, dumpRaw)

Locationsv1 Get

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V1Api apiInstance = new V1Api(defaultClient);
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
      OpenAQResult result = apiInstance.locationsv1GetV1LocationsGet(limit, page, offset, sort, hasGeo, parameterId, parameter, unit, coordinates, radius, countryId, country, city, locationId, location, orderBy, isMobile, isAnalysis, sourceName, entity, sensorType, modelName, manufacturerName, dumpRaw);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#locationsv1GetV1LocationsGet");
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

<a id="locationsv1GetV1LocationsLocationIdGet"></a>
# **locationsv1GetV1LocationsLocationIdGet**
> OpenAQResult locationsv1GetV1LocationsLocationIdGet(locationId, limit, page, offset, sort, hasGeo, parameterId, parameter, unit, coordinates, radius, countryId, country, city, location, orderBy, isMobile, isAnalysis, sourceName, entity, sensorType, modelName, manufacturerName, dumpRaw)

Locationsv1 Get

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V1Api apiInstance = new V1Api(defaultClient);
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
      OpenAQResult result = apiInstance.locationsv1GetV1LocationsLocationIdGet(locationId, limit, page, offset, sort, hasGeo, parameterId, parameter, unit, coordinates, radius, countryId, country, city, location, orderBy, isMobile, isAnalysis, sourceName, entity, sensorType, modelName, manufacturerName, dumpRaw);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#locationsv1GetV1LocationsLocationIdGet");
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

<a id="measurementsGetV1V1MeasurementsGet"></a>
# **measurementsGetV1V1MeasurementsGet**
> Object measurementsGetV1V1MeasurementsGet(format, dateFrom, dateTo, limit, page, offset, sort, hasGeo, parameterId, parameter, unit, coordinates, radius, countryId, country, city, locationId, location, orderBy, isMobile, isAnalysis, project, entity, sensorType, valueFrom, valueTo, includeFields)

Measurements Get V1

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V1Api apiInstance = new V1Api(defaultClient);
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
      Object result = apiInstance.measurementsGetV1V1MeasurementsGet(format, dateFrom, dateTo, limit, page, offset, sort, hasGeo, parameterId, parameter, unit, coordinates, radius, countryId, country, city, locationId, location, orderBy, isMobile, isAnalysis, project, entity, sensorType, valueFrom, valueTo, includeFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#measurementsGetV1V1MeasurementsGet");
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

<a id="parametersGetv1V1ParametersGet"></a>
# **parametersGetv1V1ParametersGet**
> OpenAQParametersResult parametersGetv1V1ParametersGet(limit, page, offset, sort, sourceName, sourceId, sourceSlug, orderBy)

Parameters Getv1

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V1Api apiInstance = new V1Api(defaultClient);
    Integer limit = 100; // Integer | Change the number of results returned.
    Integer page = 1; // Integer | Paginate through results.
    Integer offset = 0; // Integer | 
    Sort sort = Sort.fromValue("asc"); // Sort | Define sort order.
    List<String> sourceName = Arrays.asList(); // List<String> | 
    List<Integer> sourceId = Arrays.asList(); // List<Integer> | 
    List<String> sourceSlug = Arrays.asList(); // List<String> | 
    OrderBy orderBy = new OrderBy(); // OrderBy | 
    try {
      OpenAQParametersResult result = apiInstance.parametersGetv1V1ParametersGet(limit, page, offset, sort, sourceName, sourceId, sourceSlug, orderBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#parametersGetv1V1ParametersGet");
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

<a id="sourcesV1GetV1SourcesGet"></a>
# **sourcesV1GetV1SourcesGet**
> OpenAQResult sourcesV1GetV1SourcesGet(limit, page, offset, sort, name, orderBy)

Sources V1 Get

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    V1Api apiInstance = new V1Api(defaultClient);
    Integer limit = 100; // Integer | Change the number of results returned.
    Integer page = 1; // Integer | Paginate through results.
    Integer offset = 0; // Integer | 
    Sort sort = Sort.fromValue("asc"); // Sort | Define sort order.
    String name = "name_example"; // String | 
    SourcesV1Order orderBy = SourcesV1Order.fromValue("name"); // SourcesV1Order | 
    try {
      OpenAQResult result = apiInstance.sourcesV1GetV1SourcesGet(limit, page, offset, sort, name, orderBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#sourcesV1GetV1SourcesGet");
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
| **name** | **String**|  | [optional] |
| **orderBy** | [**SourcesV1Order**](.md)|  | [optional] [default to name] [enum: name] |

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

