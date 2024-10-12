# TradematicCloudApi.BuilderAPIApi

All URIs are relative to *https://api.tradematic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**builderRulesGet**](BuilderAPIApi.md#builderRulesGet) | **GET** /builder/rules | Get strategy builder rules list
[**builderRulesRuleidGet**](BuilderAPIApi.md#builderRulesRuleidGet) | **GET** /builder/rules/{ruleid} | Get strategy builder rules by ID



## builderRulesGet

> [Rule] builderRulesGet()

Get strategy builder rules list

Get strategy builder rules list

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.BuilderAPIApi();
apiInstance.builderRulesGet((error, data, response) => {
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

[**[Rule]**](Rule.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## builderRulesRuleidGet

> [Rule] builderRulesRuleidGet(ruleid)

Get strategy builder rules by ID

Get strategy builder rules by ID

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.BuilderAPIApi();
let ruleid = 789; // Number | 
apiInstance.builderRulesRuleidGet(ruleid, (error, data, response) => {
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
 **ruleid** | **Number**|  | 

### Return type

[**[Rule]**](Rule.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

