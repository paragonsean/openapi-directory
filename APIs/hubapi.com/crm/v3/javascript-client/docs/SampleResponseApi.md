# CrmCards.SampleResponseApi

All URIs are relative to *https://api.hubapi.com/crm/v3/extensions/cards*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCrmV3ExtensionsCardsSampleResponse**](SampleResponseApi.md#getCrmV3ExtensionsCardsSampleResponse) | **GET** /sample-response | Get sample card detail response



## getCrmV3ExtensionsCardsSampleResponse

> IntegratorCardPayloadResponse getCrmV3ExtensionsCardsSampleResponse()

Get sample card detail response

Returns an example card detail response. This is the payload with displayed details for a card that will be shown to a user. An app should send this in response to the data fetch request.

### Example

```javascript
import CrmCards from 'crm_cards';

let apiInstance = new CrmCards.SampleResponseApi();
apiInstance.getCrmV3ExtensionsCardsSampleResponse((error, data, response) => {
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

[**IntegratorCardPayloadResponse**](IntegratorCardPayloadResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*

