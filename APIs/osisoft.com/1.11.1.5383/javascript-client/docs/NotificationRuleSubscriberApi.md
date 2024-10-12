# PiWebApi2018Sp1SwaggerSpec.NotificationRuleSubscriberApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notificationRuleSubscriberDelete**](NotificationRuleSubscriberApi.md#notificationRuleSubscriberDelete) | **DELETE** /notificationrulesubscribers/{webId} | Delete a notification rule subscriber.
[**notificationRuleSubscriberGet**](NotificationRuleSubscriberApi.md#notificationRuleSubscriberGet) | **GET** /notificationrulesubscribers/{webId} | Retrieve a notification rule subscriber.
[**notificationRuleSubscriberGetByPath**](NotificationRuleSubscriberApi.md#notificationRuleSubscriberGetByPath) | **GET** /notificationrulesubscribers | Retrieve a notification rule subscriber by path.
[**notificationRuleSubscriberGetNotificationRuleSubscribers**](NotificationRuleSubscriberApi.md#notificationRuleSubscriberGetNotificationRuleSubscribers) | **GET** /notificationrulesubscribers/{webId}/notificationrulesubscribers | Retrieve notification rule subscriber subscribers.
[**notificationRuleSubscriberUpdate**](NotificationRuleSubscriberApi.md#notificationRuleSubscriberUpdate) | **PATCH** /notificationrulesubscribers/{webId} | Update a notification rule subscriber.



## notificationRuleSubscriberDelete

> notificationRuleSubscriberDelete(webId)

Delete a notification rule subscriber.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.NotificationRuleSubscriberApi();
let webId = "webId_example"; // String | The ID of the notification rule subscriber.
apiInstance.notificationRuleSubscriberDelete(webId, (error, data, response) => {
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
 **webId** | **String**| The ID of the notification rule subscriber. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## notificationRuleSubscriberGet

> NotificationRuleSubscriber notificationRuleSubscriberGet(webId, opts)

Retrieve a notification rule subscriber.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.NotificationRuleSubscriberApi();
let webId = "webId_example"; // String | The ID of the resource to use as the root of the search.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.notificationRuleSubscriberGet(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the resource to use as the root of the search. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**NotificationRuleSubscriber**](NotificationRuleSubscriber.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## notificationRuleSubscriberGetByPath

> NotificationRuleSubscriber notificationRuleSubscriberGetByPath(path, opts)

Retrieve a notification rule subscriber by path.

This method returns a Notification Rule Subscriber based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.NotificationRuleSubscriberApi();
let path = "path_example"; // String | The path to the notification rule subscriber.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.notificationRuleSubscriberGetByPath(path, opts, (error, data, response) => {
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
 **path** | **String**| The path to the notification rule subscriber. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**NotificationRuleSubscriber**](NotificationRuleSubscriber.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## notificationRuleSubscriberGetNotificationRuleSubscribers

> ItemsNotificationRuleSubscriber notificationRuleSubscriberGetNotificationRuleSubscribers(webId, opts)

Retrieve notification rule subscriber subscribers.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.NotificationRuleSubscriberApi();
let webId = "webId_example"; // String | The ID of the resource to use as the root of the search.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.notificationRuleSubscriberGetNotificationRuleSubscribers(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the resource to use as the root of the search. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsNotificationRuleSubscriber**](ItemsNotificationRuleSubscriber.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## notificationRuleSubscriberUpdate

> notificationRuleSubscriberUpdate(webId, notificationRuleSubscriber)

Update a notification rule subscriber.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.NotificationRuleSubscriberApi();
let webId = "webId_example"; // String | The ID of the notification rule subscriber.
let notificationRuleSubscriber = new PiWebApi2018Sp1SwaggerSpec.NotificationRuleSubscriber(); // NotificationRuleSubscriber | A partial notification rule subscriber containing the desired changes.
apiInstance.notificationRuleSubscriberUpdate(webId, notificationRuleSubscriber, (error, data, response) => {
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
 **webId** | **String**| The ID of the notification rule subscriber. | 
 **notificationRuleSubscriber** | [**NotificationRuleSubscriber**](NotificationRuleSubscriber.md)| A partial notification rule subscriber containing the desired changes. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined

