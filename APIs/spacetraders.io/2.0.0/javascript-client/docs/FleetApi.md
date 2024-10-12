# SpaceTradersApi.FleetApi

All URIs are relative to *https://api.spacetraders.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createChart**](FleetApi.md#createChart) | **POST** /my/ships/{shipSymbol}/chart | Create Chart
[**createShipShipScan**](FleetApi.md#createShipShipScan) | **POST** /my/ships/{shipSymbol}/scan/ships | Scan Ships
[**createShipSystemScan**](FleetApi.md#createShipSystemScan) | **POST** /my/ships/{shipSymbol}/scan/systems | Scan Systems
[**createShipWaypointScan**](FleetApi.md#createShipWaypointScan) | **POST** /my/ships/{shipSymbol}/scan/waypoints | Scan Waypoints
[**createSurvey**](FleetApi.md#createSurvey) | **POST** /my/ships/{shipSymbol}/survey | Create Survey
[**dockShip**](FleetApi.md#dockShip) | **POST** /my/ships/{shipSymbol}/dock | Dock Ship
[**extractResources**](FleetApi.md#extractResources) | **POST** /my/ships/{shipSymbol}/extract | Extract Resources
[**getMyShip**](FleetApi.md#getMyShip) | **GET** /my/ships/{shipSymbol} | Get Ship
[**getMyShipCargo**](FleetApi.md#getMyShipCargo) | **GET** /my/ships/{shipSymbol}/cargo | Get Ship Cargo
[**getMyShips**](FleetApi.md#getMyShips) | **GET** /my/ships | List Ships
[**getShipCooldown**](FleetApi.md#getShipCooldown) | **GET** /my/ships/{shipSymbol}/cooldown | Get Ship Cooldown
[**getShipNav**](FleetApi.md#getShipNav) | **GET** /my/ships/{shipSymbol}/nav | Get Ship Nav
[**jettison**](FleetApi.md#jettison) | **POST** /my/ships/{shipSymbol}/jettison | Jettison Cargo
[**jumpShip**](FleetApi.md#jumpShip) | **POST** /my/ships/{shipSymbol}/jump | Jump Ship
[**navigateShip**](FleetApi.md#navigateShip) | **POST** /my/ships/{shipSymbol}/navigate | Navigate Ship
[**orbitShip**](FleetApi.md#orbitShip) | **POST** /my/ships/{shipSymbol}/orbit | Orbit Ship
[**patchShipNav**](FleetApi.md#patchShipNav) | **PATCH** /my/ships/{shipSymbol}/nav | Patch Ship Nav
[**purchaseCargo**](FleetApi.md#purchaseCargo) | **POST** /my/ships/{shipSymbol}/purchase | Purchase Cargo
[**purchaseShip**](FleetApi.md#purchaseShip) | **POST** /my/ships | Purchase Ship
[**refuelShip**](FleetApi.md#refuelShip) | **POST** /my/ships/{shipSymbol}/refuel | Refuel Ship
[**sellCargo**](FleetApi.md#sellCargo) | **POST** /my/ships/{shipSymbol}/sell | Sell Cargo
[**shipRefine**](FleetApi.md#shipRefine) | **POST** /my/ships/{shipSymbol}/refine | Ship Refine
[**transferCargo**](FleetApi.md#transferCargo) | **POST** /my/ships/{shipSymbol}/transfer | Transfer Cargo
[**warpShip**](FleetApi.md#warpShip) | **POST** /my/ships/{shipSymbol}/warp | Warp Ship



## createChart

> CreateChart201Response createChart(shipSymbol)

Create Chart

Command a ship to chart the current waypoint.  Waypoints in the universe are uncharted by default. These locations will not show up in the API until they have been charted by a ship.  Charting a location will record your agent as the one who created the chart.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.FleetApi();
let shipSymbol = "shipSymbol_example"; // String | The symbol of the ship
apiInstance.createChart(shipSymbol, (error, data, response) => {
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
 **shipSymbol** | **String**| The symbol of the ship | 

### Return type

[**CreateChart201Response**](CreateChart201Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createShipShipScan

> CreateShipShipScan201Response createShipShipScan(shipSymbol)

Scan Ships

Activate your ship&#39;s sensor arrays to scan for ship information.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.FleetApi();
let shipSymbol = "shipSymbol_example"; // String | 
apiInstance.createShipShipScan(shipSymbol, (error, data, response) => {
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
 **shipSymbol** | **String**|  | 

### Return type

[**CreateShipShipScan201Response**](CreateShipShipScan201Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createShipSystemScan

> CreateShipSystemScan201Response createShipSystemScan(shipSymbol)

Scan Systems

Activate your ship&#39;s sensor arrays to scan for system information.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.FleetApi();
let shipSymbol = "shipSymbol_example"; // String | 
apiInstance.createShipSystemScan(shipSymbol, (error, data, response) => {
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
 **shipSymbol** | **String**|  | 

### Return type

[**CreateShipSystemScan201Response**](CreateShipSystemScan201Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createShipWaypointScan

> CreateShipWaypointScan201Response createShipWaypointScan(shipSymbol)

Scan Waypoints

Activate your ship&#39;s sensor arrays to scan for waypoint information.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.FleetApi();
let shipSymbol = "shipSymbol_example"; // String | 
apiInstance.createShipWaypointScan(shipSymbol, (error, data, response) => {
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
 **shipSymbol** | **String**|  | 

### Return type

[**CreateShipWaypointScan201Response**](CreateShipWaypointScan201Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createSurvey

> CreateSurvey201Response createSurvey(shipSymbol)

Create Survey

If you want to target specific yields for an extraction, you can survey a waypoint, such as an asteroid field, and send the survey in the body of the extract request. Each survey may have multiple deposits, and if a symbol shows up more than once, that indicates a higher chance of extracting that resource.  Your ship will enter a cooldown between consecutive survey requests. Surveys will eventually expire after a period of time. Multiple ships can use the same survey for extraction.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.FleetApi();
let shipSymbol = "shipSymbol_example"; // String | The symbol of the ship
apiInstance.createSurvey(shipSymbol, (error, data, response) => {
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
 **shipSymbol** | **String**| The symbol of the ship | 

### Return type

[**CreateSurvey201Response**](CreateSurvey201Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dockShip

> DockShip200Response dockShip(shipSymbol)

Dock Ship

Attempt to dock your ship at it&#39;s current location. Docking will only succeed if the waypoint is a dockable location, and your ship is capable of docking at the time of the request.  The endpoint is idempotent - successive calls will succeed even if the ship is already docked.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.FleetApi();
let shipSymbol = "shipSymbol_example"; // String | The symbol of the ship
apiInstance.dockShip(shipSymbol, (error, data, response) => {
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
 **shipSymbol** | **String**| The symbol of the ship | 

### Return type

[**DockShip200Response**](DockShip200Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## extractResources

> ExtractResources201Response extractResources(shipSymbol, opts)

Extract Resources

Extract resources from the waypoint into your ship. Send an optional survey as the payload to target specific yields.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.FleetApi();
let shipSymbol = "shipSymbol_example"; // String | The ship symbol
let opts = {
  'extractResourcesRequest': new SpaceTradersApi.ExtractResourcesRequest() // ExtractResourcesRequest | 
};
apiInstance.extractResources(shipSymbol, opts, (error, data, response) => {
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
 **shipSymbol** | **String**| The ship symbol | 
 **extractResourcesRequest** | [**ExtractResourcesRequest**](ExtractResourcesRequest.md)|  | [optional] 

### Return type

[**ExtractResources201Response**](ExtractResources201Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getMyShip

> GetMyShip200Response getMyShip(shipSymbol)

Get Ship

Retrieve the details of your ship.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.FleetApi();
let shipSymbol = "shipSymbol_example"; // String | 
apiInstance.getMyShip(shipSymbol, (error, data, response) => {
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
 **shipSymbol** | **String**|  | 

### Return type

[**GetMyShip200Response**](GetMyShip200Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMyShipCargo

> GetMyShipCargo200Response getMyShipCargo(shipSymbol)

Get Ship Cargo

Retrieve the cargo of your ship.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.FleetApi();
let shipSymbol = "shipSymbol_example"; // String | The symbol of the ship
apiInstance.getMyShipCargo(shipSymbol, (error, data, response) => {
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
 **shipSymbol** | **String**| The symbol of the ship | 

### Return type

[**GetMyShipCargo200Response**](GetMyShipCargo200Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMyShips

> GetMyShips200Response getMyShips(opts)

List Ships

Retrieve all of your ships.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.FleetApi();
let opts = {
  'page': 56, // Number | What entry offset to request
  'limit': 56 // Number | How many entries to return per page
};
apiInstance.getMyShips(opts, (error, data, response) => {
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

[**GetMyShips200Response**](GetMyShips200Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getShipCooldown

> GetShipCooldown200Response getShipCooldown(shipSymbol)

Get Ship Cooldown

Retrieve the details of your ship&#39;s reactor cooldown. Some actions such as activating your jump drive, scanning, or extracting resources taxes your reactor and results in a cooldown.  Your ship cannot perform additional actions until your cooldown has expired. The duration of your cooldown is relative to the power consumption of the related modules or mounts for the action taken.  Response returns a 204 status code (no-content) when the ship has no cooldown.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.FleetApi();
let shipSymbol = "shipSymbol_example"; // String | 
apiInstance.getShipCooldown(shipSymbol, (error, data, response) => {
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
 **shipSymbol** | **String**|  | 

### Return type

[**GetShipCooldown200Response**](GetShipCooldown200Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getShipNav

> GetShipNav200Response getShipNav(shipSymbol)

Get Ship Nav

Get the current nav status of a ship.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.FleetApi();
let shipSymbol = "shipSymbol_example"; // String | The ship symbol
apiInstance.getShipNav(shipSymbol, (error, data, response) => {
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
 **shipSymbol** | **String**| The ship symbol | 

### Return type

[**GetShipNav200Response**](GetShipNav200Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jettison

> Jettison200Response jettison(shipSymbol, opts)

Jettison Cargo

Jettison cargo from your ship&#39;s cargo hold.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.FleetApi();
let shipSymbol = "shipSymbol_example"; // String | 
let opts = {
  'jettisonRequest': new SpaceTradersApi.JettisonRequest() // JettisonRequest | 
};
apiInstance.jettison(shipSymbol, opts, (error, data, response) => {
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
 **shipSymbol** | **String**|  | 
 **jettisonRequest** | [**JettisonRequest**](JettisonRequest.md)|  | [optional] 

### Return type

[**Jettison200Response**](Jettison200Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## jumpShip

> JumpShip200Response jumpShip(shipSymbol, opts)

Jump Ship

Jump your ship instantly to a target system. Unlike other forms of navigation, jumping requires a unit of antimatter.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.FleetApi();
let shipSymbol = "shipSymbol_example"; // String | 
let opts = {
  'jumpShipRequest': new SpaceTradersApi.JumpShipRequest() // JumpShipRequest | 
};
apiInstance.jumpShip(shipSymbol, opts, (error, data, response) => {
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
 **shipSymbol** | **String**|  | 
 **jumpShipRequest** | [**JumpShipRequest**](JumpShipRequest.md)|  | [optional] 

### Return type

[**JumpShip200Response**](JumpShip200Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## navigateShip

> NavigateShip200Response navigateShip(shipSymbol, opts)

Navigate Ship

Navigate to a target destination. The destination must be located within the same system as the ship. Navigating will consume the necessary fuel and supplies from the ship&#39;s manifest, and will pay out crew wages from the agent&#39;s account.  The returned response will detail the route information including the expected time of arrival. Most ship actions are unavailable until the ship has arrived at it&#39;s destination.  To travel between systems, see the ship&#39;s warp or jump actions.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.FleetApi();
let shipSymbol = "shipSymbol_example"; // String | The ship symbol
let opts = {
  'navigateShipRequest': new SpaceTradersApi.NavigateShipRequest() // NavigateShipRequest | 
};
apiInstance.navigateShip(shipSymbol, opts, (error, data, response) => {
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
 **shipSymbol** | **String**| The ship symbol | 
 **navigateShipRequest** | [**NavigateShipRequest**](NavigateShipRequest.md)|  | [optional] 

### Return type

[**NavigateShip200Response**](NavigateShip200Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## orbitShip

> OrbitShip200Response orbitShip(shipSymbol)

Orbit Ship

Attempt to move your ship into orbit at it&#39;s current location. The request will only succeed if your ship is capable of moving into orbit at the time of the request.  The endpoint is idempotent - successive calls will succeed even if the ship is already in orbit.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.FleetApi();
let shipSymbol = "shipSymbol_example"; // String | The symbol of the ship
apiInstance.orbitShip(shipSymbol, (error, data, response) => {
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
 **shipSymbol** | **String**| The symbol of the ship | 

### Return type

[**OrbitShip200Response**](OrbitShip200Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchShipNav

> GetShipNav200Response patchShipNav(shipSymbol, opts)

Patch Ship Nav

Update the nav data of a ship, such as the flight mode.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.FleetApi();
let shipSymbol = "shipSymbol_example"; // String | The ship symbol
let opts = {
  'patchShipNavRequest': new SpaceTradersApi.PatchShipNavRequest() // PatchShipNavRequest | 
};
apiInstance.patchShipNav(shipSymbol, opts, (error, data, response) => {
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
 **shipSymbol** | **String**| The ship symbol | 
 **patchShipNavRequest** | [**PatchShipNavRequest**](PatchShipNavRequest.md)|  | [optional] 

### Return type

[**GetShipNav200Response**](GetShipNav200Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## purchaseCargo

> PurchaseCargo201Response purchaseCargo(shipSymbol, opts)

Purchase Cargo

Purchase cargo.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.FleetApi();
let shipSymbol = "shipSymbol_example"; // String | 
let opts = {
  'purchaseCargoRequest': new SpaceTradersApi.PurchaseCargoRequest() // PurchaseCargoRequest | 
};
apiInstance.purchaseCargo(shipSymbol, opts, (error, data, response) => {
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
 **shipSymbol** | **String**|  | 
 **purchaseCargoRequest** | [**PurchaseCargoRequest**](PurchaseCargoRequest.md)|  | [optional] 

### Return type

[**PurchaseCargo201Response**](PurchaseCargo201Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## purchaseShip

> PurchaseShip201Response purchaseShip(opts)

Purchase Ship

Purchase a ship

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.FleetApi();
let opts = {
  'purchaseShipRequest': new SpaceTradersApi.PurchaseShipRequest() // PurchaseShipRequest | 
};
apiInstance.purchaseShip(opts, (error, data, response) => {
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
 **purchaseShipRequest** | [**PurchaseShipRequest**](PurchaseShipRequest.md)|  | [optional] 

### Return type

[**PurchaseShip201Response**](PurchaseShip201Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## refuelShip

> RefuelShip200Response refuelShip(shipSymbol)

Refuel Ship

Refuel your ship from the local market.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.FleetApi();
let shipSymbol = "shipSymbol_example"; // String | 
apiInstance.refuelShip(shipSymbol, (error, data, response) => {
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
 **shipSymbol** | **String**|  | 

### Return type

[**RefuelShip200Response**](RefuelShip200Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sellCargo

> SellCargo201Response sellCargo(shipSymbol, opts)

Sell Cargo

Sell cargo.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.FleetApi();
let shipSymbol = "shipSymbol_example"; // String | 
let opts = {
  'sellCargoRequest': new SpaceTradersApi.SellCargoRequest() // SellCargoRequest | 
};
apiInstance.sellCargo(shipSymbol, opts, (error, data, response) => {
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
 **shipSymbol** | **String**|  | 
 **sellCargoRequest** | [**SellCargoRequest**](SellCargoRequest.md)|  | [optional] 

### Return type

[**SellCargo201Response**](SellCargo201Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## shipRefine

> ShipRefine200Response shipRefine(shipSymbol, opts)

Ship Refine

Attempt to refine the raw materials on your ship. The request will only succeed if your ship is capable of refining at the time of the request.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.FleetApi();
let shipSymbol = "shipSymbol_example"; // String | The symbol of the ship
let opts = {
  'shipRefineRequest': new SpaceTradersApi.ShipRefineRequest() // ShipRefineRequest | 
};
apiInstance.shipRefine(shipSymbol, opts, (error, data, response) => {
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
 **shipSymbol** | **String**| The symbol of the ship | 
 **shipRefineRequest** | [**ShipRefineRequest**](ShipRefineRequest.md)|  | [optional] 

### Return type

[**ShipRefine200Response**](ShipRefine200Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transferCargo

> TransferCargo200Response transferCargo(shipSymbol, opts)

Transfer Cargo

Transfer cargo between ships.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.FleetApi();
let shipSymbol = "shipSymbol_example"; // String | 
let opts = {
  'transferCargoRequest': new SpaceTradersApi.TransferCargoRequest() // TransferCargoRequest | 
};
apiInstance.transferCargo(shipSymbol, opts, (error, data, response) => {
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
 **shipSymbol** | **String**|  | 
 **transferCargoRequest** | [**TransferCargoRequest**](TransferCargoRequest.md)|  | [optional] 

### Return type

[**TransferCargo200Response**](TransferCargo200Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## warpShip

> NavigateShip200Response warpShip(shipSymbol, opts)

Warp Ship

Warp your ship to a target destination in another system. Warping will consume the necessary fuel and supplies from the ship&#39;s manifest, and will pay out crew wages from the agent&#39;s account.  The returned response will detail the route information including the expected time of arrival. Most ship actions are unavailable until the ship has arrived at it&#39;s destination.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.FleetApi();
let shipSymbol = "shipSymbol_example"; // String | 
let opts = {
  'navigateShipRequest': new SpaceTradersApi.NavigateShipRequest() // NavigateShipRequest | 
};
apiInstance.warpShip(shipSymbol, opts, (error, data, response) => {
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
 **shipSymbol** | **String**|  | 
 **navigateShipRequest** | [**NavigateShipRequest**](NavigateShipRequest.md)|  | [optional] 

### Return type

[**NavigateShip200Response**](NavigateShip200Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

