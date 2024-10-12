# SpaceTradersApi.FactionsApi

All URIs are relative to *https://api.spacetraders.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getFaction**](FactionsApi.md#getFaction) | **GET** /factions/{factionSymbol} | Get Faction
[**getFactions**](FactionsApi.md#getFactions) | **GET** /factions | List Factions



## getFaction

> GetFaction200Response getFaction(factionSymbol)

Get Faction

View the details of a faction.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.FactionsApi();
let factionSymbol = "'CGR'"; // String | The faction symbol
apiInstance.getFaction(factionSymbol, (error, data, response) => {
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
 **factionSymbol** | **String**| The faction symbol | [default to &#39;CGR&#39;]

### Return type

[**GetFaction200Response**](GetFaction200Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFactions

> GetFactions200Response getFactions(opts)

List Factions

List all discovered factions in the game.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.FactionsApi();
let opts = {
  'page': 56, // Number | What entry offset to request
  'limit': 56 // Number | How many entries to return per page
};
apiInstance.getFactions(opts, (error, data, response) => {
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

[**GetFactions200Response**](GetFactions200Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

