# EveSwaggerInterface.UserInterfaceApi

All URIs are relative to *https://esi.evetech.net/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postUiAutopilotWaypoint**](UserInterfaceApi.md#postUiAutopilotWaypoint) | **POST** /ui/autopilot/waypoint/ | Set Autopilot Waypoint
[**postUiOpenwindowContract**](UserInterfaceApi.md#postUiOpenwindowContract) | **POST** /ui/openwindow/contract/ | Open Contract Window
[**postUiOpenwindowInformation**](UserInterfaceApi.md#postUiOpenwindowInformation) | **POST** /ui/openwindow/information/ | Open Information Window
[**postUiOpenwindowMarketdetails**](UserInterfaceApi.md#postUiOpenwindowMarketdetails) | **POST** /ui/openwindow/marketdetails/ | Open Market Details
[**postUiOpenwindowNewmail**](UserInterfaceApi.md#postUiOpenwindowNewmail) | **POST** /ui/openwindow/newmail/ | Open New Mail Window



## postUiAutopilotWaypoint

> postUiAutopilotWaypoint(addToBeginning, clearOtherWaypoints, destinationId, opts)

Set Autopilot Waypoint

Set a solar system as autopilot waypoint  --- Alternate route: &#x60;/dev/ui/autopilot/waypoint/&#x60;  Alternate route: &#x60;/v2/ui/autopilot/waypoint/&#x60; 

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';
let defaultClient = EveSwaggerInterface.ApiClient.instance;
// Configure OAuth2 access token for authorization: evesso
let evesso = defaultClient.authentications['evesso'];
evesso.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EveSwaggerInterface.UserInterfaceApi();
let addToBeginning = false; // Boolean | Whether this solar system should be added to the beginning of all waypoints
let clearOtherWaypoints = false; // Boolean | Whether clean other waypoints beforing adding this one
let destinationId = 789; // Number | The destination to travel to, can be solar system, station or structure's id
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'token': "token_example" // String | Access token to use if unable to set a header
};
apiInstance.postUiAutopilotWaypoint(addToBeginning, clearOtherWaypoints, destinationId, opts, (error, data, response) => {
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
 **addToBeginning** | **Boolean**| Whether this solar system should be added to the beginning of all waypoints | [default to false]
 **clearOtherWaypoints** | **Boolean**| Whether clean other waypoints beforing adding this one | [default to false]
 **destinationId** | **Number**| The destination to travel to, can be solar system, station or structure&#39;s id | 
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **token** | **String**| Access token to use if unable to set a header | [optional] 

### Return type

null (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postUiOpenwindowContract

> postUiOpenwindowContract(contractId, opts)

Open Contract Window

Open the contract window inside the client  --- Alternate route: &#x60;/dev/ui/openwindow/contract/&#x60;  Alternate route: &#x60;/legacy/ui/openwindow/contract/&#x60;  Alternate route: &#x60;/v1/ui/openwindow/contract/&#x60; 

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';
let defaultClient = EveSwaggerInterface.ApiClient.instance;
// Configure OAuth2 access token for authorization: evesso
let evesso = defaultClient.authentications['evesso'];
evesso.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EveSwaggerInterface.UserInterfaceApi();
let contractId = 56; // Number | The contract to open
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'token': "token_example" // String | Access token to use if unable to set a header
};
apiInstance.postUiOpenwindowContract(contractId, opts, (error, data, response) => {
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
 **contractId** | **Number**| The contract to open | 
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **token** | **String**| Access token to use if unable to set a header | [optional] 

### Return type

null (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postUiOpenwindowInformation

> postUiOpenwindowInformation(targetId, opts)

Open Information Window

Open the information window for a character, corporation or alliance inside the client  --- Alternate route: &#x60;/dev/ui/openwindow/information/&#x60;  Alternate route: &#x60;/legacy/ui/openwindow/information/&#x60;  Alternate route: &#x60;/v1/ui/openwindow/information/&#x60; 

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';
let defaultClient = EveSwaggerInterface.ApiClient.instance;
// Configure OAuth2 access token for authorization: evesso
let evesso = defaultClient.authentications['evesso'];
evesso.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EveSwaggerInterface.UserInterfaceApi();
let targetId = 56; // Number | The target to open
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'token': "token_example" // String | Access token to use if unable to set a header
};
apiInstance.postUiOpenwindowInformation(targetId, opts, (error, data, response) => {
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
 **targetId** | **Number**| The target to open | 
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **token** | **String**| Access token to use if unable to set a header | [optional] 

### Return type

null (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postUiOpenwindowMarketdetails

> postUiOpenwindowMarketdetails(typeId, opts)

Open Market Details

Open the market details window for a specific typeID inside the client  --- Alternate route: &#x60;/dev/ui/openwindow/marketdetails/&#x60;  Alternate route: &#x60;/legacy/ui/openwindow/marketdetails/&#x60;  Alternate route: &#x60;/v1/ui/openwindow/marketdetails/&#x60; 

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';
let defaultClient = EveSwaggerInterface.ApiClient.instance;
// Configure OAuth2 access token for authorization: evesso
let evesso = defaultClient.authentications['evesso'];
evesso.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EveSwaggerInterface.UserInterfaceApi();
let typeId = 56; // Number | The item type to open in market window
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'token': "token_example" // String | Access token to use if unable to set a header
};
apiInstance.postUiOpenwindowMarketdetails(typeId, opts, (error, data, response) => {
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
 **typeId** | **Number**| The item type to open in market window | 
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **token** | **String**| Access token to use if unable to set a header | [optional] 

### Return type

null (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postUiOpenwindowNewmail

> postUiOpenwindowNewmail(newMail, opts)

Open New Mail Window

Open the New Mail window, according to settings from the request if applicable  --- Alternate route: &#x60;/dev/ui/openwindow/newmail/&#x60;  Alternate route: &#x60;/legacy/ui/openwindow/newmail/&#x60;  Alternate route: &#x60;/v1/ui/openwindow/newmail/&#x60; 

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';
let defaultClient = EveSwaggerInterface.ApiClient.instance;
// Configure OAuth2 access token for authorization: evesso
let evesso = defaultClient.authentications['evesso'];
evesso.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EveSwaggerInterface.UserInterfaceApi();
let newMail = new EveSwaggerInterface.PostUiOpenwindowNewmailNewMail(); // PostUiOpenwindowNewmailNewMail | The details of mail to create
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'token': "token_example" // String | Access token to use if unable to set a header
};
apiInstance.postUiOpenwindowNewmail(newMail, opts, (error, data, response) => {
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
 **newMail** | [**PostUiOpenwindowNewmailNewMail**](PostUiOpenwindowNewmailNewMail.md)| The details of mail to create | 
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **token** | **String**| Access token to use if unable to set a header | [optional] 

### Return type

null (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

