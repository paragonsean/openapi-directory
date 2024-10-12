# Netatmo.ThermostatApi

All URIs are relative to *https://api.netatmo.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createnewschedule**](ThermostatApi.md#createnewschedule) | **POST** /createnewschedule | 
[**getmeasure_0**](ThermostatApi.md#getmeasure_0) | **GET** /getmeasure | 
[**getthermostatsdata**](ThermostatApi.md#getthermostatsdata) | **GET** /getthermostatsdata | 
[**setthermpoint**](ThermostatApi.md#setthermpoint) | **POST** /setthermpoint | 
[**switchschedule**](ThermostatApi.md#switchschedule) | **POST** /switchschedule | 
[**syncschedule**](ThermostatApi.md#syncschedule) | **POST** /syncschedule | 



## createnewschedule

> NANewScheduleResponse createnewschedule(deviceId, moduleId, nAThermProgram)



The method createnewschedule creates a new schedule stored in the backup list.

### Example

```javascript
import Netatmo from 'netatmo';
let defaultClient = Netatmo.ApiClient.instance;
// Configure OAuth2 access token for authorization: code_oauth
let code_oauth = defaultClient.authentications['code_oauth'];
code_oauth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: password_oauth
let password_oauth = defaultClient.authentications['password_oauth'];
password_oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Netatmo.ThermostatApi();
let deviceId = "deviceId_example"; // String | The relay id
let moduleId = "moduleId_example"; // String | The thermostat id
let nAThermProgram = new Netatmo.NAThermProgram(); // NAThermProgram | The thermostat program (zones and timetable)
apiInstance.createnewschedule(deviceId, moduleId, nAThermProgram, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceId** | **String**| The relay id | 
 **moduleId** | **String**| The thermostat id | 
 **nAThermProgram** | [**NAThermProgram**](NAThermProgram.md)| The thermostat program (zones and timetable) | 

### Return type

[**NANewScheduleResponse**](NANewScheduleResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: application/json


## getmeasure_0

> NAMeasureResponse getmeasure_0(deviceId, scale, type, opts)



The method getmeasure returns the measurements of a device or a module. 

### Example

```javascript
import Netatmo from 'netatmo';
let defaultClient = Netatmo.ApiClient.instance;
// Configure OAuth2 access token for authorization: code_oauth
let code_oauth = defaultClient.authentications['code_oauth'];
code_oauth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: password_oauth
let password_oauth = defaultClient.authentications['password_oauth'];
password_oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Netatmo.ThermostatApi();
let deviceId = "deviceId_example"; // String | Id of the device whose module's measurements you want to retrieve. This _id can be found in the user's devices field.
let scale = "scale_example"; // String | Defines the time interval between two measurements. Possible values : max -> every value stored will be returned 30min -> 1 value every 30 minutes 1hour -> 1 value every hour 3hours -> 1 value every 3 hours 1day -> 1 value per day 1week -> 1 value per week 1month -> 1 value per month 
let type = ["null"]; // [String] | Measures you are interested in. Data you can request depends on the scale. **For Weather Station:**   * max -> Temperature (°C), CO2 (ppm), Humidity (%), Pressure (mbar), Noise (db), Rain (mm), WindStrength (km/h), WindAngle (angles), Guststrength (km/h), GustAngle (angles)   * 30min, 1hour, 3hours -> Same as above + min_temp, max_temp, min_hum, max_hum, min_pressure, max_pressure, min_noise, max_noise, sum_rain, date_max_gust   * 1day, 1week, 1month -> Same as above + date_min_temp, date_max_temp, date_min_hum, date_max_hum, date_min_pressure, date_max_pressure, date_min_noise, date_max_noise, date_min_co2, date_max_co2  **For Thermostat:**   * max -> temperature (°C), sp_temperature (°C), boileron (sec), boileroff (sec)   * 30min, 1hour, 3hours -> temperature, sp_temperature, min_temp, max_temp, sum_boiler_on, sum_boiler_off   * 1day, 1week, 1month -> temperature, min_temp, date_min_temp, max_temp, sum_boiler_on, sum_boiler_off 
let opts = {
  'moduleId': "moduleId_example", // String | If you don't specify any module_id you will retrieve the device's measurements. If you specify a module_id you will retrieve the module's measurements.
  'dateBegin': 56, // Number | Starting timestamp (utc) of the requested measurements. Please note measurement retrieving is limited to 1024 measurements. 
  'dateEnd': "dateEnd_example", // String | Ending timestamp (utc) of the request measurements. If you want only the last measurement, do not provide date_begin, and set date_end to `last`. 
  'limit': 56, // Number | Limits the number of measurements returned (default & max is 1024)
  'optimize': true, // Boolean | Allows you to choose the format of the answer. If you build a mobile app and bandwith usage is an issue, use `optimize = true`. Use `optimize = false`, for an easier parse. In this case, values are indexed by sorted timestamp. Example of un-optimized response : ```json {\"status\": \"ok\",    \"body\": {     \"1347575400\": [18.3,39],     \"1347586200\": [20.6,48]   }, \"time_exec\": 0.012136936187744} ``` If optimize is set true, measurements are returned as an array of series of regularly spaced measurements. Each series is defined by a beginning time beg_time and a step between measurements, step_time: ```json {\"status\": \"ok\",   \"body\": [     {\"beg_time\": 1347575400,      \"step_time\": 10800,      \"value\":          [[18.3,39],         [ 20.6,48]]     }], \"time_exec\": 0.014238119125366} ``` Default value is `true`. 
  'realTime': true // Boolean | In scales higher than max, since the data is aggregated, the timestamps returned are by default offset by +(scale/2). For instance, if you ask for measurements at a daily scale, you will receive data timestamped at 12:00 if real_time is set to `false` (default case), and timestamped at 00:00 if real_time is set to `true`. NB : The servers always store data with real_time set to `true` and data are offset by this parameter AFTER having being time-filtered, thus you could have data after date_end if real_time is set to `false`. 
};
apiInstance.getmeasure_0(deviceId, scale, type, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceId** | **String**| Id of the device whose module&#39;s measurements you want to retrieve. This _id can be found in the user&#39;s devices field. | 
 **scale** | **String**| Defines the time interval between two measurements. Possible values : max -&gt; every value stored will be returned 30min -&gt; 1 value every 30 minutes 1hour -&gt; 1 value every hour 3hours -&gt; 1 value every 3 hours 1day -&gt; 1 value per day 1week -&gt; 1 value per week 1month -&gt; 1 value per month  | 
 **type** | [**[String]**](String.md)| Measures you are interested in. Data you can request depends on the scale. **For Weather Station:**   * max -&gt; Temperature (°C), CO2 (ppm), Humidity (%), Pressure (mbar), Noise (db), Rain (mm), WindStrength (km/h), WindAngle (angles), Guststrength (km/h), GustAngle (angles)   * 30min, 1hour, 3hours -&gt; Same as above + min_temp, max_temp, min_hum, max_hum, min_pressure, max_pressure, min_noise, max_noise, sum_rain, date_max_gust   * 1day, 1week, 1month -&gt; Same as above + date_min_temp, date_max_temp, date_min_hum, date_max_hum, date_min_pressure, date_max_pressure, date_min_noise, date_max_noise, date_min_co2, date_max_co2  **For Thermostat:**   * max -&gt; temperature (°C), sp_temperature (°C), boileron (sec), boileroff (sec)   * 30min, 1hour, 3hours -&gt; temperature, sp_temperature, min_temp, max_temp, sum_boiler_on, sum_boiler_off   * 1day, 1week, 1month -&gt; temperature, min_temp, date_min_temp, max_temp, sum_boiler_on, sum_boiler_off  | 
 **moduleId** | **String**| If you don&#39;t specify any module_id you will retrieve the device&#39;s measurements. If you specify a module_id you will retrieve the module&#39;s measurements. | [optional] 
 **dateBegin** | **Number**| Starting timestamp (utc) of the requested measurements. Please note measurement retrieving is limited to 1024 measurements.  | [optional] 
 **dateEnd** | **String**| Ending timestamp (utc) of the request measurements. If you want only the last measurement, do not provide date_begin, and set date_end to &#x60;last&#x60;.  | [optional] 
 **limit** | **Number**| Limits the number of measurements returned (default &amp; max is 1024) | [optional] 
 **optimize** | **Boolean**| Allows you to choose the format of the answer. If you build a mobile app and bandwith usage is an issue, use &#x60;optimize &#x3D; true&#x60;. Use &#x60;optimize &#x3D; false&#x60;, for an easier parse. In this case, values are indexed by sorted timestamp. Example of un-optimized response : &#x60;&#x60;&#x60;json {\&quot;status\&quot;: \&quot;ok\&quot;,    \&quot;body\&quot;: {     \&quot;1347575400\&quot;: [18.3,39],     \&quot;1347586200\&quot;: [20.6,48]   }, \&quot;time_exec\&quot;: 0.012136936187744} &#x60;&#x60;&#x60; If optimize is set true, measurements are returned as an array of series of regularly spaced measurements. Each series is defined by a beginning time beg_time and a step between measurements, step_time: &#x60;&#x60;&#x60;json {\&quot;status\&quot;: \&quot;ok\&quot;,   \&quot;body\&quot;: [     {\&quot;beg_time\&quot;: 1347575400,      \&quot;step_time\&quot;: 10800,      \&quot;value\&quot;:          [[18.3,39],         [ 20.6,48]]     }], \&quot;time_exec\&quot;: 0.014238119125366} &#x60;&#x60;&#x60; Default value is &#x60;true&#x60;.  | [optional] 
 **realTime** | **Boolean**| In scales higher than max, since the data is aggregated, the timestamps returned are by default offset by +(scale/2). For instance, if you ask for measurements at a daily scale, you will receive data timestamped at 12:00 if real_time is set to &#x60;false&#x60; (default case), and timestamped at 00:00 if real_time is set to &#x60;true&#x60;. NB : The servers always store data with real_time set to &#x60;true&#x60; and data are offset by this parameter AFTER having being time-filtered, thus you could have data after date_end if real_time is set to &#x60;false&#x60;.  | [optional] 

### Return type

[**NAMeasureResponse**](NAMeasureResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getthermostatsdata

> NAThermostatDataResponse getthermostatsdata(opts)



The method getthermostatsdata returns information about user&#39;s thermostats such as their last measurements.

### Example

```javascript
import Netatmo from 'netatmo';
let defaultClient = Netatmo.ApiClient.instance;
// Configure OAuth2 access token for authorization: code_oauth
let code_oauth = defaultClient.authentications['code_oauth'];
code_oauth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: password_oauth
let password_oauth = defaultClient.authentications['password_oauth'];
password_oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Netatmo.ThermostatApi();
let opts = {
  'deviceId': "deviceId_example" // String | Id of the device you want to retrieve information of
};
apiInstance.getthermostatsdata(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceId** | **String**| Id of the device you want to retrieve information of | [optional] 

### Return type

[**NAThermostatDataResponse**](NAThermostatDataResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setthermpoint

> NAOkResponse setthermpoint(deviceId, moduleId, setpointMode, opts)



The method setthermpoint changes the Thermostat manual temperature setpoint.

### Example

```javascript
import Netatmo from 'netatmo';
let defaultClient = Netatmo.ApiClient.instance;
// Configure OAuth2 access token for authorization: code_oauth
let code_oauth = defaultClient.authentications['code_oauth'];
code_oauth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: password_oauth
let password_oauth = defaultClient.authentications['password_oauth'];
password_oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Netatmo.ThermostatApi();
let deviceId = "deviceId_example"; // String | The relay id
let moduleId = "moduleId_example"; // String | The thermostat id
let setpointMode = "setpointMode_example"; // String | Chosen setpoint_mode
let opts = {
  'setpointEndtime': 56, // Number | When using the manual or max setpoint_mode, this parameter defines when the setpoint expires.
  'setpointTemp': 3.4 // Number | When using the manual setpoint_mode, this parameter defines the temperature setpoint (in Celcius) to use.
};
apiInstance.setthermpoint(deviceId, moduleId, setpointMode, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceId** | **String**| The relay id | 
 **moduleId** | **String**| The thermostat id | 
 **setpointMode** | **String**| Chosen setpoint_mode | 
 **setpointEndtime** | **Number**| When using the manual or max setpoint_mode, this parameter defines when the setpoint expires. | [optional] 
 **setpointTemp** | **Number**| When using the manual setpoint_mode, this parameter defines the temperature setpoint (in Celcius) to use. | [optional] 

### Return type

[**NAOkResponse**](NAOkResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## switchschedule

> NAOkResponse switchschedule(deviceId, moduleId, scheduleId)



The method switchschedule switches the Thermostat&#39;s schedule to another existing schedule.

### Example

```javascript
import Netatmo from 'netatmo';
let defaultClient = Netatmo.ApiClient.instance;
// Configure OAuth2 access token for authorization: code_oauth
let code_oauth = defaultClient.authentications['code_oauth'];
code_oauth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: password_oauth
let password_oauth = defaultClient.authentications['password_oauth'];
password_oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Netatmo.ThermostatApi();
let deviceId = "deviceId_example"; // String | The relay id
let moduleId = "moduleId_example"; // String | The thermostat id
let scheduleId = "scheduleId_example"; // String | The schedule id. It can be found in the getthermstate response, under the keys `therm_program_backup` and `therm_program`. 
apiInstance.switchschedule(deviceId, moduleId, scheduleId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceId** | **String**| The relay id | 
 **moduleId** | **String**| The thermostat id | 
 **scheduleId** | **String**| The schedule id. It can be found in the getthermstate response, under the keys &#x60;therm_program_backup&#x60; and &#x60;therm_program&#x60;.  | 

### Return type

[**NAOkResponse**](NAOkResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## syncschedule

> NAOkResponse syncschedule(deviceId, moduleId, nAThermProgram)



The method syncschedule changes the Thermostat weekly schedule.

### Example

```javascript
import Netatmo from 'netatmo';
let defaultClient = Netatmo.ApiClient.instance;
// Configure OAuth2 access token for authorization: code_oauth
let code_oauth = defaultClient.authentications['code_oauth'];
code_oauth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: password_oauth
let password_oauth = defaultClient.authentications['password_oauth'];
password_oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Netatmo.ThermostatApi();
let deviceId = "deviceId_example"; // String | The relay id
let moduleId = "moduleId_example"; // String | The thermostat id
let nAThermProgram = new Netatmo.NAThermProgram(); // NAThermProgram | The thermostat program (zones, timetable and name)
apiInstance.syncschedule(deviceId, moduleId, nAThermProgram, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deviceId** | **String**| The relay id | 
 **moduleId** | **String**| The thermostat id | 
 **nAThermProgram** | [**NAThermProgram**](NAThermProgram.md)| The thermostat program (zones, timetable and name) | 

### Return type

[**NAOkResponse**](NAOkResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: application/json

