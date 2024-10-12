# TheJiraCloudPlatformRestApi.AnnouncementBannerApi

All URIs are relative to *https://your-domain.atlassian.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBanner**](AnnouncementBannerApi.md#getBanner) | **GET** /rest/api/3/announcementBanner | Get announcement banner configuration
[**setBanner**](AnnouncementBannerApi.md#setBanner) | **PUT** /rest/api/3/announcementBanner | Update announcement banner configuration



## getBanner

> AnnouncementBannerConfiguration getBanner()

Get announcement banner configuration

Returns the current announcement banner configuration.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.AnnouncementBannerApi();
apiInstance.getBanner((error, data, response) => {
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

[**AnnouncementBannerConfiguration**](AnnouncementBannerConfiguration.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setBanner

> Object setBanner(announcementBannerConfigurationUpdate)

Update announcement banner configuration

Updates the announcement banner configuration.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.AnnouncementBannerApi();
let announcementBannerConfigurationUpdate = {"isDismissible":false,"isEnabled":true,"message":"This is a public, enabled, non-dismissible banner, set using the API","visibility":"public"}; // AnnouncementBannerConfigurationUpdate | 
apiInstance.setBanner(announcementBannerConfigurationUpdate, (error, data, response) => {
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
 **announcementBannerConfigurationUpdate** | [**AnnouncementBannerConfigurationUpdate**](AnnouncementBannerConfigurationUpdate.md)|  | 

### Return type

**Object**

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

