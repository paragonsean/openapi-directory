# CustomerCreditApi.StoreConfigurationApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createorchangestoreconfiguration**](StoreConfigurationApi.md#createorchangestoreconfiguration) | **PUT** /api/creditcontrol/storeconfig | Create or change store configuration
[**retrievestoreconfiguration**](StoreConfigurationApi.md#retrievestoreconfiguration) | **GET** /api/creditcontrol/storeconfig | Retrieve store configuration



## createorchangestoreconfiguration

> Savestoreconfig1 createorchangestoreconfiguration(accept, contentType, createorchangestoreconfigurationRequest1)

Create or change store configuration

Create or change store configuration data.

### Example

```javascript
import CustomerCreditApi from 'customer_credit_api';
let defaultClient = CustomerCreditApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CustomerCreditApi.StoreConfigurationApi();
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let createorchangestoreconfigurationRequest1 = {"automaticCheckingAccountCreationEnabled":false,"dailyInterestRate":"number(percent 0.1=10%) (float)","defaultCreditValue":"number (decimal)","invoicePostponementLimit":"number (int)","maxPostponementDays":"number (int","maxPreAuthorizationGrowthRate":"number (percent 0.1=10%) (float)","myCreditsEnabled":false,"postponementEnabled":false,"taxRate":"number(percent 0.1=10%) (float)","toleranceEnabled":false}; // CreateorchangestoreconfigurationRequest1 | 
apiInstance.createorchangestoreconfiguration(accept, contentType, createorchangestoreconfigurationRequest1, (error, data, response) => {
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
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **createorchangestoreconfigurationRequest1** | [**CreateorchangestoreconfigurationRequest1**](CreateorchangestoreconfigurationRequest1.md)|  | 

### Return type

[**Savestoreconfig1**](Savestoreconfig1.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## retrievestoreconfiguration

> Storeconfig1 retrievestoreconfiguration(contentType, accept)

Retrieve store configuration

Get store configuration data.

### Example

```javascript
import CustomerCreditApi from 'customer_credit_api';
let defaultClient = CustomerCreditApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CustomerCreditApi.StoreConfigurationApi();
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
apiInstance.retrievestoreconfiguration(contentType, accept, (error, data, response) => {
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
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]

### Return type

[**Storeconfig1**](Storeconfig1.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8

