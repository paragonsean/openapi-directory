# ElmahIoApi.DeploymentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deploymentsCreate**](DeploymentsApi.md#deploymentsCreate) | **POST** /v3/deployments | Create a new deployment.
[**deploymentsDelete**](DeploymentsApi.md#deploymentsDelete) | **DELETE** /v3/deployments/{id} | Delete a deployment by its ID.
[**deploymentsGet**](DeploymentsApi.md#deploymentsGet) | **GET** /v3/deployments/{id} | Fetch a deployment by its ID.
[**deploymentsGetAll**](DeploymentsApi.md#deploymentsGetAll) | **GET** /v3/deployments | Fetch a list of deployments.



## deploymentsCreate

> CreateDeploymentResult deploymentsCreate(opts)

Create a new deployment.

Required permission: &#x60;deployments_write&#x60;

### Example

```javascript
import ElmahIoApi from 'elmah_io_api';
let defaultClient = ElmahIoApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ElmahIoApi.DeploymentsApi();
let opts = {
  'createDeployment': new ElmahIoApi.CreateDeployment() // CreateDeployment | The deployment object to create.
};
apiInstance.deploymentsCreate(opts, (error, data, response) => {
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
 **createDeployment** | [**CreateDeployment**](CreateDeployment.md)| The deployment object to create. | [optional] 

### Return type

[**CreateDeploymentResult**](CreateDeploymentResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## deploymentsDelete

> deploymentsDelete(id)

Delete a deployment by its ID.

This endpoint doesn&#39;t clear the version number of messages already annotated with this deployment version.&lt;br/&gt;&lt;br/&gt;Required permission: &#x60;deployments_delete&#x60;

### Example

```javascript
import ElmahIoApi from 'elmah_io_api';
let defaultClient = ElmahIoApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ElmahIoApi.DeploymentsApi();
let id = "id_example"; // String | The ID of the deployment to delete.
apiInstance.deploymentsDelete(id, (error, data, response) => {
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
 **id** | **String**| The ID of the deployment to delete. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deploymentsGet

> Deployment deploymentsGet(id)

Fetch a deployment by its ID.

Required permission: &#x60;deployments_read&#x60;

### Example

```javascript
import ElmahIoApi from 'elmah_io_api';
let defaultClient = ElmahIoApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ElmahIoApi.DeploymentsApi();
let id = "id_example"; // String | The ID of the deployment to fetch.
apiInstance.deploymentsGet(id, (error, data, response) => {
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
 **id** | **String**| The ID of the deployment to fetch. | 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## deploymentsGetAll

> [Deployment] deploymentsGetAll()

Fetch a list of deployments.

Required permission: &#x60;deployments_read&#x60;

### Example

```javascript
import ElmahIoApi from 'elmah_io_api';
let defaultClient = ElmahIoApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ElmahIoApi.DeploymentsApi();
apiInstance.deploymentsGetAll((error, data, response) => {
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

[**[Deployment]**](Deployment.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

