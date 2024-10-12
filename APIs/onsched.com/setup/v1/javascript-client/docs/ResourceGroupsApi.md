# OnSchedSetupApi.ResourceGroupsApi

All URIs are relative to *https://sandbox-api.onsched.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**setupV1ResourcegroupsGet**](ResourceGroupsApi.md#setupV1ResourcegroupsGet) | **GET** /setup/v1/resourcegroups | List Resource Groups
[**setupV1ResourcegroupsIdDelete**](ResourceGroupsApi.md#setupV1ResourcegroupsIdDelete) | **DELETE** /setup/v1/resourcegroups/{id} | Delete Resource Group
[**setupV1ResourcegroupsIdGet**](ResourceGroupsApi.md#setupV1ResourcegroupsIdGet) | **GET** /setup/v1/resourcegroups/{id} | Get Resource Group
[**setupV1ResourcegroupsIdPut**](ResourceGroupsApi.md#setupV1ResourcegroupsIdPut) | **PUT** /setup/v1/resourcegroups/{id} | Update Resource Group
[**setupV1ResourcegroupsIdRecoverPut**](ResourceGroupsApi.md#setupV1ResourcegroupsIdRecoverPut) | **PUT** /setup/v1/resourcegroups/{id}/recover | Recover Resource Group
[**setupV1ResourcegroupsPost**](ResourceGroupsApi.md#setupV1ResourcegroupsPost) | **POST** /setup/v1/resourcegroups | Create Resource Group



## setupV1ResourcegroupsGet

> ResourceGroupListViewModel setupV1ResourcegroupsGet(opts)

List Resource Groups

&lt;p&gt;Use this endpoint to &lt;b&gt;List Resource Groups&lt;/b&gt; for the specified location. If not specified, the business location defaults to the primary business location. &lt;b&gt;Name&lt;/b&gt; is a required field.&lt;/p&gt;  &lt;p&gt;Use the offset and limit parameters to control the page start and size. Default offset is 0, limit is 20, maximum is 100. Use the query parameters to filter the results further.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ResourceGroupsApi();
let opts = {
  'locationId': "locationId_example", // String | id of business location, defaults to primary business location
  'deleted': true, // Boolean | Filter results by deleted status
  'offset': 56, // Number | Starting row of page, default 0
  'limit': 56 // Number | Page limit default 20, max 100
};
apiInstance.setupV1ResourcegroupsGet(opts, (error, data, response) => {
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
 **locationId** | **String**| id of business location, defaults to primary business location | [optional] 
 **deleted** | **Boolean**| Filter results by deleted status | [optional] 
 **offset** | **Number**| Starting row of page, default 0 | [optional] 
 **limit** | **Number**| Page limit default 20, max 100 | [optional] 

### Return type

[**ResourceGroupListViewModel**](ResourceGroupListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupV1ResourcegroupsIdDelete

> ResourceGroupViewModel setupV1ResourcegroupsIdDelete(id)

Delete Resource Group

&lt;p&gt;Use this endpoint to &lt;b&gt;Delete&lt;/b&gt; a resourceGroup object. A valid &lt;b&gt;resourceGroup id&lt;/b&gt; is required. The resource group is not permanently deleted and can be recovered by using the &lt;i&gt;PUT ​/setup​/v1​/resourcegroups​/{id}​/recover&lt;/i&gt; endpoint.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ResourceGroupsApi();
let id = "id_example"; // String | id of resourceGroup object
apiInstance.setupV1ResourcegroupsIdDelete(id, (error, data, response) => {
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
 **id** | **String**| id of resourceGroup object | 

### Return type

[**ResourceGroupViewModel**](ResourceGroupViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupV1ResourcegroupsIdGet

> ResourceGroupViewModel setupV1ResourcegroupsIdGet(id)

Get Resource Group

&lt;p&gt;Use this endpoint to return a &lt;b&gt;Resource Group&lt;/b&gt; object. A valid &lt;b&gt;resourceGroup id&lt;/b&gt; is required. Find resourceGroup id&#39;s by using the &lt;i&gt;GET setup/v1/resourceGroups&lt;/i&gt; endpoint.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ResourceGroupsApi();
let id = "id_example"; // String | id of resourceGroup object
apiInstance.setupV1ResourcegroupsIdGet(id, (error, data, response) => {
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
 **id** | **String**| id of resourceGroup object | 

### Return type

[**ResourceGroupViewModel**](ResourceGroupViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupV1ResourcegroupsIdPut

> ResourceGroupViewModel setupV1ResourcegroupsIdPut(id, opts)

Update Resource Group

&lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; a resourceGroup object. A valid &lt;b&gt;resourceGroup id&lt;/b&gt; is required. &lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ResourceGroupsApi();
let id = "id_example"; // String | id of resourcGroup object
let opts = {
  'resourceGroupUpdateModel': new OnSchedSetupApi.ResourceGroupUpdateModel() // ResourceGroupUpdateModel | Resource Group Update Model
};
apiInstance.setupV1ResourcegroupsIdPut(id, opts, (error, data, response) => {
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
 **id** | **String**| id of resourcGroup object | 
 **resourceGroupUpdateModel** | [**ResourceGroupUpdateModel**](ResourceGroupUpdateModel.md)| Resource Group Update Model | [optional] 

### Return type

[**ResourceGroupViewModel**](ResourceGroupViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json


## setupV1ResourcegroupsIdRecoverPut

> ResourceViewModel setupV1ResourcegroupsIdRecoverPut(id)

Recover Resource Group

&lt;p&gt;Use this endpoint to &lt;b&gt;Recover&lt;/b&gt; a deleted resourceGroup object. A valid &lt;b&gt;resourceGroup id&lt;/b&gt; is required.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ResourceGroupsApi();
let id = "id_example"; // String | id of resourceGroup object
apiInstance.setupV1ResourcegroupsIdRecoverPut(id, (error, data, response) => {
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
 **id** | **String**| id of resourceGroup object | 

### Return type

[**ResourceViewModel**](ResourceViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupV1ResourcegroupsPost

> ResourceGroupViewModel setupV1ResourcegroupsPost(opts)

Create Resource Group

&lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a resourceGroup object. Resource groups are used to categorize your resources.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ResourceGroupsApi();
let opts = {
  'resourceGroupInputModel': new OnSchedSetupApi.ResourceGroupInputModel() // ResourceGroupInputModel | Resource input model
};
apiInstance.setupV1ResourcegroupsPost(opts, (error, data, response) => {
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
 **resourceGroupInputModel** | [**ResourceGroupInputModel**](ResourceGroupInputModel.md)| Resource input model | [optional] 

### Return type

[**ResourceGroupViewModel**](ResourceGroupViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json

