# ConversationApi.LegApi

All URIs are relative to *https://api.nexmo.com/v0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteLeg**](LegApi.md#deleteLeg) | **DELETE** /legs/{leg_id} | Delete a leg
[**listLegs**](LegApi.md#listLegs) | **GET** /legs | List legs



## deleteLeg

> Object deleteLeg(legId)

Delete a leg

### Example

```javascript
import ConversationApi from 'conversation_api';
let defaultClient = ConversationApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ConversationApi.LegApi();
let legId = "legId_example"; // String | Leg ID
apiInstance.deleteLeg(legId, (error, data, response) => {
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
 **legId** | **String**| Leg ID | 

### Return type

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listLegs

> ListLegs200Response listLegs()

List legs

### Example

```javascript
import ConversationApi from 'conversation_api';
let defaultClient = ConversationApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ConversationApi.LegApi();
apiInstance.listLegs((error, data, response) => {
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

[**ListLegs200Response**](ListLegs200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

