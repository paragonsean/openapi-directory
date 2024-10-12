# OdWeather.ODWeatherApi

All URIs are relative to *https://api.oceandrivers.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compareStation**](ODWeatherApi.md#compareStation) | **GET** /v1.0/compareStation/{stationName}/ | 
[**getAemetStation**](ODWeatherApi.md#getAemetStation) | **GET** /v1.0/getAemetStation/{stationName}/{period}/ | 
[**getEasywind**](ODWeatherApi.md#getEasywind) | **GET** /v1.0/getEasyWind/{easywindId}/ | 
[**getEventStations**](ODWeatherApi.md#getEventStations) | **GET** /v1.0/getEventStations/{eventId}/ | 
[**getForecastPoints**](ODWeatherApi.md#getForecastPoints) | **GET** /v1.0/getForecastPoints/{yatchclubid}/language/{language} | 
[**getForecastTimeSeries**](ODWeatherApi.md#getForecastTimeSeries) | **GET** /v1.0/getForecastTimeSeries/{latitude}/{longitude}/ | 
[**getForecastTimeSeriesWrf**](ODWeatherApi.md#getForecastTimeSeriesWrf) | **GET** /v1.0/getForecastTimeSeriesWrf/{latitude}/{longitude}/ | 
[**getSocibWeatherStation**](ODWeatherApi.md#getSocibWeatherStation) | **GET** /v1.0/getSocibWeatherStation/{stationName}/{period}/ | 
[**getWeatherDisplay**](ODWeatherApi.md#getWeatherDisplay) | **GET** /v1.0/getWeatherDisplay/{stationName}/ | 
[**getWebCams**](ODWeatherApi.md#getWebCams) | **GET** /v1.0/getWebCams/ | 



## compareStation

> compareStation(stationName)



Get forecast and realtime information for known points&lt;br/&gt;None

### Example

```javascript
import OdWeather from 'od_weather';

let apiInstance = new OdWeather.ODWeatherApi();
let stationName = "'cnarenal'"; // String | Weather station to compare, values: cnareanl|rcnp | cmsap|boyaenderrocat|areopuertopalma | EWXXX
apiInstance.compareStation(stationName, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stationName** | **String**| Weather station to compare, values: cnareanl|rcnp | cmsap|boyaenderrocat|areopuertopalma | EWXXX | [default to &#39;cnarenal&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAemetStation

> getAemetStation(stationName, period)



Get data from the aemet stations&lt;br/&gt;None

### Example

```javascript
import OdWeather from 'od_weather';

let apiInstance = new OdWeather.ODWeatherApi();
let stationName = "'aeropuertopalma'"; // String | station name currently: aeropuertopalma | caboblanco 
let period = "'lastdata'"; // String | Period of time to get the data. Options: lastdata lastday
apiInstance.getAemetStation(stationName, period, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stationName** | **String**| station name currently: aeropuertopalma | caboblanco  | [default to &#39;aeropuertopalma&#39;]
 **period** | **String**| Period of time to get the data. Options: lastdata lastday | [default to &#39;lastdata&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getEasywind

> getEasywind(easywindId, period)



Get data from the easywind weather stations&lt;br/&gt;None

### Example

```javascript
import OdWeather from 'od_weather';

let apiInstance = new OdWeather.ODWeatherApi();
let easywindId = "'EW013'"; // String | currently: 'EW013'|'EW008'
let period = "'latestdata'"; // String | Period of time to get the data latestdata|latesthour|latestday
apiInstance.getEasywind(easywindId, period, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **easywindId** | **String**| currently: &#39;EW013&#39;|&#39;EW008&#39; | [default to &#39;EW013&#39;]
 **period** | **String**| Period of time to get the data latestdata|latesthour|latestday | [default to &#39;latestdata&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getEventStations

> getEventStations(eventId)



Get stations in an event&lt;br/&gt;None

### Example

```javascript
import OdWeather from 'od_weather';

let apiInstance = new OdWeather.ODWeatherApi();
let eventId = "'trofeoprincesasofia'"; // String | currently: 'trofeoprincesasofia|palmavela'
apiInstance.getEventStations(eventId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eventId** | **String**| currently: &#39;trofeoprincesasofia|palmavela&#39; | [default to &#39;trofeoprincesasofia&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getForecastPoints

> getForecastPoints(yatchclubid, language)



Get forecast points of a yatchclub&lt;br/&gt;None

### Example

```javascript
import OdWeather from 'od_weather';

let apiInstance = new OdWeather.ODWeatherApi();
let yatchclubid = "'cnarenal'"; // String | base URL for the the
let language = "language_example"; // String | 
apiInstance.getForecastPoints(yatchclubid, language, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **yatchclubid** | **String**| base URL for the the | [default to &#39;cnarenal&#39;]
 **language** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getForecastTimeSeries

> getForecastTimeSeries(latitude, longitude, weather, opts)



Get timeseries forecast information&lt;br/&gt;None

### Example

```javascript
import OdWeather from 'od_weather';

let apiInstance = new OdWeather.ODWeatherApi();
let latitude = 39.49; // Number | latitude for the forecast
let longitude = 2.74; // Number | longitude for the forecast
let weather = "weather_example"; // String |  Comma separated values for the weather parameteres temperature,rain,wind_u,wind_v,gust,pressure,cloud,humidity&wave=height,direction,period
let opts = {
  'inittime': "inittime_example", // String | initial date for the forecast ISO string YYYY-MM-DDTHH:mm:SS.SZ
  'endtime': "endtime_example", // String | end date for the forecast ISO string YYYY-MM-DDTHH:mm:SS.SZ
  'days': 56, // Number | optional number of days in string. Will be added to init forecast date
  'hours': 56, // Number | optional number of hours in string. Will be added to init forecast date
  'wave': "wave_example", // String |  Comma separated values for the wave parameteres height,direction,period
  'entryid': "entryid_example" // String | Direct file I want to extract
};
apiInstance.getForecastTimeSeries(latitude, longitude, weather, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **latitude** | **Number**| latitude for the forecast | [default to 39.49]
 **longitude** | **Number**| longitude for the forecast | [default to 2.74]
 **weather** | **String**|  Comma separated values for the weather parameteres temperature,rain,wind_u,wind_v,gust,pressure,cloud,humidity&amp;wave&#x3D;height,direction,period | 
 **inittime** | **String**| initial date for the forecast ISO string YYYY-MM-DDTHH:mm:SS.SZ | [optional] 
 **endtime** | **String**| end date for the forecast ISO string YYYY-MM-DDTHH:mm:SS.SZ | [optional] 
 **days** | **Number**| optional number of days in string. Will be added to init forecast date | [optional] 
 **hours** | **Number**| optional number of hours in string. Will be added to init forecast date | [optional] 
 **wave** | **String**|  Comma separated values for the wave parameteres height,direction,period | [optional] 
 **entryid** | **String**| Direct file I want to extract | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getForecastTimeSeriesWrf

> getForecastTimeSeriesWrf(latitude, longitude, weather, opts)



Get timeseries forecast information&lt;br/&gt;None

### Example

```javascript
import OdWeather from 'od_weather';

let apiInstance = new OdWeather.ODWeatherApi();
let latitude = 39.49; // Number | latitude for the forecast
let longitude = 2.74; // Number | longitude for the forecast
let weather = "weather_example"; // String |  Comma separated values for the weather parameteres temperature,rain,wind_u,wind_v,gust,pressure,cloud,humidity&wave=height,direction,period
let opts = {
  'inittime': "inittime_example", // String | initial date for the forecast ISO string YYYY-MM-DDTHH:mm:SS.SZ
  'endtime': "endtime_example", // String | end date for the forecast ISO string YYYY-MM-DDTHH:mm:SS.SZ
  'days': 56, // Number | optional number of days in string. Will be added to init forecast date
  'hours': 56, // Number | optional number of hours in string. Will be added to init forecast date
  'wave': "wave_example", // String |  Comma separated values for the wave parameteres height,direction,period
  'entryid': "entryid_example" // String | Direct file I want to extract
};
apiInstance.getForecastTimeSeriesWrf(latitude, longitude, weather, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **latitude** | **Number**| latitude for the forecast | [default to 39.49]
 **longitude** | **Number**| longitude for the forecast | [default to 2.74]
 **weather** | **String**|  Comma separated values for the weather parameteres temperature,rain,wind_u,wind_v,gust,pressure,cloud,humidity&amp;wave&#x3D;height,direction,period | 
 **inittime** | **String**| initial date for the forecast ISO string YYYY-MM-DDTHH:mm:SS.SZ | [optional] 
 **endtime** | **String**| end date for the forecast ISO string YYYY-MM-DDTHH:mm:SS.SZ | [optional] 
 **days** | **Number**| optional number of days in string. Will be added to init forecast date | [optional] 
 **hours** | **Number**| optional number of hours in string. Will be added to init forecast date | [optional] 
 **wave** | **String**|  Comma separated values for the wave parameteres height,direction,period | [optional] 
 **entryid** | **String**| Direct file I want to extract | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSocibWeatherStation

> getSocibWeatherStation(stationName, period)



Get data from the socib bahia de palma buoy&lt;br/&gt;None

### Example

```javascript
import OdWeather from 'od_weather';

let apiInstance = new OdWeather.ODWeatherApi();
let stationName = "'boyaenderrocat'"; // String | station name currently: boyaenderrocat | playadepalma
let period = "'lastdata'"; // String | Period of time to get the data. Options: lastdata lasthour lastday
apiInstance.getSocibWeatherStation(stationName, period, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stationName** | **String**| station name currently: boyaenderrocat | playadepalma | [default to &#39;boyaenderrocat&#39;]
 **period** | **String**| Period of time to get the data. Options: lastdata lasthour lastday | [default to &#39;lastdata&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getWeatherDisplay

> getWeatherDisplay(stationName, period)



Get data from the weather display software&lt;br/&gt;None

### Example

```javascript
import OdWeather from 'od_weather';

let apiInstance = new OdWeather.ODWeatherApi();
let stationName = "'cnarenal'"; // String | currently: 'cnarenal'|'campastilla' | 'cncg'
let period = "'latestdata'"; // String | Period of time to get the data latestdata|latesthour|latestday|dailylog
apiInstance.getWeatherDisplay(stationName, period, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stationName** | **String**| currently: &#39;cnarenal&#39;|&#39;campastilla&#39; | &#39;cncg&#39; | [default to &#39;cnarenal&#39;]
 **period** | **String**| Period of time to get the data latestdata|latesthour|latestday|dailylog | [default to &#39;latestdata&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getWebCams

> getWebCams()



Get forecast and realtime information for known points&lt;br/&gt;None

### Example

```javascript
import OdWeather from 'od_weather';

let apiInstance = new OdWeather.ODWeatherApi();
apiInstance.getWebCams((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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

