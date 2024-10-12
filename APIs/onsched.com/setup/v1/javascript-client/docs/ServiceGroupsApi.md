# OnSchedSetupApi.ServiceGroupsApi

All URIs are relative to *https://sandbox-api.onsched.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**setupV1ServicegroupsGet**](ServiceGroupsApi.md#setupV1ServicegroupsGet) | **GET** /setup/v1/servicegroups | List Service Groups
[**setupV1ServicegroupsIdDelete**](ServiceGroupsApi.md#setupV1ServicegroupsIdDelete) | **DELETE** /setup/v1/servicegroups/{id} | Delete Service Group
[**setupV1ServicegroupsIdGet**](ServiceGroupsApi.md#setupV1ServicegroupsIdGet) | **GET** /setup/v1/servicegroups/{id} | Get Service Group
[**setupV1ServicegroupsIdPut**](ServiceGroupsApi.md#setupV1ServicegroupsIdPut) | **PUT** /setup/v1/servicegroups/{id} | Update Service Group
[**setupV1ServicegroupsIdRecoverPut**](ServiceGroupsApi.md#setupV1ServicegroupsIdRecoverPut) | **PUT** /setup/v1/servicegroups/{id}/recover | Recover Service Group
[**setupV1ServicegroupsPost**](ServiceGroupsApi.md#setupV1ServicegroupsPost) | **POST** /setup/v1/servicegroups | Create Service Group



## setupV1ServicegroupsGet

> ServiceGroupListViewModel setupV1ServicegroupsGet(opts)

List Service Groups

&lt;p&gt;Use this endpoint to return a list of &lt;b&gt;Service Groups&lt;/b&gt; for the requested location. If no business location is specified it will default to the Primary Business Location of the company. Use the offset and limit parameters to control the page start and size. Default offset is 0, limit is 20, maximum is 100. Use the other query parameters to filter the results further.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ServiceGroupsApi();
let opts = {
  'locationId': "locationId_example", // String | id of business location, defaults to primary business location
  'offset': 56, // Number | Starting row of page, default 0
  'limit': 56 // Number | Page limit default 20, max 100
};
apiInstance.setupV1ServicegroupsGet(opts, (error, data, response) => {
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
 **offset** | **Number**| Starting row of page, default 0 | [optional] 
 **limit** | **Number**| Page limit default 20, max 100 | [optional] 

### Return type

[**ServiceGroupListViewModel**](ServiceGroupListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupV1ServicegroupsIdDelete

> ServiceGroupViewModel setupV1ServicegroupsIdDelete(id)

Delete Service Group

&lt;p&gt;Use this endpoint to &lt;b&gt;Delete&lt;/b&gt; a Service Group object. A valid &lt;b&gt;serviceGroup id&lt;/b&gt; is required. The service group is not permanently deleted and can be recovered by using the &lt;i&gt;PUT ​/setup​/v1​/servicegroups​/{id}​/recover&lt;/i&gt; endpoint.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ServiceGroupsApi();
let id = 56; // Number | id of serviceGroup object
apiInstance.setupV1ServicegroupsIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| id of serviceGroup object | 

### Return type

[**ServiceGroupViewModel**](ServiceGroupViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupV1ServicegroupsIdGet

> ServiceGroupViewModel setupV1ServicegroupsIdGet(id)

Get Service Group

&lt;p&gt;Use this endpoint to return a &lt;b&gt;Service Group&lt;/b&gt; object. A valid &lt;b&gt;serviceGroup id&lt;/b&gt; is required. Find service group id&#39;s by using the &lt;i&gt;GET /setup/v1/serviceGroups&lt;/i&gt; endpoint.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ServiceGroupsApi();
let id = 56; // Number | id of serviceGroup object
apiInstance.setupV1ServicegroupsIdGet(id, (error, data, response) => {
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
 **id** | **Number**| id of serviceGroup object | 

### Return type

[**ServiceGroupViewModel**](ServiceGroupViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupV1ServicegroupsIdPut

> ServiceGroupViewModel setupV1ServicegroupsIdPut(id, opts)

Update Service Group

&lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; a Service Group object. A valid &lt;b&gt;serviceGroup id&lt;/b&gt; is required. &lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ServiceGroupsApi();
let id = 56; // Number | id of serviceGroup object
let opts = {
  'serviceGroupInputModel': new OnSchedSetupApi.ServiceGroupInputModel() // ServiceGroupInputModel | 
};
apiInstance.setupV1ServicegroupsIdPut(id, opts, (error, data, response) => {
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
 **id** | **Number**| id of serviceGroup object | 
 **serviceGroupInputModel** | [**ServiceGroupInputModel**](ServiceGroupInputModel.md)|  | [optional] 

### Return type

[**ServiceGroupViewModel**](ServiceGroupViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json


## setupV1ServicegroupsIdRecoverPut

> ServiceGroupViewModel setupV1ServicegroupsIdRecoverPut(id)

Recover Service Group

&lt;p&gt;Use this endpoint to &lt;b&gt;Recover&lt;/b&gt; a deleted Service Group. A valid &lt;b&gt;serviceGroup id&lt;/b&gt; is required. &lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ServiceGroupsApi();
let id = 56; // Number | id of serviceGroup object
apiInstance.setupV1ServicegroupsIdRecoverPut(id, (error, data, response) => {
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
 **id** | **Number**| id of serviceGroup object | 

### Return type

[**ServiceGroupViewModel**](ServiceGroupViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupV1ServicegroupsPost

> ServiceGroupViewModel setupV1ServicegroupsPost(opts)

Create Service Group

&lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a Service Group. If no locationId is specified in the body, the business location will default to the primary business location. Service groups are used to categorize services. Service groups are optional and only make sense if you have multiple services that will be easier read if categorized. Only the service group Type of 0 is supported by the API. It defaults to 0 if not supplied.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ServiceGroupsApi();
let opts = {
  'serviceGroupInputModel': new OnSchedSetupApi.ServiceGroupInputModel() // ServiceGroupInputModel | 
};
apiInstance.setupV1ServicegroupsPost(opts, (error, data, response) => {
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
 **serviceGroupInputModel** | [**ServiceGroupInputModel**](ServiceGroupInputModel.md)|  | [optional] 

### Return type

[**ServiceGroupViewModel**](ServiceGroupViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json

