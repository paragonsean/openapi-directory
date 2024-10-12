# LogisticsApi.SLAApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculateSLA**](SLAApi.md#calculateSLA) | **POST** /api/logistics/pvt/shipping/calculate | Calculate SLA



## calculateSLA

> [[CalculateSLA200ResponseInnerInner]] calculateSLA(contentType, accept, calculateSLARequest1)

Calculate SLA

Endpoint used by the checkout to calculate the Service Level Agreement (SLA), a contract between the store and shoppers on the order&#39;s fulfillment conditions, such as the shipping estimated date.     The calculation of the estimated date considers the [shipping policy](https://help.vtex.com/en/tutorial/shipping-policy--tutorials_140) and [loading dock](https://help.vtex.com/en/tutorial/loading-dock--5DY8xHEjOLYDVL41Urd5qj) related to the order.

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

let apiInstance = new LogisticsApi.SLAApi();
let contentType = "'application/json; charset=utf-8'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let calculateSLARequest1 = [{"items":[{"additionalHandlingTime":"00:00:00","dimension":{"height":5,"length":17,"weight":150,"width":17},"groupItemId":null,"id":"1","kitItem":[{"additionalHandlingTime":"00:00:00","dimension":{"height":5,"length":17,"weight":150,"width":17},"groupItemId":null,"id":"2000042","kitItem":[],"price":0,"quantity":1},{"additionalHandlingTime":"00:00:00","dimension":{"height":5,"length":17,"weight":150,"width":17},"groupItemId":null,"id":"2390059","kitItem":[],"price":0,"quantity":1}],"price":0,"quantity":1}],"location":{"country":"BRA","point":[-43.32475950000003,-22.9999575],"zipCode":"22780084"},"salesChannel":"1"}]; // [CalculateSLARequest1] | 
apiInstance.calculateSLA(contentType, accept, calculateSLARequest1, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json; charset&#x3D;utf-8&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **calculateSLARequest1** | [**[CalculateSLARequest1]**](CalculateSLARequest1.md)|  | 

### Return type

**[[CalculateSLA200ResponseInnerInner]]**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json; charset=utf-8
- **Accept**: application/json; charset=utf-8

