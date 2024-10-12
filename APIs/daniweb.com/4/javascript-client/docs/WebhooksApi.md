# DaniWebConnectApi.WebhooksApi

All URIs are relative to *https://www.daniweb.com/connect/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhooksGet**](WebhooksApi.md#webhooksGet) | **GET** /webhooks | 
[**webhooksIDDelete**](WebhooksApi.md#webhooksIDDelete) | **DELETE** /webhooks/{ID} | 
[**webhooksPost**](WebhooksApi.md#webhooksPost) | **POST** /webhooks | 



## webhooksGet

> EndpointGetWebhooks webhooksGet()



Fetch a listing of all webhooks owned by the current user/bubble combination.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.WebhooksApi();
apiInstance.webhooksGet((error, data, response) => {
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

[**EndpointGetWebhooks**](EndpointGetWebhooks.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webhooksIDDelete

> EndpointDeleteWebhooksID webhooksIDDelete(ID)



Delete a webhook that was previously registered by the current user/bubble combination.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.WebhooksApi();
let ID = 56; // Number | 
apiInstance.webhooksIDDelete(ID, (error, data, response) => {
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
 **ID** | **Number**|  | 

### Return type

[**EndpointDeleteWebhooksID**](EndpointDeleteWebhooksID.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webhooksPost

> EndpointPostWebhooks webhooksPost(event, name, uri, opts)



Register a new webhook for the current user/bubble combination. Specify an object_id to only be notified on an event related to that specific Conversation ID, Group ID, or User ID. Your access token must have access to the user being tracked, user you are in the conversation with, or user who created the group. You must be connected with a user in order to keep track of their online status. Alternatively, do not specify an object_id to be notified on all events that are related to conversations you&#39;re in, groups you&#39;re a member of, or users you are in conversations with. You may only have one webhook for each object_id/event. The webhook URI must reside on your own server. Webhooks do not expire when the access token used to create them expires. However, they will temporarily cease to function if the user who created them deauthorizes access to the application (effectively no longer existing within the bubble), unless/until the user reauthorizes the application using OAuth.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.WebhooksApi();
let event = "event_example"; // String | 
let name = "name_example"; // String | 
let uri = "uri_example"; // String | 
let opts = {
  'bubbled': false, // Boolean | 
  'objectId': 56 // Number | 
};
apiInstance.webhooksPost(event, name, uri, opts, (error, data, response) => {
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
 **event** | **String**|  | 
 **name** | **String**|  | 
 **uri** | **String**|  | 
 **bubbled** | **Boolean**|  | [optional] [default to false]
 **objectId** | **Number**|  | [optional] 

### Return type

[**EndpointPostWebhooks**](EndpointPostWebhooks.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

