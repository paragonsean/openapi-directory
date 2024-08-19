# EDrvApi.CommandsApi

All URIs are relative to *http://api.edrv.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelreservation**](CommandsApi.md#cancelreservation) | **POST** /v1/commands/cancelreservation | 
[**getCommands**](CommandsApi.md#getCommands) | **GET** /v1/commands | 
[**getVariables**](CommandsApi.md#getVariables) | **GET** /v1/commands/{id}/variables | 
[**patchChargeStationVariable**](CommandsApi.md#patchChargeStationVariable) | **PATCH** /v1/commands/{id}/variables | 
[**remotestart**](CommandsApi.md#remotestart) | **POST** /v1/commands/remotestart | 
[**remotestop**](CommandsApi.md#remotestop) | **POST** /v1/commands/remotestop | 
[**reserve**](CommandsApi.md#reserve) | **POST** /v1/commands/reserve | 
[**reset**](CommandsApi.md#reset) | **POST** /v1/commands/reset | 
[**unlockconnector**](CommandsApi.md#unlockconnector) | **POST** /v1/commands/unlockconnector | 



## cancelreservation

> PatchChargeStation200Response cancelreservation(cancelreservationRequest)



Use to request a delete an existing reservation. The request will wait for the charge station to process the command. It will timeout after 60 seconds.

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.CommandsApi();
let cancelreservationRequest = new EDrvApi.CancelreservationRequest(); // CancelreservationRequest | 
apiInstance.cancelreservation(cancelreservationRequest, (error, data, response) => {
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
 **cancelreservationRequest** | [**CancelreservationRequest**](CancelreservationRequest.md)|  | 

### Return type

[**PatchChargeStation200Response**](PatchChargeStation200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getCommands

> getCommands(opts)



Get Commands data

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.CommandsApi();
let opts = {
  'paginateLimit': 20, // Number | Number of results per page
  'paginatePage': "paginatePage_example", // String | The queried page index
  'paginateEnabled': true, // Boolean | Enable pagination
  'sortBy': "'createdAt'", // String | Sort data by this key
  'sortOrder': "'desc'", // String | asc to sort ascending (default is desc - descending)
  'createdAtGte': new Date("2013-10-20T19:20:30+01:00"), // Date | Date as ISO String
  'createdAtLte': new Date("2013-10-20T19:20:30+01:00"), // Date | Date as ISO String
  'updatedAtGte': new Date("2013-10-20T19:20:30+01:00"), // Date | Date as ISO String
  'updatedAtLte': new Date("2013-10-20T19:20:30+01:00"), // Date | Date as ISO String
  'includeChargestation': true, // Boolean | Populate chargestation
  'includeDriver': true, // Boolean | Populate driver
  'includeTransaction': true, // Boolean | Populate transaction
  'includeOrganization': true // Boolean | Populate organization
};
apiInstance.getCommands(opts, (error, data, response) => {
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
 **paginateLimit** | **Number**| Number of results per page | [optional] [default to 20]
 **paginatePage** | **String**| The queried page index | [optional] 
 **paginateEnabled** | **Boolean**| Enable pagination | [optional] [default to true]
 **sortBy** | **String**| Sort data by this key | [optional] [default to &#39;createdAt&#39;]
 **sortOrder** | **String**| asc to sort ascending (default is desc - descending) | [optional] [default to &#39;desc&#39;]
 **createdAtGte** | **Date**| Date as ISO String | [optional] 
 **createdAtLte** | **Date**| Date as ISO String | [optional] 
 **updatedAtGte** | **Date**| Date as ISO String | [optional] 
 **updatedAtLte** | **Date**| Date as ISO String | [optional] 
 **includeChargestation** | **Boolean**| Populate chargestation | [optional] 
 **includeDriver** | **Boolean**| Populate driver | [optional] 
 **includeTransaction** | **Boolean**| Populate transaction | [optional] 
 **includeOrganization** | **Boolean**| Populate organization | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getVariables

> getVariables(id)



Get a charge station&#39;s config variables

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.CommandsApi();
let id = "id_example"; // String | The chargestation id
apiInstance.getVariables(id, (error, data, response) => {
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
 **id** | **String**| The chargestation id | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## patchChargeStationVariable

> PatchChargeStation200Response patchChargeStationVariable(id, patchChargeStationVariableRequest)



Update config variables for a chargestation

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.CommandsApi();
let id = "id_example"; // String | ID of charge station
let patchChargeStationVariableRequest = new EDrvApi.PatchChargeStationVariableRequest(); // PatchChargeStationVariableRequest | Charge Station Variable to set
apiInstance.patchChargeStationVariable(id, patchChargeStationVariableRequest, (error, data, response) => {
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
 **id** | **String**| ID of charge station | 
 **patchChargeStationVariableRequest** | [**PatchChargeStationVariableRequest**](PatchChargeStationVariableRequest.md)| Charge Station Variable to set | 

### Return type

[**PatchChargeStation200Response**](PatchChargeStation200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## remotestart

> Setchargingschedule201Response remotestart(remotestartRequest)



Use to request a remote start command. The request will wait for the charge station to process the command. It will timeout after 60 seconds.

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.CommandsApi();
let remotestartRequest = new EDrvApi.RemotestartRequest(); // RemotestartRequest | 
apiInstance.remotestart(remotestartRequest, (error, data, response) => {
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
 **remotestartRequest** | [**RemotestartRequest**](RemotestartRequest.md)|  | 

### Return type

[**Setchargingschedule201Response**](Setchargingschedule201Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## remotestop

> remotestop(remotestopRequest)



Use to request a remote stop command. The request will wait for the charge station to process the command. It will timeout after 60 seconds.

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.CommandsApi();
let remotestopRequest = new EDrvApi.RemotestopRequest(); // RemotestopRequest | Remote stop transaction info here.
apiInstance.remotestop(remotestopRequest, (error, data, response) => {
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
 **remotestopRequest** | [**RemotestopRequest**](RemotestopRequest.md)| Remote stop transaction info here. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## reserve

> Setchargingschedule201Response reserve(reserveRequest)



Use to request a reserve command. The request will wait for the charge station to process the command. It will timeout after 60 seconds.

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.CommandsApi();
let reserveRequest = new EDrvApi.ReserveRequest(); // ReserveRequest | 
apiInstance.reserve(reserveRequest, (error, data, response) => {
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
 **reserveRequest** | [**ReserveRequest**](ReserveRequest.md)|  | 

### Return type

[**Setchargingschedule201Response**](Setchargingschedule201Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## reset

> PatchChargeStation200Response reset(resetRequest)



Use to request a reset command. The request will wait for the charge station to process the command. It will timeout after 60 seconds.

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.CommandsApi();
let resetRequest = new EDrvApi.ResetRequest(); // ResetRequest | 
apiInstance.reset(resetRequest, (error, data, response) => {
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
 **resetRequest** | [**ResetRequest**](ResetRequest.md)|  | 

### Return type

[**PatchChargeStation200Response**](PatchChargeStation200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## unlockconnector

> Setchargingschedule201Response unlockconnector(unlockconnectorRequest)



Use to request an unlock command for a connector. The request will wait for the charge station to process the command. It will timeout after 60 seconds.

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.CommandsApi();
let unlockconnectorRequest = new EDrvApi.UnlockconnectorRequest(); // UnlockconnectorRequest | 
apiInstance.unlockconnector(unlockconnectorRequest, (error, data, response) => {
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
 **unlockconnectorRequest** | [**UnlockconnectorRequest**](UnlockconnectorRequest.md)|  | 

### Return type

[**Setchargingschedule201Response**](Setchargingschedule201Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

