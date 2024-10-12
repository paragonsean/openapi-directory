# MerakiDashboardApi.SensorApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkSensorAlertsProfile**](SensorApi.md#createNetworkSensorAlertsProfile) | **POST** /networks/{networkId}/sensor/alerts/profiles | Creates a sensor alert profile for a network.
[**deleteNetworkSensorAlertsProfile**](SensorApi.md#deleteNetworkSensorAlertsProfile) | **DELETE** /networks/{networkId}/sensor/alerts/profiles/{id} | Deletes a sensor alert profile from a network.
[**getDeviceSensorRelationships**](SensorApi.md#getDeviceSensorRelationships) | **GET** /devices/{serial}/sensor/relationships | List the sensor roles for a given sensor or camera device.
[**getNetworkSensorAlertsCurrentOverviewByMetric**](SensorApi.md#getNetworkSensorAlertsCurrentOverviewByMetric) | **GET** /networks/{networkId}/sensor/alerts/current/overview/byMetric | Return an overview of currently alerting sensors by metric
[**getNetworkSensorAlertsOverviewByMetric**](SensorApi.md#getNetworkSensorAlertsOverviewByMetric) | **GET** /networks/{networkId}/sensor/alerts/overview/byMetric | Return an overview of alert occurrences over a timespan, by metric
[**getNetworkSensorAlertsProfile**](SensorApi.md#getNetworkSensorAlertsProfile) | **GET** /networks/{networkId}/sensor/alerts/profiles/{id} | Show details of a sensor alert profile for a network.
[**getNetworkSensorAlertsProfiles**](SensorApi.md#getNetworkSensorAlertsProfiles) | **GET** /networks/{networkId}/sensor/alerts/profiles | Lists all sensor alert profiles for a network.
[**getNetworkSensorRelationships**](SensorApi.md#getNetworkSensorRelationships) | **GET** /networks/{networkId}/sensor/relationships | List the sensor roles for devices in a given network
[**getOrganizationSensorReadingsHistory**](SensorApi.md#getOrganizationSensorReadingsHistory) | **GET** /organizations/{organizationId}/sensor/readings/history | Return all reported readings from sensors in a given timespan, sorted by timestamp
[**getOrganizationSensorReadingsLatest**](SensorApi.md#getOrganizationSensorReadingsLatest) | **GET** /organizations/{organizationId}/sensor/readings/latest | Return the latest available reading for each metric from each sensor, sorted by sensor serial
[**updateDeviceSensorRelationships**](SensorApi.md#updateDeviceSensorRelationships) | **PUT** /devices/{serial}/sensor/relationships | Assign one or more sensor roles to a given sensor or camera device.
[**updateNetworkSensorAlertsProfile**](SensorApi.md#updateNetworkSensorAlertsProfile) | **PUT** /networks/{networkId}/sensor/alerts/profiles/{id} | Updates a sensor alert profile for a network.



## createNetworkSensorAlertsProfile

> GetNetworkSensorAlertsProfiles200ResponseInner createNetworkSensorAlertsProfile(networkId, createNetworkSensorAlertsProfileRequest)

Creates a sensor alert profile for a network.

Creates a sensor alert profile for a network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SensorApi();
let networkId = "networkId_example"; // String | 
let createNetworkSensorAlertsProfileRequest = new MerakiDashboardApi.CreateNetworkSensorAlertsProfileRequest(); // CreateNetworkSensorAlertsProfileRequest | 
apiInstance.createNetworkSensorAlertsProfile(networkId, createNetworkSensorAlertsProfileRequest, (error, data, response) => {
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
 **networkId** | **String**|  | 
 **createNetworkSensorAlertsProfileRequest** | [**CreateNetworkSensorAlertsProfileRequest**](CreateNetworkSensorAlertsProfileRequest.md)|  | 

### Return type

[**GetNetworkSensorAlertsProfiles200ResponseInner**](GetNetworkSensorAlertsProfiles200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteNetworkSensorAlertsProfile

> deleteNetworkSensorAlertsProfile(networkId, id)

Deletes a sensor alert profile from a network.

Deletes a sensor alert profile from a network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SensorApi();
let networkId = "networkId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.deleteNetworkSensorAlertsProfile(networkId, id, (error, data, response) => {
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
 **networkId** | **String**|  | 
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDeviceSensorRelationships

> [GetDeviceSensorRelationships200ResponseInner] getDeviceSensorRelationships(serial)

List the sensor roles for a given sensor or camera device.

List the sensor roles for a given sensor or camera device.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SensorApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceSensorRelationships(serial, (error, data, response) => {
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
 **serial** | **String**|  | 

### Return type

[**[GetDeviceSensorRelationships200ResponseInner]**](GetDeviceSensorRelationships200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSensorAlertsCurrentOverviewByMetric

> GetNetworkSensorAlertsCurrentOverviewByMetric200Response getNetworkSensorAlertsCurrentOverviewByMetric(networkId)

Return an overview of currently alerting sensors by metric

Return an overview of currently alerting sensors by metric

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SensorApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSensorAlertsCurrentOverviewByMetric(networkId, (error, data, response) => {
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
 **networkId** | **String**|  | 

### Return type

[**GetNetworkSensorAlertsCurrentOverviewByMetric200Response**](GetNetworkSensorAlertsCurrentOverviewByMetric200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSensorAlertsOverviewByMetric

> [GetNetworkSensorAlertsOverviewByMetric200ResponseInner] getNetworkSensorAlertsOverviewByMetric(networkId, opts)

Return an overview of alert occurrences over a timespan, by metric

Return an overview of alert occurrences over a timespan, by metric

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SensorApi();
let networkId = "networkId_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
  'interval': 56 // Number | The time interval in seconds for returned data. The valid intervals are: 86400, 604800. The default is 604800.
};
apiInstance.getNetworkSensorAlertsOverviewByMetric(networkId, opts, (error, data, response) => {
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
 **networkId** | **String**|  | 
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 365 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days. | [optional] 
 **interval** | **Number**| The time interval in seconds for returned data. The valid intervals are: 86400, 604800. The default is 604800. | [optional] 

### Return type

[**[GetNetworkSensorAlertsOverviewByMetric200ResponseInner]**](GetNetworkSensorAlertsOverviewByMetric200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSensorAlertsProfile

> GetNetworkSensorAlertsProfiles200ResponseInner getNetworkSensorAlertsProfile(networkId, id)

Show details of a sensor alert profile for a network.

Show details of a sensor alert profile for a network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SensorApi();
let networkId = "networkId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.getNetworkSensorAlertsProfile(networkId, id, (error, data, response) => {
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
 **networkId** | **String**|  | 
 **id** | **String**|  | 

### Return type

[**GetNetworkSensorAlertsProfiles200ResponseInner**](GetNetworkSensorAlertsProfiles200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSensorAlertsProfiles

> [GetNetworkSensorAlertsProfiles200ResponseInner] getNetworkSensorAlertsProfiles(networkId)

Lists all sensor alert profiles for a network.

Lists all sensor alert profiles for a network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SensorApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSensorAlertsProfiles(networkId, (error, data, response) => {
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
 **networkId** | **String**|  | 

### Return type

[**[GetNetworkSensorAlertsProfiles200ResponseInner]**](GetNetworkSensorAlertsProfiles200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSensorRelationships

> [GetNetworkSensorRelationships200ResponseInner] getNetworkSensorRelationships(networkId)

List the sensor roles for devices in a given network

List the sensor roles for devices in a given network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SensorApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSensorRelationships(networkId, (error, data, response) => {
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
 **networkId** | **String**|  | 

### Return type

[**[GetNetworkSensorRelationships200ResponseInner]**](GetNetworkSensorRelationships200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationSensorReadingsHistory

> [GetOrganizationSensorReadingsHistory200ResponseInner] getOrganizationSensorReadingsHistory(organizationId, opts)

Return all reported readings from sensors in a given timespan, sorted by timestamp

Return all reported readings from sensors in a given timespan, sorted by timestamp

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SensorApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example", // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 365 days and 6 hours from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 2 hours.
  'networkIds': ["null"], // [String] | Optional parameter to filter readings by network.
  'serials': ["null"], // [String] | Optional parameter to filter readings by sensor.
  'metrics': ["null"] // [String] | Types of sensor readings to retrieve. If no metrics are supplied, all available types of readings will be retrieved. Allowed values are battery, button, door, humidity, indoorAirQuality, noise, pm25, temperature, tvoc, and water.
};
apiInstance.getOrganizationSensorReadingsHistory(organizationId, opts, (error, data, response) => {
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
 **organizationId** | **String**|  | 
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 365 days and 6 hours from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 2 hours. | [optional] 
 **networkIds** | [**[String]**](String.md)| Optional parameter to filter readings by network. | [optional] 
 **serials** | [**[String]**](String.md)| Optional parameter to filter readings by sensor. | [optional] 
 **metrics** | [**[String]**](String.md)| Types of sensor readings to retrieve. If no metrics are supplied, all available types of readings will be retrieved. Allowed values are battery, button, door, humidity, indoorAirQuality, noise, pm25, temperature, tvoc, and water. | [optional] 

### Return type

[**[GetOrganizationSensorReadingsHistory200ResponseInner]**](GetOrganizationSensorReadingsHistory200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationSensorReadingsLatest

> [GetOrganizationSensorReadingsLatest200ResponseInner] getOrganizationSensorReadingsLatest(organizationId, opts)

Return the latest available reading for each metric from each sensor, sorted by sensor serial

Return the latest available reading for each metric from each sensor, sorted by sensor serial

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SensorApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 3 - 100. Default is 100.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example", // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'networkIds': ["null"], // [String] | Optional parameter to filter readings by network.
  'serials': ["null"], // [String] | Optional parameter to filter readings by sensor.
  'metrics': ["null"] // [String] | Types of sensor readings to retrieve. If no metrics are supplied, all available types of readings will be retrieved. Allowed values are battery, button, door, humidity, indoorAirQuality, noise, pm25, temperature, tvoc, and water.
};
apiInstance.getOrganizationSensorReadingsLatest(organizationId, opts, (error, data, response) => {
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
 **organizationId** | **String**|  | 
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 3 - 100. Default is 100. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **networkIds** | [**[String]**](String.md)| Optional parameter to filter readings by network. | [optional] 
 **serials** | [**[String]**](String.md)| Optional parameter to filter readings by sensor. | [optional] 
 **metrics** | [**[String]**](String.md)| Types of sensor readings to retrieve. If no metrics are supplied, all available types of readings will be retrieved. Allowed values are battery, button, door, humidity, indoorAirQuality, noise, pm25, temperature, tvoc, and water. | [optional] 

### Return type

[**[GetOrganizationSensorReadingsLatest200ResponseInner]**](GetOrganizationSensorReadingsLatest200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateDeviceSensorRelationships

> GetDeviceSensorRelationships200ResponseInner updateDeviceSensorRelationships(serial, opts)

Assign one or more sensor roles to a given sensor or camera device.

Assign one or more sensor roles to a given sensor or camera device.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SensorApi();
let serial = "serial_example"; // String | 
let opts = {
  'updateDeviceSensorRelationshipsRequest': new MerakiDashboardApi.UpdateDeviceSensorRelationshipsRequest() // UpdateDeviceSensorRelationshipsRequest | 
};
apiInstance.updateDeviceSensorRelationships(serial, opts, (error, data, response) => {
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
 **serial** | **String**|  | 
 **updateDeviceSensorRelationshipsRequest** | [**UpdateDeviceSensorRelationshipsRequest**](UpdateDeviceSensorRelationshipsRequest.md)|  | [optional] 

### Return type

[**GetDeviceSensorRelationships200ResponseInner**](GetDeviceSensorRelationships200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSensorAlertsProfile

> GetNetworkSensorAlertsProfiles200ResponseInner updateNetworkSensorAlertsProfile(networkId, id, opts)

Updates a sensor alert profile for a network.

Updates a sensor alert profile for a network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SensorApi();
let networkId = "networkId_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'updateNetworkSensorAlertsProfileRequest': new MerakiDashboardApi.UpdateNetworkSensorAlertsProfileRequest() // UpdateNetworkSensorAlertsProfileRequest | 
};
apiInstance.updateNetworkSensorAlertsProfile(networkId, id, opts, (error, data, response) => {
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
 **networkId** | **String**|  | 
 **id** | **String**|  | 
 **updateNetworkSensorAlertsProfileRequest** | [**UpdateNetworkSensorAlertsProfileRequest**](UpdateNetworkSensorAlertsProfileRequest.md)|  | [optional] 

### Return type

[**GetNetworkSensorAlertsProfiles200ResponseInner**](GetNetworkSensorAlertsProfiles200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

