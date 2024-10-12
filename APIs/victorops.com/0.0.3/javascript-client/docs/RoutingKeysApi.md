# VictorOps.RoutingKeysApi

All URIs are relative to *https://api.victorops.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiPublicV1OrgRoutingKeysGet**](RoutingKeysApi.md#apiPublicV1OrgRoutingKeysGet) | **GET** /api-public/v1/org/routing-keys | List routing keys with associated teams



## apiPublicV1OrgRoutingKeysGet

> ListRoutingKeysResponse apiPublicV1OrgRoutingKeysGet(xVOApiId, xVOApiKey)

List routing keys with associated teams

Retrieves a list of routing keys and associated teams. This API may be called a maximum of 60 times per minute.

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.RoutingKeysApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
apiInstance.apiPublicV1OrgRoutingKeysGet(xVOApiId, xVOApiKey, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 

### Return type

[**ListRoutingKeysResponse**](ListRoutingKeysResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

