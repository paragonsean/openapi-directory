# ConfigCatPublicManagementApi.IntegrationLinksApi

All URIs are relative to *https://api.configcat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addOrUpdateIntegrationLink**](IntegrationLinksApi.md#addOrUpdateIntegrationLink) | **POST** /v1/environments/{environmentId}/settings/{settingId}/integrationLinks/{integrationLinkType}/{key} | Add or update Integration link
[**deleteIntegrationLink**](IntegrationLinksApi.md#deleteIntegrationLink) | **DELETE** /v1/environments/{environmentId}/settings/{settingId}/integrationLinks/{integrationLinkType}/{key} | Delete Integration link
[**getIntegrationLinkDetails**](IntegrationLinksApi.md#getIntegrationLinkDetails) | **GET** /v1/integrationLink/{integrationLinkType}/{key}/details | Get Integration link
[**jiraAddOrUpdateIntegrationLink**](IntegrationLinksApi.md#jiraAddOrUpdateIntegrationLink) | **POST** /v1/jira/environments/{environmentId}/settings/{settingId}/integrationLinks/{key} | 
[**v1JiraConnectPost**](IntegrationLinksApi.md#v1JiraConnectPost) | **POST** /v1/jira/Connect | 



## addOrUpdateIntegrationLink

> IntegrationLinkModel addOrUpdateIntegrationLink(environmentId, settingId, integrationLinkType, key, opts)

Add or update Integration link



### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.IntegrationLinksApi();
let environmentId = "environmentId_example"; // String | The identifier of the Environment.
let settingId = 56; // Number | The id of the Setting.
let integrationLinkType = new ConfigCatPublicManagementApi.IntegrationLinkType(); // IntegrationLinkType | The integration link's type.
let key = "key_example"; // String | The key of the integration link.
let opts = {
  'addOrUpdateIntegrationLinkModel': new ConfigCatPublicManagementApi.AddOrUpdateIntegrationLinkModel() // AddOrUpdateIntegrationLinkModel | 
};
apiInstance.addOrUpdateIntegrationLink(environmentId, settingId, integrationLinkType, key, opts, (error, data, response) => {
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
 **environmentId** | **String**| The identifier of the Environment. | 
 **settingId** | **Number**| The id of the Setting. | 
 **integrationLinkType** | [**IntegrationLinkType**](.md)| The integration link&#39;s type. | 
 **key** | **String**| The key of the integration link. | 
 **addOrUpdateIntegrationLinkModel** | [**AddOrUpdateIntegrationLinkModel**](AddOrUpdateIntegrationLinkModel.md)|  | [optional] 

### Return type

[**IntegrationLinkModel**](IntegrationLinkModel.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/hal+json, application/json


## deleteIntegrationLink

> DeleteIntegrationLinkModel deleteIntegrationLink(environmentId, settingId, integrationLinkType, key)

Delete Integration link



### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.IntegrationLinksApi();
let environmentId = "environmentId_example"; // String | The identifier of the Environment.
let settingId = 56; // Number | The id of the Setting.
let integrationLinkType = new ConfigCatPublicManagementApi.IntegrationLinkType(); // IntegrationLinkType | The integration's type.
let key = "key_example"; // String | The key of the integration link.
apiInstance.deleteIntegrationLink(environmentId, settingId, integrationLinkType, key, (error, data, response) => {
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
 **environmentId** | **String**| The identifier of the Environment. | 
 **settingId** | **Number**| The id of the Setting. | 
 **integrationLinkType** | [**IntegrationLinkType**](.md)| The integration&#39;s type. | 
 **key** | **String**| The key of the integration link. | 

### Return type

[**DeleteIntegrationLinkModel**](DeleteIntegrationLinkModel.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json, application/json


## getIntegrationLinkDetails

> IntegrationLinkDetailsModel getIntegrationLinkDetails(integrationLinkType, key)

Get Integration link



### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.IntegrationLinksApi();
let integrationLinkType = new ConfigCatPublicManagementApi.IntegrationLinkType(); // IntegrationLinkType | The integration link's type.
let key = "key_example"; // String | The key of the integration link.
apiInstance.getIntegrationLinkDetails(integrationLinkType, key, (error, data, response) => {
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
 **integrationLinkType** | [**IntegrationLinkType**](.md)| The integration link&#39;s type. | 
 **key** | **String**| The key of the integration link. | 

### Return type

[**IntegrationLinkDetailsModel**](IntegrationLinkDetailsModel.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json, application/json


## jiraAddOrUpdateIntegrationLink

> IntegrationLinkModel jiraAddOrUpdateIntegrationLink(environmentId, settingId, key, opts)



### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.IntegrationLinksApi();
let environmentId = "environmentId_example"; // String | The identifier of the Environment.
let settingId = 56; // Number | The id of the Setting.
let key = "key_example"; // String | The key of the integration link.
let opts = {
  'addOrUpdateJiraIntegrationLinkModel': new ConfigCatPublicManagementApi.AddOrUpdateJiraIntegrationLinkModel() // AddOrUpdateJiraIntegrationLinkModel | 
};
apiInstance.jiraAddOrUpdateIntegrationLink(environmentId, settingId, key, opts, (error, data, response) => {
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
 **environmentId** | **String**| The identifier of the Environment. | 
 **settingId** | **Number**| The id of the Setting. | 
 **key** | **String**| The key of the integration link. | 
 **addOrUpdateJiraIntegrationLinkModel** | [**AddOrUpdateJiraIntegrationLinkModel**](AddOrUpdateJiraIntegrationLinkModel.md)|  | [optional] 

### Return type

[**IntegrationLinkModel**](IntegrationLinkModel.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/hal+json, application/json


## v1JiraConnectPost

> v1JiraConnectPost(opts)



### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.IntegrationLinksApi();
let opts = {
  'connectRequest': new ConfigCatPublicManagementApi.ConnectRequest() // ConnectRequest | 
};
apiInstance.v1JiraConnectPost(opts, (error, data, response) => {
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
 **connectRequest** | [**ConnectRequest**](ConnectRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: Not defined

