# DockerHubApi.OrgSettingsApi

All URIs are relative to *https://hub.docker.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2OrgsNameSettingsGet**](OrgSettingsApi.md#v2OrgsNameSettingsGet) | **GET** /v2/orgs/{name}/settings | Get organization settings
[**v2OrgsNameSettingsPut**](OrgSettingsApi.md#v2OrgsNameSettingsPut) | **PUT** /v2/orgs/{name}/settings | Update organization settings



## v2OrgsNameSettingsGet

> OrgSettings v2OrgsNameSettingsGet(name)

Get organization settings

Returns organization settings by name. 

### Example

```javascript
import DockerHubApi from 'docker_hub_api';

let apiInstance = new DockerHubApi.OrgSettingsApi();
let name = "name_example"; // String | Name of the organization.
apiInstance.v2OrgsNameSettingsGet(name, (error, data, response) => {
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
 **name** | **String**| Name of the organization. | 

### Return type

[**OrgSettings**](OrgSettings.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v2OrgsNameSettingsPut

> OrgSettings v2OrgsNameSettingsPut(name, v2OrgsNameSettingsPutRequest)

Update organization settings

Updates an organization&#39;s settings. Some settings are only used when the organization is on a business plan.  ***Only users in the \&quot;owners\&quot; group of the organization can use this endpoint.***  The following settings are only used on a business plan: - &#x60;restricted_images&#x60; 

### Example

```javascript
import DockerHubApi from 'docker_hub_api';

let apiInstance = new DockerHubApi.OrgSettingsApi();
let name = "name_example"; // String | Name of the organization.
let v2OrgsNameSettingsPutRequest = new DockerHubApi.V2OrgsNameSettingsPutRequest(); // V2OrgsNameSettingsPutRequest | 
apiInstance.v2OrgsNameSettingsPut(name, v2OrgsNameSettingsPutRequest, (error, data, response) => {
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
 **name** | **String**| Name of the organization. | 
 **v2OrgsNameSettingsPutRequest** | [**V2OrgsNameSettingsPutRequest**](V2OrgsNameSettingsPutRequest.md)|  | 

### Return type

[**OrgSettings**](OrgSettings.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

