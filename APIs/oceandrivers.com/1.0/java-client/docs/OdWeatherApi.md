# OdWeatherApi

All URIs are relative to *https://api.oceandrivers.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**compareStation**](OdWeatherApi.md#compareStation) | **GET** /v1.0/compareStation/{stationName}/ |  |
| [**getAemetStation**](OdWeatherApi.md#getAemetStation) | **GET** /v1.0/getAemetStation/{stationName}/{period}/ |  |
| [**getEasywind**](OdWeatherApi.md#getEasywind) | **GET** /v1.0/getEasyWind/{easywindId}/ |  |
| [**getEventStations**](OdWeatherApi.md#getEventStations) | **GET** /v1.0/getEventStations/{eventId}/ |  |
| [**getForecastPoints**](OdWeatherApi.md#getForecastPoints) | **GET** /v1.0/getForecastPoints/{yatchclubid}/language/{language} |  |
| [**getForecastTimeSeries**](OdWeatherApi.md#getForecastTimeSeries) | **GET** /v1.0/getForecastTimeSeries/{latitude}/{longitude}/ |  |
| [**getForecastTimeSeriesWrf**](OdWeatherApi.md#getForecastTimeSeriesWrf) | **GET** /v1.0/getForecastTimeSeriesWrf/{latitude}/{longitude}/ |  |
| [**getSocibWeatherStation**](OdWeatherApi.md#getSocibWeatherStation) | **GET** /v1.0/getSocibWeatherStation/{stationName}/{period}/ |  |
| [**getWeatherDisplay**](OdWeatherApi.md#getWeatherDisplay) | **GET** /v1.0/getWeatherDisplay/{stationName}/ |  |
| [**getWebCams**](OdWeatherApi.md#getWebCams) | **GET** /v1.0/getWebCams/ |  |


<a id="compareStation"></a>
# **compareStation**
> compareStation(stationName)



Get forecast and realtime information for known points&lt;br/&gt;None

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OdWeatherApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.oceandrivers.com");

    OdWeatherApi apiInstance = new OdWeatherApi(defaultClient);
    String stationName = "cnarenal"; // String | Weather station to compare, values: cnareanl|rcnp | cmsap|boyaenderrocat|areopuertopalma | EWXXX
    try {
      apiInstance.compareStation(stationName);
    } catch (ApiException e) {
      System.err.println("Exception when calling OdWeatherApi#compareStation");
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
| **stationName** | **String**| Weather station to compare, values: cnareanl|rcnp | cmsap|boyaenderrocat|areopuertopalma | EWXXX | [default to cnarenal] |

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

<a id="getAemetStation"></a>
# **getAemetStation**
> getAemetStation(stationName, period)



Get data from the aemet stations&lt;br/&gt;None

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OdWeatherApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.oceandrivers.com");

    OdWeatherApi apiInstance = new OdWeatherApi(defaultClient);
    String stationName = "aeropuertopalma"; // String | station name currently: aeropuertopalma | caboblanco 
    String period = "lastdata"; // String | Period of time to get the data. Options: lastdata lastday
    try {
      apiInstance.getAemetStation(stationName, period);
    } catch (ApiException e) {
      System.err.println("Exception when calling OdWeatherApi#getAemetStation");
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
| **stationName** | **String**| station name currently: aeropuertopalma | caboblanco  | [default to aeropuertopalma] |
| **period** | **String**| Period of time to get the data. Options: lastdata lastday | [default to lastdata] |

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

<a id="getEasywind"></a>
# **getEasywind**
> getEasywind(easywindId, period)



Get data from the easywind weather stations&lt;br/&gt;None

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OdWeatherApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.oceandrivers.com");

    OdWeatherApi apiInstance = new OdWeatherApi(defaultClient);
    String easywindId = "EW013"; // String | currently: 'EW013'|'EW008'
    String period = "latestdata"; // String | Period of time to get the data latestdata|latesthour|latestday
    try {
      apiInstance.getEasywind(easywindId, period);
    } catch (ApiException e) {
      System.err.println("Exception when calling OdWeatherApi#getEasywind");
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
| **easywindId** | **String**| currently: &#39;EW013&#39;|&#39;EW008&#39; | [default to EW013] |
| **period** | **String**| Period of time to get the data latestdata|latesthour|latestday | [default to latestdata] |

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

<a id="getEventStations"></a>
# **getEventStations**
> getEventStations(eventId)



Get stations in an event&lt;br/&gt;None

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OdWeatherApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.oceandrivers.com");

    OdWeatherApi apiInstance = new OdWeatherApi(defaultClient);
    String eventId = "trofeoprincesasofia"; // String | currently: 'trofeoprincesasofia|palmavela'
    try {
      apiInstance.getEventStations(eventId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OdWeatherApi#getEventStations");
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
| **eventId** | **String**| currently: &#39;trofeoprincesasofia|palmavela&#39; | [default to trofeoprincesasofia] |

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

<a id="getForecastPoints"></a>
# **getForecastPoints**
> getForecastPoints(yatchclubid, language)



Get forecast points of a yatchclub&lt;br/&gt;None

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OdWeatherApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.oceandrivers.com");

    OdWeatherApi apiInstance = new OdWeatherApi(defaultClient);
    String yatchclubid = "cnarenal"; // String | base URL for the the
    String language = "language_example"; // String | 
    try {
      apiInstance.getForecastPoints(yatchclubid, language);
    } catch (ApiException e) {
      System.err.println("Exception when calling OdWeatherApi#getForecastPoints");
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
| **yatchclubid** | **String**| base URL for the the | [default to cnarenal] |
| **language** | **String**|  | |

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

<a id="getForecastTimeSeries"></a>
# **getForecastTimeSeries**
> getForecastTimeSeries(latitude, longitude, weather, inittime, endtime, days, hours, wave, entryid)



Get timeseries forecast information&lt;br/&gt;None

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OdWeatherApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.oceandrivers.com");

    OdWeatherApi apiInstance = new OdWeatherApi(defaultClient);
    Float latitude = 39.49F; // Float | latitude for the forecast
    Float longitude = 2.74F; // Float | longitude for the forecast
    String weather = "weather_example"; // String |  Comma separated values for the weather parameteres temperature,rain,wind_u,wind_v,gust,pressure,cloud,humidity&wave=height,direction,period
    String inittime = "inittime_example"; // String | initial date for the forecast ISO string YYYY-MM-DDTHH:mm:SS.SZ
    String endtime = "endtime_example"; // String | end date for the forecast ISO string YYYY-MM-DDTHH:mm:SS.SZ
    Integer days = 56; // Integer | optional number of days in string. Will be added to init forecast date
    Integer hours = 56; // Integer | optional number of hours in string. Will be added to init forecast date
    String wave = "wave_example"; // String |  Comma separated values for the wave parameteres height,direction,period
    String entryid = "entryid_example"; // String | Direct file I want to extract
    try {
      apiInstance.getForecastTimeSeries(latitude, longitude, weather, inittime, endtime, days, hours, wave, entryid);
    } catch (ApiException e) {
      System.err.println("Exception when calling OdWeatherApi#getForecastTimeSeries");
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
| **latitude** | **Float**| latitude for the forecast | [default to 39.49] |
| **longitude** | **Float**| longitude for the forecast | [default to 2.74] |
| **weather** | **String**|  Comma separated values for the weather parameteres temperature,rain,wind_u,wind_v,gust,pressure,cloud,humidity&amp;wave&#x3D;height,direction,period | |
| **inittime** | **String**| initial date for the forecast ISO string YYYY-MM-DDTHH:mm:SS.SZ | [optional] |
| **endtime** | **String**| end date for the forecast ISO string YYYY-MM-DDTHH:mm:SS.SZ | [optional] |
| **days** | **Integer**| optional number of days in string. Will be added to init forecast date | [optional] |
| **hours** | **Integer**| optional number of hours in string. Will be added to init forecast date | [optional] |
| **wave** | **String**|  Comma separated values for the wave parameteres height,direction,period | [optional] |
| **entryid** | **String**| Direct file I want to extract | [optional] |

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

<a id="getForecastTimeSeriesWrf"></a>
# **getForecastTimeSeriesWrf**
> getForecastTimeSeriesWrf(latitude, longitude, weather, inittime, endtime, days, hours, wave, entryid)



Get timeseries forecast information&lt;br/&gt;None

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OdWeatherApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.oceandrivers.com");

    OdWeatherApi apiInstance = new OdWeatherApi(defaultClient);
    Float latitude = 39.49F; // Float | latitude for the forecast
    Float longitude = 2.74F; // Float | longitude for the forecast
    String weather = "weather_example"; // String |  Comma separated values for the weather parameteres temperature,rain,wind_u,wind_v,gust,pressure,cloud,humidity&wave=height,direction,period
    String inittime = "inittime_example"; // String | initial date for the forecast ISO string YYYY-MM-DDTHH:mm:SS.SZ
    String endtime = "endtime_example"; // String | end date for the forecast ISO string YYYY-MM-DDTHH:mm:SS.SZ
    Integer days = 56; // Integer | optional number of days in string. Will be added to init forecast date
    Integer hours = 56; // Integer | optional number of hours in string. Will be added to init forecast date
    String wave = "wave_example"; // String |  Comma separated values for the wave parameteres height,direction,period
    String entryid = "entryid_example"; // String | Direct file I want to extract
    try {
      apiInstance.getForecastTimeSeriesWrf(latitude, longitude, weather, inittime, endtime, days, hours, wave, entryid);
    } catch (ApiException e) {
      System.err.println("Exception when calling OdWeatherApi#getForecastTimeSeriesWrf");
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
| **latitude** | **Float**| latitude for the forecast | [default to 39.49] |
| **longitude** | **Float**| longitude for the forecast | [default to 2.74] |
| **weather** | **String**|  Comma separated values for the weather parameteres temperature,rain,wind_u,wind_v,gust,pressure,cloud,humidity&amp;wave&#x3D;height,direction,period | |
| **inittime** | **String**| initial date for the forecast ISO string YYYY-MM-DDTHH:mm:SS.SZ | [optional] |
| **endtime** | **String**| end date for the forecast ISO string YYYY-MM-DDTHH:mm:SS.SZ | [optional] |
| **days** | **Integer**| optional number of days in string. Will be added to init forecast date | [optional] |
| **hours** | **Integer**| optional number of hours in string. Will be added to init forecast date | [optional] |
| **wave** | **String**|  Comma separated values for the wave parameteres height,direction,period | [optional] |
| **entryid** | **String**| Direct file I want to extract | [optional] |

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

<a id="getSocibWeatherStation"></a>
# **getSocibWeatherStation**
> getSocibWeatherStation(stationName, period)



Get data from the socib bahia de palma buoy&lt;br/&gt;None

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OdWeatherApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.oceandrivers.com");

    OdWeatherApi apiInstance = new OdWeatherApi(defaultClient);
    String stationName = "boyaenderrocat"; // String | station name currently: boyaenderrocat | playadepalma
    String period = "lastdata"; // String | Period of time to get the data. Options: lastdata lasthour lastday
    try {
      apiInstance.getSocibWeatherStation(stationName, period);
    } catch (ApiException e) {
      System.err.println("Exception when calling OdWeatherApi#getSocibWeatherStation");
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
| **stationName** | **String**| station name currently: boyaenderrocat | playadepalma | [default to boyaenderrocat] |
| **period** | **String**| Period of time to get the data. Options: lastdata lasthour lastday | [default to lastdata] |

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

<a id="getWeatherDisplay"></a>
# **getWeatherDisplay**
> getWeatherDisplay(stationName, period)



Get data from the weather display software&lt;br/&gt;None

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OdWeatherApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.oceandrivers.com");

    OdWeatherApi apiInstance = new OdWeatherApi(defaultClient);
    String stationName = "cnarenal"; // String | currently: 'cnarenal'|'campastilla' | 'cncg'
    String period = "latestdata"; // String | Period of time to get the data latestdata|latesthour|latestday|dailylog
    try {
      apiInstance.getWeatherDisplay(stationName, period);
    } catch (ApiException e) {
      System.err.println("Exception when calling OdWeatherApi#getWeatherDisplay");
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
| **stationName** | **String**| currently: &#39;cnarenal&#39;|&#39;campastilla&#39; | &#39;cncg&#39; | [default to cnarenal] |
| **period** | **String**| Period of time to get the data latestdata|latesthour|latestday|dailylog | [default to latestdata] |

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

<a id="getWebCams"></a>
# **getWebCams**
> getWebCams()



Get forecast and realtime information for known points&lt;br/&gt;None

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OdWeatherApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.oceandrivers.com");

    OdWeatherApi apiInstance = new OdWeatherApi(defaultClient);
    try {
      apiInstance.getWebCams();
    } catch (ApiException e) {
      System.err.println("Exception when calling OdWeatherApi#getWebCams");
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

