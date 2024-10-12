# GameSparksGameDetailsApi.PushNotificationTestApi

All URIs are relative to *http://config2.gamesparks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**testPushAmazonNotificationsUsingPOST**](PushNotificationTestApi.md#testPushAmazonNotificationsUsingPOST) | **POST** /restv2/game/{apiKey}/admin/pushNotifications/test/amazon | testPushAmazonNotifications
[**testPushAppleDevNotificationsUsingPOST**](PushNotificationTestApi.md#testPushAppleDevNotificationsUsingPOST) | **POST** /restv2/game/{apiKey}/admin/pushNotifications/test/apple/development | testPushAppleDevNotifications
[**testPushAppleProdNotificationsUsingPOST**](PushNotificationTestApi.md#testPushAppleProdNotificationsUsingPOST) | **POST** /restv2/game/{apiKey}/admin/pushNotifications/test/apple/production | testPushAppleProdNotifications
[**testPushGoogleNotificationsUsingPOST**](PushNotificationTestApi.md#testPushGoogleNotificationsUsingPOST) | **POST** /restv2/game/{apiKey}/admin/pushNotifications/test/google | testPushGoogleNotifications
[**testViberIntegrationNotificationsUsingPOST**](PushNotificationTestApi.md#testViberIntegrationNotificationsUsingPOST) | **POST** /restv2/game/{apiKey}/admin/pushNotifications/test/viber/integration | testViberIntegrationNotifications
[**testViberProductionNotificationsUsingPOST**](PushNotificationTestApi.md#testViberProductionNotificationsUsingPOST) | **POST** /restv2/game/{apiKey}/admin/pushNotifications/test/viber/production | testViberProductionNotifications
[**testWindows8NotificationsUsingPOST**](PushNotificationTestApi.md#testWindows8NotificationsUsingPOST) | **POST** /restv2/game/{apiKey}/admin/pushNotifications/test/microsoft/windows8 | testWindows8Notifications
[**testWindowsPhone8NotificationsUsingPOST**](PushNotificationTestApi.md#testWindowsPhone8NotificationsUsingPOST) | **POST** /restv2/game/{apiKey}/admin/pushNotifications/test/microsoft/windowsPhone8 | testWindowsPhone8Notifications



## testPushAmazonNotificationsUsingPOST

> PushNotificationTestSummaryListModel testPushAmazonNotificationsUsingPOST(apiKey, pushNotificationTestModel)

testPushAmazonNotifications

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.PushNotificationTestApi();
let apiKey = "apiKey_example"; // String | apiKey
let pushNotificationTestModel = new GameSparksGameDetailsApi.PushNotificationTestModel(); // PushNotificationTestModel | messageDetails
apiInstance.testPushAmazonNotificationsUsingPOST(apiKey, pushNotificationTestModel, (error, data, response) => {
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
 **apiKey** | **String**| apiKey | 
 **pushNotificationTestModel** | [**PushNotificationTestModel**](PushNotificationTestModel.md)| messageDetails | 

### Return type

[**PushNotificationTestSummaryListModel**](PushNotificationTestSummaryListModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## testPushAppleDevNotificationsUsingPOST

> PushNotificationTestSummaryListModel testPushAppleDevNotificationsUsingPOST(apiKey, pushNotificationTestModel)

testPushAppleDevNotifications

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.PushNotificationTestApi();
let apiKey = "apiKey_example"; // String | apiKey
let pushNotificationTestModel = new GameSparksGameDetailsApi.PushNotificationTestModel(); // PushNotificationTestModel | messageDetails
apiInstance.testPushAppleDevNotificationsUsingPOST(apiKey, pushNotificationTestModel, (error, data, response) => {
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
 **apiKey** | **String**| apiKey | 
 **pushNotificationTestModel** | [**PushNotificationTestModel**](PushNotificationTestModel.md)| messageDetails | 

### Return type

[**PushNotificationTestSummaryListModel**](PushNotificationTestSummaryListModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## testPushAppleProdNotificationsUsingPOST

> PushNotificationTestSummaryListModel testPushAppleProdNotificationsUsingPOST(apiKey, pushNotificationTestModel)

testPushAppleProdNotifications

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.PushNotificationTestApi();
let apiKey = "apiKey_example"; // String | apiKey
let pushNotificationTestModel = new GameSparksGameDetailsApi.PushNotificationTestModel(); // PushNotificationTestModel | messageDetails
apiInstance.testPushAppleProdNotificationsUsingPOST(apiKey, pushNotificationTestModel, (error, data, response) => {
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
 **apiKey** | **String**| apiKey | 
 **pushNotificationTestModel** | [**PushNotificationTestModel**](PushNotificationTestModel.md)| messageDetails | 

### Return type

[**PushNotificationTestSummaryListModel**](PushNotificationTestSummaryListModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## testPushGoogleNotificationsUsingPOST

> PushNotificationTestSummaryListModel testPushGoogleNotificationsUsingPOST(apiKey, pushNotificationTestModel)

testPushGoogleNotifications

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.PushNotificationTestApi();
let apiKey = "apiKey_example"; // String | apiKey
let pushNotificationTestModel = new GameSparksGameDetailsApi.PushNotificationTestModel(); // PushNotificationTestModel | messageDetails
apiInstance.testPushGoogleNotificationsUsingPOST(apiKey, pushNotificationTestModel, (error, data, response) => {
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
 **apiKey** | **String**| apiKey | 
 **pushNotificationTestModel** | [**PushNotificationTestModel**](PushNotificationTestModel.md)| messageDetails | 

### Return type

[**PushNotificationTestSummaryListModel**](PushNotificationTestSummaryListModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## testViberIntegrationNotificationsUsingPOST

> PushNotificationTestSummaryListModel testViberIntegrationNotificationsUsingPOST(apiKey, pushNotificationTestModel)

testViberIntegrationNotifications

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.PushNotificationTestApi();
let apiKey = "apiKey_example"; // String | apiKey
let pushNotificationTestModel = new GameSparksGameDetailsApi.PushNotificationTestModel(); // PushNotificationTestModel | messageDetails
apiInstance.testViberIntegrationNotificationsUsingPOST(apiKey, pushNotificationTestModel, (error, data, response) => {
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
 **apiKey** | **String**| apiKey | 
 **pushNotificationTestModel** | [**PushNotificationTestModel**](PushNotificationTestModel.md)| messageDetails | 

### Return type

[**PushNotificationTestSummaryListModel**](PushNotificationTestSummaryListModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## testViberProductionNotificationsUsingPOST

> PushNotificationTestSummaryListModel testViberProductionNotificationsUsingPOST(apiKey, pushNotificationTestModel)

testViberProductionNotifications

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.PushNotificationTestApi();
let apiKey = "apiKey_example"; // String | apiKey
let pushNotificationTestModel = new GameSparksGameDetailsApi.PushNotificationTestModel(); // PushNotificationTestModel | messageDetails
apiInstance.testViberProductionNotificationsUsingPOST(apiKey, pushNotificationTestModel, (error, data, response) => {
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
 **apiKey** | **String**| apiKey | 
 **pushNotificationTestModel** | [**PushNotificationTestModel**](PushNotificationTestModel.md)| messageDetails | 

### Return type

[**PushNotificationTestSummaryListModel**](PushNotificationTestSummaryListModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## testWindows8NotificationsUsingPOST

> PushNotificationTestSummaryListModel testWindows8NotificationsUsingPOST(apiKey, pushNotificationTestModel)

testWindows8Notifications

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.PushNotificationTestApi();
let apiKey = "apiKey_example"; // String | apiKey
let pushNotificationTestModel = new GameSparksGameDetailsApi.PushNotificationTestModel(); // PushNotificationTestModel | messageDetails
apiInstance.testWindows8NotificationsUsingPOST(apiKey, pushNotificationTestModel, (error, data, response) => {
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
 **apiKey** | **String**| apiKey | 
 **pushNotificationTestModel** | [**PushNotificationTestModel**](PushNotificationTestModel.md)| messageDetails | 

### Return type

[**PushNotificationTestSummaryListModel**](PushNotificationTestSummaryListModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## testWindowsPhone8NotificationsUsingPOST

> PushNotificationTestSummaryListModel testWindowsPhone8NotificationsUsingPOST(apiKey, pushNotificationTestModel)

testWindowsPhone8Notifications

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.PushNotificationTestApi();
let apiKey = "apiKey_example"; // String | apiKey
let pushNotificationTestModel = new GameSparksGameDetailsApi.PushNotificationTestModel(); // PushNotificationTestModel | messageDetails
apiInstance.testWindowsPhone8NotificationsUsingPOST(apiKey, pushNotificationTestModel, (error, data, response) => {
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
 **apiKey** | **String**| apiKey | 
 **pushNotificationTestModel** | [**PushNotificationTestModel**](PushNotificationTestModel.md)| messageDetails | 

### Return type

[**PushNotificationTestSummaryListModel**](PushNotificationTestSummaryListModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*

