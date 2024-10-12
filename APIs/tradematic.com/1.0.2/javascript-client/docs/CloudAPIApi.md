# TradematicCloudApi.CloudAPIApi

All URIs are relative to *https://api.tradematic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloudAccountsAccountidCloseallPost**](CloudAPIApi.md#cloudAccountsAccountidCloseallPost) | **POST** /cloud/accounts/{accountid}/closeall | Close all positions by account
[**cloudAccountsAccountidGet**](CloudAPIApi.md#cloudAccountsAccountidGet) | **GET** /cloud/accounts/{accountid} | Get trading account by ID
[**cloudAccountsAccountidOrdersGet**](CloudAPIApi.md#cloudAccountsAccountidOrdersGet) | **GET** /cloud/accounts/{accountid}/orders | Get orders list by account
[**cloudAccountsAccountidOrdersOrderidDelete**](CloudAPIApi.md#cloudAccountsAccountidOrdersOrderidDelete) | **DELETE** /cloud/accounts/{accountid}/orders/{orderid} | Cancel an order by ID
[**cloudAccountsAccountidOrdersPost**](CloudAPIApi.md#cloudAccountsAccountidOrdersPost) | **POST** /cloud/accounts/{accountid}/orders | Place a new order
[**cloudAccountsAccountidSnapshotsGet**](CloudAPIApi.md#cloudAccountsAccountidSnapshotsGet) | **GET** /cloud/accounts/{accountid}/snapshots | Get account equity and cash snapshots
[**cloudAccountsAccountidSyncPost**](CloudAPIApi.md#cloudAccountsAccountidSyncPost) | **POST** /cloud/accounts/{accountid}/sync | Syhchronize an account with account active strategies
[**cloudAccountsAccountidTradesGet**](CloudAPIApi.md#cloudAccountsAccountidTradesGet) | **GET** /cloud/accounts/{accountid}/trades | Get trades list by account
[**cloudAccountsGet**](CloudAPIApi.md#cloudAccountsGet) | **GET** /cloud/accounts | Get trading accounts list
[**cloudCommandsCommandidGet**](CloudAPIApi.md#cloudCommandsCommandidGet) | **GET** /cloud/commands/{commandid} | Get command by ID
[**cloudCommandsGet**](CloudAPIApi.md#cloudCommandsGet) | **GET** /cloud/commands | Get commands list
[**cloudConnectionsConnectionidDelete**](CloudAPIApi.md#cloudConnectionsConnectionidDelete) | **DELETE** /cloud/connections/{connectionid} | Delete connection by ID
[**cloudConnectionsConnectionidGet**](CloudAPIApi.md#cloudConnectionsConnectionidGet) | **GET** /cloud/connections/{connectionid} | Get connection by ID
[**cloudConnectionsConnectionidPut**](CloudAPIApi.md#cloudConnectionsConnectionidPut) | **PUT** /cloud/connections/{connectionid} | Update existing connection
[**cloudConnectionsGet**](CloudAPIApi.md#cloudConnectionsGet) | **GET** /cloud/connections | Get connections list
[**cloudConnectionsPost**](CloudAPIApi.md#cloudConnectionsPost) | **POST** /cloud/connections | Create a new connection
[**cloudConnectorsConnectoridGet**](CloudAPIApi.md#cloudConnectorsConnectoridGet) | **GET** /cloud/connectors/{connectorid} | Get connector by ID
[**cloudConnectorsGet**](CloudAPIApi.md#cloudConnectorsGet) | **GET** /cloud/connectors | Get available connectors list
[**cloudSessionsGet**](CloudAPIApi.md#cloudSessionsGet) | **GET** /cloud/sessions | Get sessions list
[**cloudSessionsSessionidGet**](CloudAPIApi.md#cloudSessionsSessionidGet) | **GET** /cloud/sessions/{sessionid} | Get session by ID
[**cloudStrategiesGet**](CloudAPIApi.md#cloudStrategiesGet) | **GET** /cloud/strategies | Get list of active (executing) strategies
[**cloudStrategiesStartPost**](CloudAPIApi.md#cloudStrategiesStartPost) | **POST** /cloud/strategies/start | Start a strategy execution for account
[**cloudStrategiesStrategyidGet**](CloudAPIApi.md#cloudStrategiesStrategyidGet) | **GET** /cloud/strategies/{strategyid} | Get active (executing) strategy by ID
[**cloudStrategiesStrategyidStopPost**](CloudAPIApi.md#cloudStrategiesStrategyidStopPost) | **POST** /cloud/strategies/{strategyid}/stop | Stop a strategy execution by ID



## cloudAccountsAccountidCloseallPost

> CloudAccountsAccountidCloseallPost202Response cloudAccountsAccountidCloseallPost(accountid)

Close all positions by account

Close all positions by account

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.CloudAPIApi();
let accountid = 789; // Number | 
apiInstance.cloudAccountsAccountidCloseallPost(accountid, (error, data, response) => {
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
 **accountid** | **Number**|  | 

### Return type

[**CloudAccountsAccountidCloseallPost202Response**](CloudAccountsAccountidCloseallPost202Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudAccountsAccountidGet

> Account cloudAccountsAccountidGet(accountid)

Get trading account by ID

Get trading account by ID

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.CloudAPIApi();
let accountid = 789; // Number | 
apiInstance.cloudAccountsAccountidGet(accountid, (error, data, response) => {
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
 **accountid** | **Number**|  | 

### Return type

[**Account**](Account.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudAccountsAccountidOrdersGet

> [Order] cloudAccountsAccountidOrdersGet(accountid)

Get orders list by account

Get orders list by account

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.CloudAPIApi();
let accountid = 789; // Number | 
apiInstance.cloudAccountsAccountidOrdersGet(accountid, (error, data, response) => {
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
 **accountid** | **Number**|  | 

### Return type

[**[Order]**](Order.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudAccountsAccountidOrdersOrderidDelete

> CloudAccountsAccountidCloseallPost202Response cloudAccountsAccountidOrdersOrderidDelete(accountid, orderid)

Cancel an order by ID

Cancel an order by ID

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.CloudAPIApi();
let accountid = 789; // Number | 
let orderid = 789; // Number | 
apiInstance.cloudAccountsAccountidOrdersOrderidDelete(accountid, orderid, (error, data, response) => {
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
 **accountid** | **Number**|  | 
 **orderid** | **Number**|  | 

### Return type

[**CloudAccountsAccountidCloseallPost202Response**](CloudAccountsAccountidCloseallPost202Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudAccountsAccountidOrdersPost

> CloudAccountsAccountidCloseallPost202Response cloudAccountsAccountidOrdersPost(accountid, body)

Place a new order

Place a new order

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.CloudAPIApi();
let accountid = 789; // Number | 
let body = new TradematicCloudApi.CloudAccountsAccountidOrdersPostRequest(); // CloudAccountsAccountidOrdersPostRequest | 
apiInstance.cloudAccountsAccountidOrdersPost(accountid, body, (error, data, response) => {
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
 **accountid** | **Number**|  | 
 **body** | [**CloudAccountsAccountidOrdersPostRequest**](CloudAccountsAccountidOrdersPostRequest.md)|  | 

### Return type

[**CloudAccountsAccountidCloseallPost202Response**](CloudAccountsAccountidCloseallPost202Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudAccountsAccountidSnapshotsGet

> [Snapshot] cloudAccountsAccountidSnapshotsGet(accountid)

Get account equity and cash snapshots

Get account equity and cash snapshots

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.CloudAPIApi();
let accountid = 789; // Number | 
apiInstance.cloudAccountsAccountidSnapshotsGet(accountid, (error, data, response) => {
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
 **accountid** | **Number**|  | 

### Return type

[**[Snapshot]**](Snapshot.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudAccountsAccountidSyncPost

> CloudAccountsAccountidCloseallPost202Response cloudAccountsAccountidSyncPost(accountid)

Syhchronize an account with account active strategies

Syhchronize an account with account active strategies

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.CloudAPIApi();
let accountid = 789; // Number | 
apiInstance.cloudAccountsAccountidSyncPost(accountid, (error, data, response) => {
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
 **accountid** | **Number**|  | 

### Return type

[**CloudAccountsAccountidCloseallPost202Response**](CloudAccountsAccountidCloseallPost202Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudAccountsAccountidTradesGet

> [Trade] cloudAccountsAccountidTradesGet(accountid)

Get trades list by account

Get trades list by account

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.CloudAPIApi();
let accountid = 789; // Number | 
apiInstance.cloudAccountsAccountidTradesGet(accountid, (error, data, response) => {
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
 **accountid** | **Number**|  | 

### Return type

[**[Trade]**](Trade.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudAccountsGet

> [Account] cloudAccountsGet()

Get trading accounts list

Get trading accounts list

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.CloudAPIApi();
apiInstance.cloudAccountsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Account]**](Account.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudCommandsCommandidGet

> Command cloudCommandsCommandidGet(commandid)

Get command by ID

Get command by ID

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.CloudAPIApi();
let commandid = 789; // Number | 
apiInstance.cloudCommandsCommandidGet(commandid, (error, data, response) => {
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
 **commandid** | **Number**|  | 

### Return type

[**Command**](Command.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudCommandsGet

> [Command] cloudCommandsGet()

Get commands list

Get commands list

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.CloudAPIApi();
apiInstance.cloudCommandsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Command]**](Command.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudConnectionsConnectionidDelete

> CloudConnectionsPost200Response cloudConnectionsConnectionidDelete(connectionid)

Delete connection by ID

Delete connection by ID

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.CloudAPIApi();
let connectionid = 789; // Number | 
apiInstance.cloudConnectionsConnectionidDelete(connectionid, (error, data, response) => {
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
 **connectionid** | **Number**|  | 

### Return type

[**CloudConnectionsPost200Response**](CloudConnectionsPost200Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudConnectionsConnectionidGet

> Connection cloudConnectionsConnectionidGet(connectionid)

Get connection by ID

Get connection by ID

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.CloudAPIApi();
let connectionid = 789; // Number | 
apiInstance.cloudConnectionsConnectionidGet(connectionid, (error, data, response) => {
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
 **connectionid** | **Number**|  | 

### Return type

[**Connection**](Connection.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudConnectionsConnectionidPut

> CloudConnectionsPost200Response cloudConnectionsConnectionidPut(connectionid, body)

Update existing connection

Update existing connection

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.CloudAPIApi();
let connectionid = 789; // Number | 
let body = new TradematicCloudApi.CloudConnectionsPostRequest(); // CloudConnectionsPostRequest | 
apiInstance.cloudConnectionsConnectionidPut(connectionid, body, (error, data, response) => {
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
 **connectionid** | **Number**|  | 
 **body** | [**CloudConnectionsPostRequest**](CloudConnectionsPostRequest.md)|  | 

### Return type

[**CloudConnectionsPost200Response**](CloudConnectionsPost200Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudConnectionsGet

> [Connection] cloudConnectionsGet()

Get connections list

Get connections list

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.CloudAPIApi();
apiInstance.cloudConnectionsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Connection]**](Connection.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudConnectionsPost

> CloudConnectionsPost200Response cloudConnectionsPost(body)

Create a new connection

Create a new connection

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.CloudAPIApi();
let body = new TradematicCloudApi.CloudConnectionsPostRequest(); // CloudConnectionsPostRequest | 
apiInstance.cloudConnectionsPost(body, (error, data, response) => {
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
 **body** | [**CloudConnectionsPostRequest**](CloudConnectionsPostRequest.md)|  | 

### Return type

[**CloudConnectionsPost200Response**](CloudConnectionsPost200Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudConnectorsConnectoridGet

> Connector cloudConnectorsConnectoridGet(connectorid)

Get connector by ID

Get connector by ID

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.CloudAPIApi();
let connectorid = 789; // Number | 
apiInstance.cloudConnectorsConnectoridGet(connectorid, (error, data, response) => {
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
 **connectorid** | **Number**|  | 

### Return type

[**Connector**](Connector.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudConnectorsGet

> [Connector] cloudConnectorsGet()

Get available connectors list

Get available connectors list

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.CloudAPIApi();
apiInstance.cloudConnectorsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Connector]**](Connector.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudSessionsGet

> [Session] cloudSessionsGet()

Get sessions list

Get sessions list

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.CloudAPIApi();
apiInstance.cloudSessionsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Session]**](Session.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudSessionsSessionidGet

> Session cloudSessionsSessionidGet(sessionid)

Get session by ID

Get session by ID

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.CloudAPIApi();
let sessionid = 789; // Number | 
apiInstance.cloudSessionsSessionidGet(sessionid, (error, data, response) => {
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
 **sessionid** | **Number**|  | 

### Return type

[**Session**](Session.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudStrategiesGet

> [CloudStrategy] cloudStrategiesGet()

Get list of active (executing) strategies

Get list of active (executing) strategies

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.CloudAPIApi();
apiInstance.cloudStrategiesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[CloudStrategy]**](CloudStrategy.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudStrategiesStartPost

> CloudAccountsAccountidCloseallPost202Response cloudStrategiesStartPost(body)

Start a strategy execution for account

Start a strategy execution for account

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.CloudAPIApi();
let body = new TradematicCloudApi.CloudStrategiesStartPostRequest(); // CloudStrategiesStartPostRequest | 
apiInstance.cloudStrategiesStartPost(body, (error, data, response) => {
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
 **body** | [**CloudStrategiesStartPostRequest**](CloudStrategiesStartPostRequest.md)|  | 

### Return type

[**CloudAccountsAccountidCloseallPost202Response**](CloudAccountsAccountidCloseallPost202Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudStrategiesStrategyidGet

> [CloudStrategy] cloudStrategiesStrategyidGet(strategyid)

Get active (executing) strategy by ID

Get active (executing) strategy by ID

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.CloudAPIApi();
let strategyid = 789; // Number | 
apiInstance.cloudStrategiesStrategyidGet(strategyid, (error, data, response) => {
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
 **strategyid** | **Number**|  | 

### Return type

[**[CloudStrategy]**](CloudStrategy.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudStrategiesStrategyidStopPost

> CloudAccountsAccountidCloseallPost202Response cloudStrategiesStrategyidStopPost(strategyid)

Stop a strategy execution by ID

Stop a strategy execution by ID

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.CloudAPIApi();
let strategyid = 789; // Number | 
apiInstance.cloudStrategiesStrategyidStopPost(strategyid, (error, data, response) => {
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
 **strategyid** | **Number**|  | 

### Return type

[**CloudAccountsAccountidCloseallPost202Response**](CloudAccountsAccountidCloseallPost202Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

