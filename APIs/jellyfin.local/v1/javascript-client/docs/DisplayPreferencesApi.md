# JellyfinApi.DisplayPreferencesApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDisplayPreferences**](DisplayPreferencesApi.md#getDisplayPreferences) | **GET** /DisplayPreferences/{displayPreferencesId} | Get Display Preferences.
[**updateDisplayPreferences**](DisplayPreferencesApi.md#updateDisplayPreferences) | **POST** /DisplayPreferences/{displayPreferencesId} | Update Display Preferences.



## getDisplayPreferences

> DisplayPreferencesDto getDisplayPreferences(displayPreferencesId, userId, client)

Get Display Preferences.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.DisplayPreferencesApi();
let displayPreferencesId = "displayPreferencesId_example"; // String | Display preferences id.
let userId = "userId_example"; // String | User id.
let client = "client_example"; // String | Client.
apiInstance.getDisplayPreferences(displayPreferencesId, userId, client, (error, data, response) => {
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
 **displayPreferencesId** | **String**| Display preferences id. | 
 **userId** | **String**| User id. | 
 **client** | **String**| Client. | 

### Return type

[**DisplayPreferencesDto**](DisplayPreferencesDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## updateDisplayPreferences

> updateDisplayPreferences(displayPreferencesId, userId, client, displayPreferencesDto)

Update Display Preferences.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.DisplayPreferencesApi();
let displayPreferencesId = "displayPreferencesId_example"; // String | Display preferences id.
let userId = "userId_example"; // String | User Id.
let client = "client_example"; // String | Client.
let displayPreferencesDto = new JellyfinApi.DisplayPreferencesDto(); // DisplayPreferencesDto | New Display Preferences object.
apiInstance.updateDisplayPreferences(displayPreferencesId, userId, client, displayPreferencesDto, (error, data, response) => {
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
 **displayPreferencesId** | **String**| Display preferences id. | 
 **userId** | **String**| User Id. | 
 **client** | **String**| Client. | 
 **displayPreferencesDto** | [**DisplayPreferencesDto**](DisplayPreferencesDto.md)| New Display Preferences object. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: Not defined

