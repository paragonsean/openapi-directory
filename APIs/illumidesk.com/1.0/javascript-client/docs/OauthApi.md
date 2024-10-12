# IllumiDesk.OauthApi

All URIs are relative to *https://api.illumidesk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauthApplicationCreate**](OauthApi.md#oauthApplicationCreate) | **POST** /v1/{namespace}/oauth/applications/ | Create a new OAuth2 application
[**oauthApplicationDelete**](OauthApi.md#oauthApplicationDelete) | **DELETE** /v1/{namespace}/oauth/applications/{application}/ | Delete an application by id
[**oauthApplicationRead**](OauthApi.md#oauthApplicationRead) | **GET** /v1/{namespace}/oauth/applications/{application}/ | Get an application by id
[**oauthApplicationReplace**](OauthApi.md#oauthApplicationReplace) | **PUT** /v1/{namespace}/oauth/applications/{application}/ | Replace an application by id
[**oauthApplicationUpdate**](OauthApi.md#oauthApplicationUpdate) | **PATCH** /v1/{namespace}/oauth/applications/{application}/ | Update an application by id
[**oauthApplicationsList**](OauthApi.md#oauthApplicationsList) | **GET** /v1/{namespace}/oauth/applications/ | Retrieve oauth applications



## oauthApplicationCreate

> Application oauthApplicationCreate(namespace, opts)

Create a new OAuth2 application

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.OauthApi();
let namespace = "namespace_example"; // String | User or team name.
let opts = {
  'applicationData': new IllumiDesk.ApplicationData() // ApplicationData | 
};
apiInstance.oauthApplicationCreate(namespace, opts, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **applicationData** | [**ApplicationData**](ApplicationData.md)|  | [optional] 

### Return type

[**Application**](Application.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## oauthApplicationDelete

> oauthApplicationDelete(namespace, application)

Delete an application by id

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.OauthApi();
let namespace = "namespace_example"; // String | User or team name.
let application = "application_example"; // String | Application unique identifier expressed as UUID or name.
apiInstance.oauthApplicationDelete(namespace, application, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **application** | **String**| Application unique identifier expressed as UUID or name. | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## oauthApplicationRead

> Application oauthApplicationRead(namespace, application)

Get an application by id

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.OauthApi();
let namespace = "namespace_example"; // String | User or team name.
let application = "application_example"; // String | Application unique identifier expressed as UUID or name.
apiInstance.oauthApplicationRead(namespace, application, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **application** | **String**| Application unique identifier expressed as UUID or name. | 

### Return type

[**Application**](Application.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## oauthApplicationReplace

> Application oauthApplicationReplace(namespace, application, opts)

Replace an application by id

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.OauthApi();
let namespace = "namespace_example"; // String | User or team name.
let application = "application_example"; // String | Application unique identifier expressed as UUID or name.
let opts = {
  'oauthApplicationData': new IllumiDesk.ApplicationData() // ApplicationData | 
};
apiInstance.oauthApplicationReplace(namespace, application, opts, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **application** | **String**| Application unique identifier expressed as UUID or name. | 
 **oauthApplicationData** | [**ApplicationData**](ApplicationData.md)|  | [optional] 

### Return type

[**Application**](Application.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## oauthApplicationUpdate

> Application oauthApplicationUpdate(namespace, application, opts)

Update an application by id

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.OauthApi();
let namespace = "namespace_example"; // String | User or team name.
let application = "application_example"; // String | Application unique identifier expressed as UUID or name.
let opts = {
  'applicationData': new IllumiDesk.ApplicationData() // ApplicationData | 
};
apiInstance.oauthApplicationUpdate(namespace, application, opts, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **application** | **String**| Application unique identifier expressed as UUID or name. | 
 **applicationData** | [**ApplicationData**](ApplicationData.md)|  | [optional] 

### Return type

[**Application**](Application.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## oauthApplicationsList

> [Application] oauthApplicationsList(namespace, opts)

Retrieve oauth applications

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.OauthApi();
let namespace = "namespace_example"; // String | User or team name.
let opts = {
  'limit': "limit_example", // String | Set limit when retrieving items.
  'offset': "offset_example", // String | Offset when retrieving items.
  'ordering': "ordering_example" // String | Set order when retrieving items.
};
apiInstance.oauthApplicationsList(namespace, opts, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **limit** | **String**| Set limit when retrieving items. | [optional] 
 **offset** | **String**| Offset when retrieving items. | [optional] 
 **ordering** | **String**| Set order when retrieving items. | [optional] 

### Return type

[**[Application]**](Application.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html

