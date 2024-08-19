# Netatmo.WelcomeApi

All URIs are relative to *https://api.netatmo.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addwebhook**](WelcomeApi.md#addwebhook) | **GET** /addwebhook | 
[**dropwebhook**](WelcomeApi.md#dropwebhook) | **GET** /dropwebhook | 
[**getcamerapicture**](WelcomeApi.md#getcamerapicture) | **GET** /getcamerapicture | 
[**geteventsuntil**](WelcomeApi.md#geteventsuntil) | **GET** /geteventsuntil | 
[**gethomedata**](WelcomeApi.md#gethomedata) | **GET** /gethomedata | 
[**getlasteventof**](WelcomeApi.md#getlasteventof) | **GET** /getlasteventof | 
[**getnextevents**](WelcomeApi.md#getnextevents) | **GET** /getnextevents | 
[**setpersonsaway**](WelcomeApi.md#setpersonsaway) | **POST** /setpersonsaway | 
[**setpersonshome**](WelcomeApi.md#setpersonshome) | **POST** /setpersonshome | 



## addwebhook

> NAWelcomeWebhookResponse addwebhook(url, appType)



Links a callback url to a user. 

### Example

```javascript
import Netatmo from 'netatmo';
let defaultClient = Netatmo.ApiClient.instance;
// Configure OAuth2 access token for authorization: code_oauth
let code_oauth = defaultClient.authentications['code_oauth'];
code_oauth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: password_oauth
let password_oauth = defaultClient.authentications['password_oauth'];
password_oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Netatmo.WelcomeApi();
let url = "url_example"; // String | Your webhook callback url
let appType = "appType_example"; // String | Webhooks are only available for Welcome, enter app_camera.
apiInstance.addwebhook(url, appType, (error, data, response) => {
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
 **url** | **String**| Your webhook callback url | 
 **appType** | **String**| Webhooks are only available for Welcome, enter app_camera. | 

### Return type

[**NAWelcomeWebhookResponse**](NAWelcomeWebhookResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dropwebhook

> NAWelcomeWebhookResponse dropwebhook(appType)



Dissociates a webhook from a user. 

### Example

```javascript
import Netatmo from 'netatmo';
let defaultClient = Netatmo.ApiClient.instance;
// Configure OAuth2 access token for authorization: code_oauth
let code_oauth = defaultClient.authentications['code_oauth'];
code_oauth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: password_oauth
let password_oauth = defaultClient.authentications['password_oauth'];
password_oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Netatmo.WelcomeApi();
let appType = "appType_example"; // String | For Welcome, use app_camera
apiInstance.dropwebhook(appType, (error, data, response) => {
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
 **appType** | **String**| For Welcome, use app_camera | 

### Return type

[**NAWelcomeWebhookResponse**](NAWelcomeWebhookResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getcamerapicture

> Blob getcamerapicture(imageId, key)



Returns the snapshot associated to an event. 

### Example

```javascript
import Netatmo from 'netatmo';
let defaultClient = Netatmo.ApiClient.instance;
// Configure OAuth2 access token for authorization: code_oauth
let code_oauth = defaultClient.authentications['code_oauth'];
code_oauth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: password_oauth
let password_oauth = defaultClient.authentications['password_oauth'];
password_oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Netatmo.WelcomeApi();
let imageId = "imageId_example"; // String | id of the image (can be retrieved as 'id' in 'face' in Gethomedata, or as 'id' in 'snapshot' in Getnextevents, Getlasteventof and Geteventsuntil)
let key = "key_example"; // String | Security key to access snapshots.
apiInstance.getcamerapicture(imageId, key, (error, data, response) => {
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
 **imageId** | **String**| id of the image (can be retrieved as &#39;id&#39; in &#39;face&#39; in Gethomedata, or as &#39;id&#39; in &#39;snapshot&#39; in Getnextevents, Getlasteventof and Geteventsuntil) | 
 **key** | **String**| Security key to access snapshots. | 

### Return type

**Blob**

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## geteventsuntil

> NAWelcomeEventResponse geteventsuntil(homeId, eventId)



Returns the snapshot associated to an event. 

### Example

```javascript
import Netatmo from 'netatmo';
let defaultClient = Netatmo.ApiClient.instance;
// Configure OAuth2 access token for authorization: code_oauth
let code_oauth = defaultClient.authentications['code_oauth'];
code_oauth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: password_oauth
let password_oauth = defaultClient.authentications['password_oauth'];
password_oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Netatmo.WelcomeApi();
let homeId = "homeId_example"; // String | ID of the Home you're interested in
let eventId = "eventId_example"; // String | Your request will retrieve all the events until this one
apiInstance.geteventsuntil(homeId, eventId, (error, data, response) => {
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
 **homeId** | **String**| ID of the Home you&#39;re interested in | 
 **eventId** | **String**| Your request will retrieve all the events until this one | 

### Return type

[**NAWelcomeEventResponse**](NAWelcomeEventResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gethomedata

> NAWelcomeHomeDataResponse gethomedata(opts)



Returns information about users homes and cameras. 

### Example

```javascript
import Netatmo from 'netatmo';
let defaultClient = Netatmo.ApiClient.instance;
// Configure OAuth2 access token for authorization: code_oauth
let code_oauth = defaultClient.authentications['code_oauth'];
code_oauth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: password_oauth
let password_oauth = defaultClient.authentications['password_oauth'];
password_oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Netatmo.WelcomeApi();
let opts = {
  'homeId': "homeId_example", // String | Specify if you're looking for the events of a specific Home.
  'size': 56 // Number | Number of events to retrieve. Default is `30`.
};
apiInstance.gethomedata(opts, (error, data, response) => {
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
 **homeId** | **String**| Specify if you&#39;re looking for the events of a specific Home. | [optional] 
 **size** | **Number**| Number of events to retrieve. Default is &#x60;30&#x60;. | [optional] 

### Return type

[**NAWelcomeHomeDataResponse**](NAWelcomeHomeDataResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getlasteventof

> NAWelcomeEventResponse getlasteventof(homeId, personId, opts)



Returns most recent events. 

### Example

```javascript
import Netatmo from 'netatmo';
let defaultClient = Netatmo.ApiClient.instance;
// Configure OAuth2 access token for authorization: code_oauth
let code_oauth = defaultClient.authentications['code_oauth'];
code_oauth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: password_oauth
let password_oauth = defaultClient.authentications['password_oauth'];
password_oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Netatmo.WelcomeApi();
let homeId = "homeId_example"; // String | ID of the Home you're interested in
let personId = "personId_example"; // String | Your request will retrieve all events of the given home until the most recent event of the given person
let opts = {
  'offset': 56 // Number | Number of events to retrieve. Default is 30.
};
apiInstance.getlasteventof(homeId, personId, opts, (error, data, response) => {
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
 **homeId** | **String**| ID of the Home you&#39;re interested in | 
 **personId** | **String**| Your request will retrieve all events of the given home until the most recent event of the given person | 
 **offset** | **Number**| Number of events to retrieve. Default is 30. | [optional] 

### Return type

[**NAWelcomeEventResponse**](NAWelcomeEventResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getnextevents

> NAWelcomeEventResponse getnextevents(homeId, eventId, opts)



Returns previous events. 

### Example

```javascript
import Netatmo from 'netatmo';
let defaultClient = Netatmo.ApiClient.instance;
// Configure OAuth2 access token for authorization: code_oauth
let code_oauth = defaultClient.authentications['code_oauth'];
code_oauth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: password_oauth
let password_oauth = defaultClient.authentications['password_oauth'];
password_oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Netatmo.WelcomeApi();
let homeId = "homeId_example"; // String | ID of the Home you're interested in
let eventId = "eventId_example"; // String | Your request will retrieve events occured before this one
let opts = {
  'size': 56 // Number | Number of events to retrieve. Default is 30.
};
apiInstance.getnextevents(homeId, eventId, opts, (error, data, response) => {
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
 **homeId** | **String**| ID of the Home you&#39;re interested in | 
 **eventId** | **String**| Your request will retrieve events occured before this one | 
 **size** | **Number**| Number of events to retrieve. Default is 30. | [optional] 

### Return type

[**NAWelcomeEventResponse**](NAWelcomeEventResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setpersonsaway

> NAWelcomePersonsAwayResponse setpersonsaway(homeId, opts)



Sets a person as &#39;Away&#39; or the Home as &#39;Empty&#39;. The event will be added to the user’s timeline. 

### Example

```javascript
import Netatmo from 'netatmo';
let defaultClient = Netatmo.ApiClient.instance;
// Configure OAuth2 access token for authorization: code_oauth
let code_oauth = defaultClient.authentications['code_oauth'];
code_oauth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: password_oauth
let password_oauth = defaultClient.authentications['password_oauth'];
password_oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Netatmo.WelcomeApi();
let homeId = "homeId_example"; // String | ID of the Home you're interested in
let opts = {
  'personId': "personId_example" // String | If a person_id is specified, that person will be set as 'Away'. If no person_id is specified, the Home will be set as 'Empty'.
};
apiInstance.setpersonsaway(homeId, opts, (error, data, response) => {
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
 **homeId** | **String**| ID of the Home you&#39;re interested in | 
 **personId** | **String**| If a person_id is specified, that person will be set as &#39;Away&#39;. If no person_id is specified, the Home will be set as &#39;Empty&#39;. | [optional] 

### Return type

[**NAWelcomePersonsAwayResponse**](NAWelcomePersonsAwayResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setpersonshome

> NAWelcomePersonsHomeResponse setpersonshome(homeId, personIds)



Sets a person as &#39;At home&#39;. 

### Example

```javascript
import Netatmo from 'netatmo';
let defaultClient = Netatmo.ApiClient.instance;
// Configure OAuth2 access token for authorization: code_oauth
let code_oauth = defaultClient.authentications['code_oauth'];
code_oauth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: password_oauth
let password_oauth = defaultClient.authentications['password_oauth'];
password_oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Netatmo.WelcomeApi();
let homeId = "homeId_example"; // String | ID of the Home you're interested in
let personIds = "personIds_example"; // String | List of persons IDs
apiInstance.setpersonshome(homeId, personIds, (error, data, response) => {
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
 **homeId** | **String**| ID of the Home you&#39;re interested in | 
 **personIds** | **String**| List of persons IDs | 

### Return type

[**NAWelcomePersonsHomeResponse**](NAWelcomePersonsHomeResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

