# LogisticsApi.FreightValuesApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createUpdateFreightValues**](FreightValuesApi.md#createUpdateFreightValues) | **POST** /api/logistics/pvt/configuration/freights/{carrierId}/values/update | Create/update freight values
[**freightValues**](FreightValuesApi.md#freightValues) | **GET** /api/logistics/pvt/configuration/freights/{carrierId}/{cep}/values | List freight values



## createUpdateFreightValues

> createUpdateFreightValues(contentType, accept, carrierId, createUpdateFreightValuesRequest)

Create/update freight values

Creates or updates the freight values of your store&#39;s carriers. Learn more in [Shipping rate template](https://help.vtex.com/en/tutorial/planilha-de-frete--tutorials_127#).

### Example

```javascript
import LogisticsApi from 'logistics_api';
let defaultClient = LogisticsApi.ApiClient.instance;
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

let apiInstance = new LogisticsApi.FreightValuesApi();
let contentType = "'application/json; charset=utf-8'"; // String | Type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let carrierId = "carrier123"; // String | 
let createUpdateFreightValuesRequest = [new LogisticsApi.CreateUpdateFreightValuesRequest()]; // [CreateUpdateFreightValuesRequest] | 
apiInstance.createUpdateFreightValues(contentType, accept, carrierId, createUpdateFreightValuesRequest, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json; charset&#x3D;utf-8&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]
 **carrierId** | **String**|  | 
 **createUpdateFreightValuesRequest** | [**[CreateUpdateFreightValuesRequest]**](CreateUpdateFreightValuesRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json; charset=utf-8
- **Accept**: Not defined


## freightValues

> [FreightValues200ResponseInner] freightValues(contentType, accept, carrierId, cep)

List freight values

Lists freight values apointed to your store&#39;s carriers, searching by carrier ID and postal code (&#x60;cep&#x60;).

### Example

```javascript
import LogisticsApi from 'logistics_api';
let defaultClient = LogisticsApi.ApiClient.instance;
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

let apiInstance = new LogisticsApi.FreightValuesApi();
let contentType = "'application/json; charset=utf-8'"; // String | Type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let carrierId = "carrier-123"; // String | Carrier ID
let cep = "12345000"; // String | Postal code.
apiInstance.freightValues(contentType, accept, carrierId, cep, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json; charset&#x3D;utf-8&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]
 **carrierId** | **String**| Carrier ID | 
 **cep** | **String**| Postal code. | 

### Return type

[**[FreightValues200ResponseInner]**](FreightValues200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8

