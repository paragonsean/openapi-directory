# ConfigCatPublicManagementApi.FeatureFlagsSettingsApi

All URIs are relative to *https://api.configcat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSetting**](FeatureFlagsSettingsApi.md#createSetting) | **POST** /v1/configs/{configId}/settings | Create Flag
[**deleteSetting**](FeatureFlagsSettingsApi.md#deleteSetting) | **DELETE** /v1/settings/{settingId} | Delete Flag
[**getSetting**](FeatureFlagsSettingsApi.md#getSetting) | **GET** /v1/settings/{settingId} | Get Flag
[**getSettings**](FeatureFlagsSettingsApi.md#getSettings) | **GET** /v1/configs/{configId}/settings | List Flags
[**updateSetting**](FeatureFlagsSettingsApi.md#updateSetting) | **PATCH** /v1/settings/{settingId} | Update Flag



## createSetting

> SettingModelHaljson createSetting(configId, createSettingInitialValues)

Create Flag

This endpoint creates a new Feature Flag or Setting in a specified Config identified by the &#x60;configId&#x60; parameter.  **Important:** The &#x60;key&#x60; attribute must be unique within the given Config.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.FeatureFlagsSettingsApi();
let configId = "configId_example"; // String | The identifier of the Config.
let createSettingInitialValues = new ConfigCatPublicManagementApi.CreateSettingInitialValues(); // CreateSettingInitialValues | 
apiInstance.createSetting(configId, createSettingInitialValues, (error, data, response) => {
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
 **configId** | **String**| The identifier of the Config. | 
 **createSettingInitialValues** | [**CreateSettingInitialValues**](CreateSettingInitialValues.md)|  | 

### Return type

[**SettingModelHaljson**](SettingModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/hal+json, application/json


## deleteSetting

> deleteSetting(settingId)

Delete Flag

This endpoint removes a Feature Flag or Setting from a specified Config,  identified by the &#x60;configId&#x60; parameter.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.FeatureFlagsSettingsApi();
let settingId = 56; // Number | The identifier of the Setting.
apiInstance.deleteSetting(settingId, (error, data, response) => {
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
 **settingId** | **Number**| The identifier of the Setting. | 

### Return type

null (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSetting

> SettingModelHaljson getSetting(settingId)

Get Flag

This endpoint returns the metadata attributes of a Feature Flag or Setting  identified by the &#x60;settingId&#x60; parameter.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.FeatureFlagsSettingsApi();
let settingId = 56; // Number | The identifier of the Setting.
apiInstance.getSetting(settingId, (error, data, response) => {
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
 **settingId** | **Number**| The identifier of the Setting. | 

### Return type

[**SettingModelHaljson**](SettingModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json, application/json


## getSettings

> [SettingModelHaljson] getSettings(configId)

List Flags

This endpoint returns the list of the Feature Flags and Settings defined in a  specified Config, identified by the &#x60;configId&#x60; parameter.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.FeatureFlagsSettingsApi();
let configId = "configId_example"; // String | The identifier of the Config.
apiInstance.getSettings(configId, (error, data, response) => {
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
 **configId** | **String**| The identifier of the Config. | 

### Return type

[**[SettingModelHaljson]**](SettingModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json, application/json


## updateSetting

> SettingModelHaljson updateSetting(settingId, jsonPatch)

Update Flag

This endpoint updates the metadata of a Feature Flag or Setting  with a collection of [JSON Patch](http://jsonpatch.com) operations in a specified Config.  Only the &#x60;name&#x60;, &#x60;hint&#x60; and &#x60;tags&#x60; attributes are modifiable by this endpoint. The &#x60;tags&#x60; attribute is a simple collection of the [tag IDs](#operation/get-tags) attached to the given setting.  The advantage of using JSON Patch is that you can describe individual update operations on a resource without touching attributes that you don&#39;t want to change.  For example: We have the following resource. &#x60;&#x60;&#x60; {  \&quot;settingId\&quot;: 5345,  \&quot;key\&quot;: \&quot;myGrandFeature\&quot;,  \&quot;name\&quot;: \&quot;Tihs is a naem with soem typos.\&quot;,  \&quot;hint\&quot;: \&quot;This flag controls my grandioso feature.\&quot;,  \&quot;settingType\&quot;: \&quot;boolean\&quot;,  \&quot;tags\&quot;: [   {    \&quot;tagId\&quot;: 0,    \&quot;name\&quot;: \&quot;sample tag\&quot;,    \&quot;color\&quot;: \&quot;whale\&quot;   }  ] } &#x60;&#x60;&#x60; If we send an update request body as below (it changes the name and adds the already existing tag with the id 2): &#x60;&#x60;&#x60; [  {   \&quot;op\&quot;: \&quot;replace\&quot;,   \&quot;path\&quot;: \&quot;/name\&quot;,   \&quot;value\&quot;: \&quot;This is the name without typos.\&quot;  },  {   \&quot;op\&quot;: \&quot;add\&quot;,   \&quot;path\&quot;: \&quot;/tags/-\&quot;,   \&quot;value\&quot;: 2  } ] &#x60;&#x60;&#x60; Only the &#x60;name&#x60; and &#x60;tags&#x60; are going to be updated and all the other attributes are remaining unchanged. So we get a response like this: &#x60;&#x60;&#x60; {  \&quot;settingId\&quot;: 5345,  \&quot;key\&quot;: \&quot;myGrandFeature\&quot;,  \&quot;name\&quot;: \&quot;This is the name without typos.\&quot;,  \&quot;hint\&quot;: \&quot;This flag controls my grandioso feature.\&quot;,  \&quot;settingType\&quot;: \&quot;boolean\&quot;,  \&quot;tags\&quot;: [   {    \&quot;tagId\&quot;: 0,    \&quot;name\&quot;: \&quot;sample tag\&quot;,    \&quot;color\&quot;: \&quot;whale\&quot;   },   {    \&quot;tagId\&quot;: 2,    \&quot;name\&quot;: \&quot;another tag\&quot;,    \&quot;color\&quot;: \&quot;koala\&quot;   }  ] } &#x60;&#x60;&#x60;

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.FeatureFlagsSettingsApi();
let settingId = 56; // Number | The identifier of the Setting.
let jsonPatch = new ConfigCatPublicManagementApi.JsonPatch(); // JsonPatch | 
apiInstance.updateSetting(settingId, jsonPatch, (error, data, response) => {
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
 **settingId** | **Number**| The identifier of the Setting. | 
 **jsonPatch** | [**JsonPatch**](JsonPatch.md)|  | 

### Return type

[**SettingModelHaljson**](SettingModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/hal+json, application/json

