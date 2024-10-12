# BillbeeApi.WebhooksApi

All URIs are relative to *https://app.billbee.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webHookManagementDelete**](WebhooksApi.md#webHookManagementDelete) | **DELETE** /api/v1/webhooks/{id} | Deletes an existing WebHook registration.
[**webHookManagementDeleteAll**](WebhooksApi.md#webHookManagementDeleteAll) | **DELETE** /api/v1/webhooks | Deletes all existing WebHook registrations.
[**webHookManagementGet**](WebhooksApi.md#webHookManagementGet) | **GET** /api/v1/webhooks | Gets all registered WebHooks for a given user.
[**webHookManagementGetFilters**](WebhooksApi.md#webHookManagementGetFilters) | **GET** /api/v1/webhooks/filters | Returns a list of all known filters you can use to register webhooks
[**webHookManagementLookup**](WebhooksApi.md#webHookManagementLookup) | **GET** /api/v1/webhooks/{id} | Looks up a registered WebHook with the given {id} for a given user.
[**webHookManagementPost**](WebhooksApi.md#webHookManagementPost) | **POST** /api/v1/webhooks | Registers a new WebHook for a given user.
[**webHookManagementPut**](WebhooksApi.md#webHookManagementPut) | **PUT** /api/v1/webhooks/{id} | Updates an existing WebHook registration.



## webHookManagementDelete

> Object webHookManagementDelete(id)

Deletes an existing WebHook registration.

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.WebhooksApi();
let id = "id_example"; // String | The WebHook ID.
apiInstance.webHookManagementDelete(id, (error, data, response) => {
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
 **id** | **String**| The WebHook ID. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## webHookManagementDeleteAll

> Object webHookManagementDeleteAll()

Deletes all existing WebHook registrations.

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.WebhooksApi();
apiInstance.webHookManagementDeleteAll((error, data, response) => {
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

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## webHookManagementGet

> [RechnungsdruckWebAppControllersApiWebHookApiModel] webHookManagementGet()

Gets all registered WebHooks for a given user.

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.WebhooksApi();
apiInstance.webHookManagementGet((error, data, response) => {
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

[**[RechnungsdruckWebAppControllersApiWebHookApiModel]**](RechnungsdruckWebAppControllersApiWebHookApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## webHookManagementGetFilters

> Object webHookManagementGetFilters()

Returns a list of all known filters you can use to register webhooks

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.WebhooksApi();
apiInstance.webHookManagementGetFilters((error, data, response) => {
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

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## webHookManagementLookup

> RechnungsdruckWebAppControllersApiWebHookApiModel webHookManagementLookup(id)

Looks up a registered WebHook with the given {id} for a given user.

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.WebhooksApi();
let id = "id_example"; // String | 
apiInstance.webHookManagementLookup(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**RechnungsdruckWebAppControllersApiWebHookApiModel**](RechnungsdruckWebAppControllersApiWebHookApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## webHookManagementPost

> RechnungsdruckWebAppControllersApiWebHookApiModel webHookManagementPost(rechnungsdruckWebAppControllersApiWebHookApiModel)

Registers a new WebHook for a given user.

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.WebhooksApi();
let rechnungsdruckWebAppControllersApiWebHookApiModel = new BillbeeApi.RechnungsdruckWebAppControllersApiWebHookApiModel(); // RechnungsdruckWebAppControllersApiWebHookApiModel | The webhook to create. Attach ?noecho to the uri to prevent echo test.
apiInstance.webHookManagementPost(rechnungsdruckWebAppControllersApiWebHookApiModel, (error, data, response) => {
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
 **rechnungsdruckWebAppControllersApiWebHookApiModel** | [**RechnungsdruckWebAppControllersApiWebHookApiModel**](RechnungsdruckWebAppControllersApiWebHookApiModel.md)| The webhook to create. Attach ?noecho to the uri to prevent echo test. | 

### Return type

[**RechnungsdruckWebAppControllersApiWebHookApiModel**](RechnungsdruckWebAppControllersApiWebHookApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, text/json
- **Accept**: application/json, text/json


## webHookManagementPut

> RechnungsdruckWebAppControllersApiWebHookApiModel webHookManagementPut(id, rechnungsdruckWebAppControllersApiWebHookApiModel)

Updates an existing WebHook registration.

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.WebhooksApi();
let id = "id_example"; // String | The WebHook ID.
let rechnungsdruckWebAppControllersApiWebHookApiModel = new BillbeeApi.RechnungsdruckWebAppControllersApiWebHookApiModel(); // RechnungsdruckWebAppControllersApiWebHookApiModel | The new webhook to use.
apiInstance.webHookManagementPut(id, rechnungsdruckWebAppControllersApiWebHookApiModel, (error, data, response) => {
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
 **id** | **String**| The WebHook ID. | 
 **rechnungsdruckWebAppControllersApiWebHookApiModel** | [**RechnungsdruckWebAppControllersApiWebHookApiModel**](RechnungsdruckWebAppControllersApiWebHookApiModel.md)| The new webhook to use. | 

### Return type

[**RechnungsdruckWebAppControllersApiWebHookApiModel**](RechnungsdruckWebAppControllersApiWebHookApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, text/json
- **Accept**: application/json, text/json

