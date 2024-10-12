# WhatsAppBusinessApi.ApplicationApi

All URIs are relative to *http://whatsapp.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteMediaProviders**](ApplicationApi.md#deleteMediaProviders) | **DELETE** /settings/application/media/providers/{ProviderName} | Delete-Media-Providers
[**getApplicationSettings**](ApplicationApi.md#getApplicationSettings) | **GET** /settings/application | Get-Application-Settings
[**getMediaProviders**](ApplicationApi.md#getMediaProviders) | **GET** /settings/application/media/providers | Get-Media-Providers
[**resetApplicationSettings**](ApplicationApi.md#resetApplicationSettings) | **DELETE** /settings/application | Reset-Application-Settings
[**setShards**](ApplicationApi.md#setShards) | **POST** /account/shards | Set-Shards
[**updateApplicationSettings**](ApplicationApi.md#updateApplicationSettings) | **PATCH** /settings/application | Update-Application-Settings
[**updateMediaProviders**](ApplicationApi.md#updateMediaProviders) | **POST** /settings/application/media/providers | Update-Media-Providers



## deleteMediaProviders

> deleteMediaProviders(providerName)

Delete-Media-Providers

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.ApplicationApi();
let providerName = "providerName_example"; // String | Provider Name
apiInstance.deleteMediaProviders(providerName, (error, data, response) => {
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
 **providerName** | **String**| Provider Name | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getApplicationSettings

> ApplicationSettings getApplicationSettings()

Get-Application-Settings

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.ApplicationApi();
apiInstance.getApplicationSettings((error, data, response) => {
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

[**ApplicationSettings**](ApplicationSettings.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMediaProviders

> GetMediaProvidersResponse getMediaProviders()

Get-Media-Providers

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.ApplicationApi();
apiInstance.getMediaProviders((error, data, response) => {
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

[**GetMediaProvidersResponse**](GetMediaProvidersResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resetApplicationSettings

> resetApplicationSettings()

Reset-Application-Settings

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.ApplicationApi();
apiInstance.resetApplicationSettings((error, data, response) => {
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

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## setShards

> setShards(setShardsRequestBody)

Set-Shards

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.ApplicationApi();
let setShardsRequestBody = {"cc":"<Country Code>","phone_number":"<Phone Number>","pin":"<Two-Step PIN>","shards":32}; // SetShardsRequestBody | 
apiInstance.setShards(setShardsRequestBody, (error, data, response) => {
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
 **setShardsRequestBody** | [**SetShardsRequestBody**](SetShardsRequestBody.md)|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateApplicationSettings

> Response updateApplicationSettings(applicationSettings)

Update-Application-Settings

If a field is not present in the request, no change is made to that setting. For example, if on_call_pager is not sent with the request, the existing configuration for on_call_pager is unchanged.

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.ApplicationApi();
let applicationSettings = {"webhooks":{"url":"<Webhook URL, https>"}}; // ApplicationSettings | 
apiInstance.updateApplicationSettings(applicationSettings, (error, data, response) => {
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
 **applicationSettings** | [**ApplicationSettings**](ApplicationSettings.md)|  | 

### Return type

[**Response**](Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateMediaProviders

> updateMediaProviders(mediaProvider)

Update-Media-Providers

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.ApplicationApi();
let mediaProvider = [{"config":{"bearer":"<Bearer Auth Token>"},"name":"<Provider Name>","type":"www"}]; // [MediaProvider] | 
apiInstance.updateMediaProviders(mediaProvider, (error, data, response) => {
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
 **mediaProvider** | [**[MediaProvider]**](MediaProvider.md)|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

