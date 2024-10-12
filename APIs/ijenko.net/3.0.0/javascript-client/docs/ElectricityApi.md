# IoEIoTApiToCreateEndUserApplications.ElectricityApi

All URIs are relative to *https://ioe2api.ijenko.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**placeElectricityAutonomy**](ElectricityApi.md#placeElectricityAutonomy) | **GET** /places/{placeId}/electricity/autonomy | Get autonomy rate of the place
[**placeElectricityGetFlows**](ElectricityApi.md#placeElectricityGetFlows) | **GET** /places/{placeId}/electricity/flows | Get electricity virtual flows
[**placeElectricityGetFlowsSetup**](ElectricityApi.md#placeElectricityGetFlowsSetup) | **GET** /places/{placeId}/electricity/flows/setup | Get electricity flows setup
[**placeElectricitySelfConsumption**](ElectricityApi.md#placeElectricitySelfConsumption) | **GET** /places/{placeId}/electricity/self-consumption | Get self-consumption rate of the place



## placeElectricityAutonomy

> ElectricityAutonomy placeElectricityAutonomy(placeId, when, span)

Get autonomy rate of the place

Compute the autonomy rate of the *Place* on a time period.  &#x60;autonomy &#x3D; 1 - (elec_drawn / elec_total_usage)&#x60; 

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.ElectricityApi();
let placeId = "placeId_example"; // String | Unique identifier of a *Place*.
let when = new Date("2013-10-20T19:20:30+01:00"); // Date | A time part of the time span.
let span = "span_example"; // String | Timespan: H (hour), D (day), Wmo (week starting on Monday), Wsu (week starting on Sunday), M (month), Y (year)
apiInstance.placeElectricityAutonomy(placeId, when, span, (error, data, response) => {
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
 **placeId** | **String**| Unique identifier of a *Place*. | 
 **when** | **Date**| A time part of the time span. | 
 **span** | **String**| Timespan: H (hour), D (day), Wmo (week starting on Monday), Wsu (week starting on Sunday), M (month), Y (year) | 

### Return type

[**ElectricityAutonomy**](ElectricityAutonomy.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## placeElectricityGetFlows

> ElectricityFlows placeElectricityGetFlows(placeId, flows)

Get electricity virtual flows

Get the mapping of virtual electricity flows to functionalities.  Some rules are applied to expand the virtual flows using the concrete flows available.  The &#x60;factor&#x60; tells how each energy value coming from a functionality must be added with values from other functionality to compute the energy of the virtual flow. Factors are usually &#x60;1&#x60; or &#x60;-1&#x60;.  The &#x60;code&#x60; property gives the result which may be partial: - If all flows are available, &#x60;200000&#x60; is returned. - If no flows are available (indicating that the place has no   electricity functionality or that no functionality has been attached   to a flow), the &#x60;code&#x60; is &#x60;200001&#x60;. The &#x60;missing&#x60; property contains   all the requested flows. - If some flows are missing, the &#x60;code&#x60; is &#x60;200002&#x60; and the &#x60;missing&#x60;   property lists them. 

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.ElectricityApi();
let placeId = "placeId_example"; // String | Unique identifier of a *Place*.
let flows = ["null"]; // [String] | Names of the flows requested
apiInstance.placeElectricityGetFlows(placeId, flows, (error, data, response) => {
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
 **placeId** | **String**| Unique identifier of a *Place*. | 
 **flows** | [**[String]**](String.md)| Names of the flows requested | 

### Return type

[**ElectricityFlows**](ElectricityFlows.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## placeElectricityGetFlowsSetup

> ElectricityFlowsSetup placeElectricityGetFlowsSetup(placeId)

Get electricity flows setup

Get the mapping of functionalities to electricity flows.  A functionality is attached to *at most* one flow. 

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.ElectricityApi();
let placeId = "placeId_example"; // String | Unique identifier of a *Place*.
apiInstance.placeElectricityGetFlowsSetup(placeId, (error, data, response) => {
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
 **placeId** | **String**| Unique identifier of a *Place*. | 

### Return type

[**ElectricityFlowsSetup**](ElectricityFlowsSetup.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## placeElectricitySelfConsumption

> ElectricitySelfConsumption placeElectricitySelfConsumption(placeId, when, span)

Get self-consumption rate of the place

Compute the self-consumption rate of the *Place* on a time period.  &#x60;selfConsumption &#x3D; 1 - (elec_feed_in / elec_total_usage)&#x60; 

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.ElectricityApi();
let placeId = "placeId_example"; // String | Unique identifier of a *Place*.
let when = new Date("2013-10-20T19:20:30+01:00"); // Date | A time part of the time span.
let span = "span_example"; // String | Timespan: H (hour), D (day), Wmo (week starting on Monday), Wsu (week starting on Sunday), M (month), Y (year)
apiInstance.placeElectricitySelfConsumption(placeId, when, span, (error, data, response) => {
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
 **placeId** | **String**| Unique identifier of a *Place*. | 
 **when** | **Date**| A time part of the time span. | 
 **span** | **String**| Timespan: H (hour), D (day), Wmo (week starting on Monday), Wsu (week starting on Sunday), M (month), Y (year) | 

### Return type

[**ElectricitySelfConsumption**](ElectricitySelfConsumption.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

