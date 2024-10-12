# VestorlyApi.NewsletterSettingsApi

All URIs are relative to *https://staging.vestorly.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**findNewsletterSettings**](NewsletterSettingsApi.md#findNewsletterSettings) | **GET** /newsletter_settings | 
[**findNewsletterSettingsByID**](NewsletterSettingsApi.md#findNewsletterSettingsByID) | **GET** /newsletter_settings/{id} | 
[**updateNewsletterSettingsByID**](NewsletterSettingsApi.md#updateNewsletterSettingsByID) | **PUT** /newsletter_settings/{id} | 



## findNewsletterSettings

> NewsletterSettings findNewsletterSettings(vestorlyAuth, opts)



Returns all newsletter settings

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.NewsletterSettingsApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.findNewsletterSettings(vestorlyAuth, opts, (error, data, response) => {
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
 **vestorlyAuth** | **String**| Vestorly Auth Token | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**NewsletterSettings**](NewsletterSettings.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## findNewsletterSettingsByID

> Newslettersettingresponse findNewsletterSettingsByID(id, vestorlyAuth, opts)



Returns a single newsletter settings if the user has access

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.NewsletterSettingsApi();
let id = "id_example"; // String | Mongo ID of newsletter settings to fetch
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.findNewsletterSettingsByID(id, vestorlyAuth, opts, (error, data, response) => {
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
 **id** | **String**| Mongo ID of newsletter settings to fetch | 
 **vestorlyAuth** | **String**| Vestorly Auth Token | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**Newslettersettingresponse**](Newslettersettingresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## updateNewsletterSettingsByID

> Newslettersettingresponse updateNewsletterSettingsByID(id, vestorlyAuth, newsletterSetting, opts)



Update a single newsletter setting by ID

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.NewsletterSettingsApi();
let id = "id_example"; // String | Mongo ID of newsletter settings to update
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let newsletterSetting = new VestorlyApi.NewsletterSettingsInput(); // NewsletterSettingsInput | newsletter settings
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.updateNewsletterSettingsByID(id, vestorlyAuth, newsletterSetting, opts, (error, data, response) => {
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
 **id** | **String**| Mongo ID of newsletter settings to update | 
 **vestorlyAuth** | **String**| Vestorly Auth Token | 
 **newsletterSetting** | [**NewsletterSettingsInput**](NewsletterSettingsInput.md)| newsletter settings | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**Newslettersettingresponse**](Newslettersettingresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

