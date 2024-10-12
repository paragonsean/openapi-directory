# PeerTube.MyNotificationsApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1UsersMeNotificationSettingsPut**](MyNotificationsApi.md#apiV1UsersMeNotificationSettingsPut) | **PUT** /api/v1/users/me/notification-settings | Update my notification settings
[**apiV1UsersMeNotificationsGet**](MyNotificationsApi.md#apiV1UsersMeNotificationsGet) | **GET** /api/v1/users/me/notifications | List my notifications
[**apiV1UsersMeNotificationsReadAllPost**](MyNotificationsApi.md#apiV1UsersMeNotificationsReadAllPost) | **POST** /api/v1/users/me/notifications/read-all | Mark all my notification as read
[**apiV1UsersMeNotificationsReadPost**](MyNotificationsApi.md#apiV1UsersMeNotificationsReadPost) | **POST** /api/v1/users/me/notifications/read | Mark notifications as read by their id



## apiV1UsersMeNotificationSettingsPut

> apiV1UsersMeNotificationSettingsPut(opts)

Update my notification settings

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.MyNotificationsApi();
let opts = {
  'apiV1UsersMeNotificationSettingsPutRequest': new PeerTube.ApiV1UsersMeNotificationSettingsPutRequest() // ApiV1UsersMeNotificationSettingsPutRequest | 
};
apiInstance.apiV1UsersMeNotificationSettingsPut(opts, (error, data, response) => {
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
 **apiV1UsersMeNotificationSettingsPutRequest** | [**ApiV1UsersMeNotificationSettingsPutRequest**](ApiV1UsersMeNotificationSettingsPutRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## apiV1UsersMeNotificationsGet

> NotificationListResponse apiV1UsersMeNotificationsGet(opts)

List my notifications

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.MyNotificationsApi();
let opts = {
  'unread': true, // Boolean | only list unread notifications
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "-createdAt" // String | Sort column
};
apiInstance.apiV1UsersMeNotificationsGet(opts, (error, data, response) => {
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
 **unread** | **Boolean**| only list unread notifications | [optional] 
 **start** | **Number**| Offset used to paginate results | [optional] 
 **count** | **Number**| Number of items to return | [optional] [default to 15]
 **sort** | **String**| Sort column | [optional] 

### Return type

[**NotificationListResponse**](NotificationListResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1UsersMeNotificationsReadAllPost

> apiV1UsersMeNotificationsReadAllPost()

Mark all my notification as read

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.MyNotificationsApi();
apiInstance.apiV1UsersMeNotificationsReadAllPost((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiV1UsersMeNotificationsReadPost

> apiV1UsersMeNotificationsReadPost(opts)

Mark notifications as read by their id

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.MyNotificationsApi();
let opts = {
  'apiV1UsersMeNotificationsReadPostRequest': new PeerTube.ApiV1UsersMeNotificationsReadPostRequest() // ApiV1UsersMeNotificationsReadPostRequest | 
};
apiInstance.apiV1UsersMeNotificationsReadPost(opts, (error, data, response) => {
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
 **apiV1UsersMeNotificationsReadPostRequest** | [**ApiV1UsersMeNotificationsReadPostRequest**](ApiV1UsersMeNotificationsReadPostRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

