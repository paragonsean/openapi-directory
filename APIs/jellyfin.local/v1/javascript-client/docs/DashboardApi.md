# JellyfinApi.DashboardApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getConfigurationPages**](DashboardApi.md#getConfigurationPages) | **GET** /web/ConfigurationPages | Gets the configuration pages.
[**getDashboardConfigurationPage**](DashboardApi.md#getDashboardConfigurationPage) | **GET** /web/ConfigurationPage | Gets a dashboard configuration page.



## getConfigurationPages

> [ConfigurationPageInfo] getConfigurationPages(opts)

Gets the configuration pages.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.DashboardApi();
let opts = {
  'enableInMainMenu': true, // Boolean | Whether to enable in the main menu.
  'pageType': new JellyfinApi.ConfigurationPageType() // ConfigurationPageType | The Jellyfin.Api.Models.ConfigurationPageInfo.
};
apiInstance.getConfigurationPages(opts, (error, data, response) => {
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
 **enableInMainMenu** | **Boolean**| Whether to enable in the main menu. | [optional] 
 **pageType** | [**ConfigurationPageType**](.md)| The Jellyfin.Api.Models.ConfigurationPageInfo. | [optional] 

### Return type

[**[ConfigurationPageInfo]**](ConfigurationPageInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getDashboardConfigurationPage

> File getDashboardConfigurationPage(opts)

Gets a dashboard configuration page.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.DashboardApi();
let opts = {
  'name': "name_example" // String | The name of the page.
};
apiInstance.getDashboardConfigurationPage(opts, (error, data, response) => {
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
 **name** | **String**| The name of the page. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/x-javascript, text/html, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase

