# SpaceTradersApi.SystemsApi

All URIs are relative to *https://api.spacetraders.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getJumpGate**](SystemsApi.md#getJumpGate) | **GET** /systems/{systemSymbol}/waypoints/{waypointSymbol}/jump-gate | Get Jump Gate
[**getMarket**](SystemsApi.md#getMarket) | **GET** /systems/{systemSymbol}/waypoints/{waypointSymbol}/market | Get Market
[**getShipyard**](SystemsApi.md#getShipyard) | **GET** /systems/{systemSymbol}/waypoints/{waypointSymbol}/shipyard | Get Shipyard
[**getSystem**](SystemsApi.md#getSystem) | **GET** /systems/{systemSymbol} | Get System
[**getSystemWaypoints**](SystemsApi.md#getSystemWaypoints) | **GET** /systems/{systemSymbol}/waypoints | List Waypoints
[**getSystems**](SystemsApi.md#getSystems) | **GET** /systems | List Systems
[**getWaypoint**](SystemsApi.md#getWaypoint) | **GET** /systems/{systemSymbol}/waypoints/{waypointSymbol} | Get Waypoint



## getJumpGate

> GetJumpGate200Response getJumpGate(systemSymbol, waypointSymbol)

Get Jump Gate

Get jump gate details for a waypoint.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.SystemsApi();
let systemSymbol = "systemSymbol_example"; // String | The system symbol
let waypointSymbol = "waypointSymbol_example"; // String | The waypoint symbol
apiInstance.getJumpGate(systemSymbol, waypointSymbol, (error, data, response) => {
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
 **systemSymbol** | **String**| The system symbol | 
 **waypointSymbol** | **String**| The waypoint symbol | 

### Return type

[**GetJumpGate200Response**](GetJumpGate200Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMarket

> GetMarket200Response getMarket(systemSymbol, waypointSymbol)

Get Market

Retrieve imports, exports and exchange data from a marketplace. Imports can be sold, exports can be purchased, and exchange goods can be purchased or sold. Send a ship to the waypoint to access trade good prices and recent transactions.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.SystemsApi();
let systemSymbol = "systemSymbol_example"; // String | The system symbol
let waypointSymbol = "waypointSymbol_example"; // String | The waypoint symbol
apiInstance.getMarket(systemSymbol, waypointSymbol, (error, data, response) => {
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
 **systemSymbol** | **String**| The system symbol | 
 **waypointSymbol** | **String**| The waypoint symbol | 

### Return type

[**GetMarket200Response**](GetMarket200Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getShipyard

> GetShipyard200Response getShipyard(systemSymbol, waypointSymbol)

Get Shipyard

Get the shipyard for a waypoint. Send a ship to the waypoint to access ships that are currently available for purchase and recent transactions.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.SystemsApi();
let systemSymbol = "systemSymbol_example"; // String | The system symbol
let waypointSymbol = "waypointSymbol_example"; // String | The waypoint symbol
apiInstance.getShipyard(systemSymbol, waypointSymbol, (error, data, response) => {
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
 **systemSymbol** | **String**| The system symbol | 
 **waypointSymbol** | **String**| The waypoint symbol | 

### Return type

[**GetShipyard200Response**](GetShipyard200Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSystem

> GetSystem200Response getSystem(systemSymbol)

Get System

Get the details of a system.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.SystemsApi();
let systemSymbol = "'X1-OE'"; // String | The system symbol
apiInstance.getSystem(systemSymbol, (error, data, response) => {
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
 **systemSymbol** | **String**| The system symbol | [default to &#39;X1-OE&#39;]

### Return type

[**GetSystem200Response**](GetSystem200Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSystemWaypoints

> GetSystemWaypoints200Response getSystemWaypoints(systemSymbol, opts)

List Waypoints

Fetch all of the waypoints for a given system. System must be charted or a ship must be present to return waypoint details.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.SystemsApi();
let systemSymbol = "systemSymbol_example"; // String | The system symbol
let opts = {
  'page': 56, // Number | What entry offset to request
  'limit': 56 // Number | How many entries to return per page
};
apiInstance.getSystemWaypoints(systemSymbol, opts, (error, data, response) => {
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
 **systemSymbol** | **String**| The system symbol | 
 **page** | **Number**| What entry offset to request | [optional] 
 **limit** | **Number**| How many entries to return per page | [optional] 

### Return type

[**GetSystemWaypoints200Response**](GetSystemWaypoints200Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSystems

> GetSystems200Response getSystems(opts)

List Systems

Return a list of all systems.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.SystemsApi();
let opts = {
  'page': 56, // Number | What entry offset to request
  'limit': 56 // Number | How many entries to return per page
};
apiInstance.getSystems(opts, (error, data, response) => {
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
 **page** | **Number**| What entry offset to request | [optional] 
 **limit** | **Number**| How many entries to return per page | [optional] 

### Return type

[**GetSystems200Response**](GetSystems200Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWaypoint

> GetWaypoint200Response getWaypoint(systemSymbol, waypointSymbol)

Get Waypoint

View the details of a waypoint.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.SystemsApi();
let systemSymbol = "systemSymbol_example"; // String | The system symbol
let waypointSymbol = "waypointSymbol_example"; // String | The waypoint symbol
apiInstance.getWaypoint(systemSymbol, waypointSymbol, (error, data, response) => {
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
 **systemSymbol** | **String**| The system symbol | 
 **waypointSymbol** | **String**| The waypoint symbol | 

### Return type

[**GetWaypoint200Response**](GetWaypoint200Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

