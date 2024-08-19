# ThermostatApi

All URIs are relative to *https://api.netatmo.net/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createnewschedule**](ThermostatApi.md#createnewschedule) | **POST** /createnewschedule |  |
| [**getmeasure_0**](ThermostatApi.md#getmeasure_0) | **GET** /getmeasure |  |
| [**getthermostatsdata**](ThermostatApi.md#getthermostatsdata) | **GET** /getthermostatsdata |  |
| [**setthermpoint**](ThermostatApi.md#setthermpoint) | **POST** /setthermpoint |  |
| [**switchschedule**](ThermostatApi.md#switchschedule) | **POST** /switchschedule |  |
| [**syncschedule**](ThermostatApi.md#syncschedule) | **POST** /syncschedule |  |


<a id="createnewschedule"></a>
# **createnewschedule**
> NANewScheduleResponse createnewschedule(deviceId, moduleId, naThermProgram)



The method createnewschedule creates a new schedule stored in the backup list.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ThermostatApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netatmo.net/api");
    
    // Configure OAuth2 access token for authorization: code_oauth
    OAuth code_oauth = (OAuth) defaultClient.getAuthentication("code_oauth");
    code_oauth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: password_oauth
    OAuth password_oauth = (OAuth) defaultClient.getAuthentication("password_oauth");
    password_oauth.setAccessToken("YOUR ACCESS TOKEN");

    ThermostatApi apiInstance = new ThermostatApi(defaultClient);
    String deviceId = "deviceId_example"; // String | The relay id
    String moduleId = "moduleId_example"; // String | The thermostat id
    NAThermProgram naThermProgram = new NAThermProgram(); // NAThermProgram | The thermostat program (zones and timetable)
    try {
      NANewScheduleResponse result = apiInstance.createnewschedule(deviceId, moduleId, naThermProgram);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ThermostatApi#createnewschedule");
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
| **deviceId** | **String**| The relay id | |
| **moduleId** | **String**| The thermostat id | |
| **naThermProgram** | [**NAThermProgram**](NAThermProgram.md)| The thermostat program (zones and timetable) | |

### Return type

[**NANewScheduleResponse**](NANewScheduleResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="getmeasure_0"></a>
# **getmeasure_0**
> NAMeasureResponse getmeasure_0(deviceId, scale, type, moduleId, dateBegin, dateEnd, limit, optimize, realTime)



The method getmeasure returns the measurements of a device or a module. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ThermostatApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netatmo.net/api");
    
    // Configure OAuth2 access token for authorization: code_oauth
    OAuth code_oauth = (OAuth) defaultClient.getAuthentication("code_oauth");
    code_oauth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: password_oauth
    OAuth password_oauth = (OAuth) defaultClient.getAuthentication("password_oauth");
    password_oauth.setAccessToken("YOUR ACCESS TOKEN");

    ThermostatApi apiInstance = new ThermostatApi(defaultClient);
    String deviceId = "deviceId_example"; // String | Id of the device whose module's measurements you want to retrieve. This _id can be found in the user's devices field.
    String scale = "max"; // String | Defines the time interval between two measurements. Possible values : max -> every value stored will be returned 30min -> 1 value every 30 minutes 1hour -> 1 value every hour 3hours -> 1 value every 3 hours 1day -> 1 value per day 1week -> 1 value per week 1month -> 1 value per month 
    List<String> type = Arrays.asList(); // List<String> | Measures you are interested in. Data you can request depends on the scale. **For Weather Station:**   * max -> Temperature (°C), CO2 (ppm), Humidity (%), Pressure (mbar), Noise (db), Rain (mm), WindStrength (km/h), WindAngle (angles), Guststrength (km/h), GustAngle (angles)   * 30min, 1hour, 3hours -> Same as above + min_temp, max_temp, min_hum, max_hum, min_pressure, max_pressure, min_noise, max_noise, sum_rain, date_max_gust   * 1day, 1week, 1month -> Same as above + date_min_temp, date_max_temp, date_min_hum, date_max_hum, date_min_pressure, date_max_pressure, date_min_noise, date_max_noise, date_min_co2, date_max_co2  **For Thermostat:**   * max -> temperature (°C), sp_temperature (°C), boileron (sec), boileroff (sec)   * 30min, 1hour, 3hours -> temperature, sp_temperature, min_temp, max_temp, sum_boiler_on, sum_boiler_off   * 1day, 1week, 1month -> temperature, min_temp, date_min_temp, max_temp, sum_boiler_on, sum_boiler_off 
    String moduleId = "moduleId_example"; // String | If you don't specify any module_id you will retrieve the device's measurements. If you specify a module_id you will retrieve the module's measurements.
    Integer dateBegin = 56; // Integer | Starting timestamp (utc) of the requested measurements. Please note measurement retrieving is limited to 1024 measurements. 
    String dateEnd = "dateEnd_example"; // String | Ending timestamp (utc) of the request measurements. If you want only the last measurement, do not provide date_begin, and set date_end to `last`. 
    Integer limit = 56; // Integer | Limits the number of measurements returned (default & max is 1024)
    Boolean optimize = true; // Boolean | Allows you to choose the format of the answer. If you build a mobile app and bandwith usage is an issue, use `optimize = true`. Use `optimize = false`, for an easier parse. In this case, values are indexed by sorted timestamp. Example of un-optimized response : ```json {\"status\": \"ok\",    \"body\": {     \"1347575400\": [18.3,39],     \"1347586200\": [20.6,48]   }, \"time_exec\": 0.012136936187744} ``` If optimize is set true, measurements are returned as an array of series of regularly spaced measurements. Each series is defined by a beginning time beg_time and a step between measurements, step_time: ```json {\"status\": \"ok\",   \"body\": [     {\"beg_time\": 1347575400,      \"step_time\": 10800,      \"value\":          [[18.3,39],         [ 20.6,48]]     }], \"time_exec\": 0.014238119125366} ``` Default value is `true`. 
    Boolean realTime = true; // Boolean | In scales higher than max, since the data is aggregated, the timestamps returned are by default offset by +(scale/2). For instance, if you ask for measurements at a daily scale, you will receive data timestamped at 12:00 if real_time is set to `false` (default case), and timestamped at 00:00 if real_time is set to `true`. NB : The servers always store data with real_time set to `true` and data are offset by this parameter AFTER having being time-filtered, thus you could have data after date_end if real_time is set to `false`. 
    try {
      NAMeasureResponse result = apiInstance.getmeasure_0(deviceId, scale, type, moduleId, dateBegin, dateEnd, limit, optimize, realTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ThermostatApi#getmeasure_0");
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
| **deviceId** | **String**| Id of the device whose module&#39;s measurements you want to retrieve. This _id can be found in the user&#39;s devices field. | |
| **scale** | **String**| Defines the time interval between two measurements. Possible values : max -&gt; every value stored will be returned 30min -&gt; 1 value every 30 minutes 1hour -&gt; 1 value every hour 3hours -&gt; 1 value every 3 hours 1day -&gt; 1 value per day 1week -&gt; 1 value per week 1month -&gt; 1 value per month  | [enum: max, 30min, 1hour, 3hours, 1day, 1week, 1month] |
| **type** | [**List&lt;String&gt;**](String.md)| Measures you are interested in. Data you can request depends on the scale. **For Weather Station:**   * max -&gt; Temperature (°C), CO2 (ppm), Humidity (%), Pressure (mbar), Noise (db), Rain (mm), WindStrength (km/h), WindAngle (angles), Guststrength (km/h), GustAngle (angles)   * 30min, 1hour, 3hours -&gt; Same as above + min_temp, max_temp, min_hum, max_hum, min_pressure, max_pressure, min_noise, max_noise, sum_rain, date_max_gust   * 1day, 1week, 1month -&gt; Same as above + date_min_temp, date_max_temp, date_min_hum, date_max_hum, date_min_pressure, date_max_pressure, date_min_noise, date_max_noise, date_min_co2, date_max_co2  **For Thermostat:**   * max -&gt; temperature (°C), sp_temperature (°C), boileron (sec), boileroff (sec)   * 30min, 1hour, 3hours -&gt; temperature, sp_temperature, min_temp, max_temp, sum_boiler_on, sum_boiler_off   * 1day, 1week, 1month -&gt; temperature, min_temp, date_min_temp, max_temp, sum_boiler_on, sum_boiler_off  | [enum: Temperature, CO2, Humidity, Pressure, Noise, Rain, WindStrength, WindAngle, Guststrength, GustAngle, Sp_Temperature, BoilerOn, BoilerOff, min_temp, date_min_temp, max_temp, date_max_temp, min_hum, date_min_hum, max_hum, date_max_hum, min_pressure, date_min_pressure, max_pressure, date_max_pressure, min_noise, date_min_noise, max_noise, date_max_noise, date_min_co2, date_max_co2, date_max_gust, sum_rain, sum_boiler_on, sum_boiler_off] |
| **moduleId** | **String**| If you don&#39;t specify any module_id you will retrieve the device&#39;s measurements. If you specify a module_id you will retrieve the module&#39;s measurements. | [optional] |
| **dateBegin** | **Integer**| Starting timestamp (utc) of the requested measurements. Please note measurement retrieving is limited to 1024 measurements.  | [optional] |
| **dateEnd** | **String**| Ending timestamp (utc) of the request measurements. If you want only the last measurement, do not provide date_begin, and set date_end to &#x60;last&#x60;.  | [optional] |
| **limit** | **Integer**| Limits the number of measurements returned (default &amp; max is 1024) | [optional] |
| **optimize** | **Boolean**| Allows you to choose the format of the answer. If you build a mobile app and bandwith usage is an issue, use &#x60;optimize &#x3D; true&#x60;. Use &#x60;optimize &#x3D; false&#x60;, for an easier parse. In this case, values are indexed by sorted timestamp. Example of un-optimized response : &#x60;&#x60;&#x60;json {\&quot;status\&quot;: \&quot;ok\&quot;,    \&quot;body\&quot;: {     \&quot;1347575400\&quot;: [18.3,39],     \&quot;1347586200\&quot;: [20.6,48]   }, \&quot;time_exec\&quot;: 0.012136936187744} &#x60;&#x60;&#x60; If optimize is set true, measurements are returned as an array of series of regularly spaced measurements. Each series is defined by a beginning time beg_time and a step between measurements, step_time: &#x60;&#x60;&#x60;json {\&quot;status\&quot;: \&quot;ok\&quot;,   \&quot;body\&quot;: [     {\&quot;beg_time\&quot;: 1347575400,      \&quot;step_time\&quot;: 10800,      \&quot;value\&quot;:          [[18.3,39],         [ 20.6,48]]     }], \&quot;time_exec\&quot;: 0.014238119125366} &#x60;&#x60;&#x60; Default value is &#x60;true&#x60;.  | [optional] |
| **realTime** | **Boolean**| In scales higher than max, since the data is aggregated, the timestamps returned are by default offset by +(scale/2). For instance, if you ask for measurements at a daily scale, you will receive data timestamped at 12:00 if real_time is set to &#x60;false&#x60; (default case), and timestamped at 00:00 if real_time is set to &#x60;true&#x60;. NB : The servers always store data with real_time set to &#x60;true&#x60; and data are offset by this parameter AFTER having being time-filtered, thus you could have data after date_end if real_time is set to &#x60;false&#x60;.  | [optional] |

### Return type

[**NAMeasureResponse**](NAMeasureResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="getthermostatsdata"></a>
# **getthermostatsdata**
> NAThermostatDataResponse getthermostatsdata(deviceId)



The method getthermostatsdata returns information about user&#39;s thermostats such as their last measurements.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ThermostatApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netatmo.net/api");
    
    // Configure OAuth2 access token for authorization: code_oauth
    OAuth code_oauth = (OAuth) defaultClient.getAuthentication("code_oauth");
    code_oauth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: password_oauth
    OAuth password_oauth = (OAuth) defaultClient.getAuthentication("password_oauth");
    password_oauth.setAccessToken("YOUR ACCESS TOKEN");

    ThermostatApi apiInstance = new ThermostatApi(defaultClient);
    String deviceId = "deviceId_example"; // String | Id of the device you want to retrieve information of
    try {
      NAThermostatDataResponse result = apiInstance.getthermostatsdata(deviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ThermostatApi#getthermostatsdata");
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
| **deviceId** | **String**| Id of the device you want to retrieve information of | [optional] |

### Return type

[**NAThermostatDataResponse**](NAThermostatDataResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="setthermpoint"></a>
# **setthermpoint**
> NAOkResponse setthermpoint(deviceId, moduleId, setpointMode, setpointEndtime, setpointTemp)



The method setthermpoint changes the Thermostat manual temperature setpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ThermostatApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netatmo.net/api");
    
    // Configure OAuth2 access token for authorization: code_oauth
    OAuth code_oauth = (OAuth) defaultClient.getAuthentication("code_oauth");
    code_oauth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: password_oauth
    OAuth password_oauth = (OAuth) defaultClient.getAuthentication("password_oauth");
    password_oauth.setAccessToken("YOUR ACCESS TOKEN");

    ThermostatApi apiInstance = new ThermostatApi(defaultClient);
    String deviceId = "deviceId_example"; // String | The relay id
    String moduleId = "moduleId_example"; // String | The thermostat id
    String setpointMode = "program"; // String | Chosen setpoint_mode
    Integer setpointEndtime = 56; // Integer | When using the manual or max setpoint_mode, this parameter defines when the setpoint expires.
    Float setpointTemp = 3.4F; // Float | When using the manual setpoint_mode, this parameter defines the temperature setpoint (in Celcius) to use.
    try {
      NAOkResponse result = apiInstance.setthermpoint(deviceId, moduleId, setpointMode, setpointEndtime, setpointTemp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ThermostatApi#setthermpoint");
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
| **deviceId** | **String**| The relay id | |
| **moduleId** | **String**| The thermostat id | |
| **setpointMode** | **String**| Chosen setpoint_mode | [enum: program, away, hg, manual, false, max] |
| **setpointEndtime** | **Integer**| When using the manual or max setpoint_mode, this parameter defines when the setpoint expires. | [optional] |
| **setpointTemp** | **Float**| When using the manual setpoint_mode, this parameter defines the temperature setpoint (in Celcius) to use. | [optional] |

### Return type

[**NAOkResponse**](NAOkResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="switchschedule"></a>
# **switchschedule**
> NAOkResponse switchschedule(deviceId, moduleId, scheduleId)



The method switchschedule switches the Thermostat&#39;s schedule to another existing schedule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ThermostatApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netatmo.net/api");
    
    // Configure OAuth2 access token for authorization: code_oauth
    OAuth code_oauth = (OAuth) defaultClient.getAuthentication("code_oauth");
    code_oauth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: password_oauth
    OAuth password_oauth = (OAuth) defaultClient.getAuthentication("password_oauth");
    password_oauth.setAccessToken("YOUR ACCESS TOKEN");

    ThermostatApi apiInstance = new ThermostatApi(defaultClient);
    String deviceId = "deviceId_example"; // String | The relay id
    String moduleId = "moduleId_example"; // String | The thermostat id
    String scheduleId = "scheduleId_example"; // String | The schedule id. It can be found in the getthermstate response, under the keys `therm_program_backup` and `therm_program`. 
    try {
      NAOkResponse result = apiInstance.switchschedule(deviceId, moduleId, scheduleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ThermostatApi#switchschedule");
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
| **deviceId** | **String**| The relay id | |
| **moduleId** | **String**| The thermostat id | |
| **scheduleId** | **String**| The schedule id. It can be found in the getthermstate response, under the keys &#x60;therm_program_backup&#x60; and &#x60;therm_program&#x60;.  | |

### Return type

[**NAOkResponse**](NAOkResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="syncschedule"></a>
# **syncschedule**
> NAOkResponse syncschedule(deviceId, moduleId, naThermProgram)



The method syncschedule changes the Thermostat weekly schedule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ThermostatApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netatmo.net/api");
    
    // Configure OAuth2 access token for authorization: code_oauth
    OAuth code_oauth = (OAuth) defaultClient.getAuthentication("code_oauth");
    code_oauth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: password_oauth
    OAuth password_oauth = (OAuth) defaultClient.getAuthentication("password_oauth");
    password_oauth.setAccessToken("YOUR ACCESS TOKEN");

    ThermostatApi apiInstance = new ThermostatApi(defaultClient);
    String deviceId = "deviceId_example"; // String | The relay id
    String moduleId = "moduleId_example"; // String | The thermostat id
    NAThermProgram naThermProgram = new NAThermProgram(); // NAThermProgram | The thermostat program (zones, timetable and name)
    try {
      NAOkResponse result = apiInstance.syncschedule(deviceId, moduleId, naThermProgram);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ThermostatApi#syncschedule");
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
| **deviceId** | **String**| The relay id | |
| **moduleId** | **String**| The thermostat id | |
| **naThermProgram** | [**NAThermProgram**](NAThermProgram.md)| The thermostat program (zones, timetable and name) | |

### Return type

[**NAOkResponse**](NAOkResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

