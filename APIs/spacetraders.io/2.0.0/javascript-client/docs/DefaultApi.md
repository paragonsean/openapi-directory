# SpaceTradersApi.DefaultApi

All URIs are relative to *https://api.spacetraders.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**register**](DefaultApi.md#register) | **POST** /register | Register New Agent



## register

> Register201Response register(opts)

Register New Agent

Creates a new agent and ties it to a temporary Account.  The agent symbol is a 3-14 character string that will represent your agent. This symbol will prefix the symbol of every ship you own. Agent symbols will be cast to all uppercase characters.  A new agent will be granted an authorization token, a contract with their starting faction, a command ship with a jump drive, and one hundred thousand credits.  &gt; #### Keep your token safe and secure &gt; &gt; Save your token during the alpha phase. There is no way to regenerate this token without starting a new agent. In the future you will be able to generate and manage your tokens from the SpaceTraders website.  You can accept your contract using the &#x60;/my/contracts/{contractId}/accept&#x60; endpoint. You will want to navigate your command ship to a nearby asteroid field and execute the &#x60;/my/ships/{shipSymbol}/extract&#x60; endpoint to mine various types of ores and minerals.  Return to the contract destination and execute the &#x60;/my/ships/{shipSymbol}/deliver&#x60; endpoint to deposit goods into the contract.  When your contract is fulfilled, you can call &#x60;/my/contracts/{contractId}/fulfill&#x60; to retrieve payment.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.DefaultApi();
let opts = {
  'registerRequest': new SpaceTradersApi.RegisterRequest() // RegisterRequest | 
};
apiInstance.register(opts, (error, data, response) => {
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
 **registerRequest** | [**RegisterRequest**](RegisterRequest.md)|  | [optional] 

### Return type

[**Register201Response**](Register201Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

