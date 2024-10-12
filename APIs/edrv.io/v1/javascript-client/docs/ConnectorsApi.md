# EDrvApi.ConnectorsApi

All URIs are relative to *http://api.edrv.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteConnector**](ConnectorsApi.md#deleteConnector) | **DELETE** /v1/connectors/{id} | 
[**getConnector**](ConnectorsApi.md#getConnector) | **GET** /v1/connectors/{id} | 
[**getConnectors**](ConnectorsApi.md#getConnectors) | **GET** /v1/connectors | 
[**patchConnector**](ConnectorsApi.md#patchConnector) | **PATCH** /v1/connectors/{id} | 
[**postConnectors**](ConnectorsApi.md#postConnectors) | **POST** /v1/connectors | 



## deleteConnector

> deleteConnector(id)



Delete a connector

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.ConnectorsApi();
let id = "id_example"; // String | The connector id that needs to be deleted
apiInstance.deleteConnector(id, (error, data, response) => {
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
 **id** | **String**| The connector id that needs to be deleted | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getConnector

> getConnector(id, opts)



Get a connector

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.ConnectorsApi();
let id = "id_example"; // String | ID of connector that needs to be fetched
let opts = {
  'includeEvse': true, // Boolean | Populate evse
  'includeOrganization': true, // Boolean | Populate organization
  'includeRate': true // Boolean | Populate rate
};
apiInstance.getConnector(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of connector that needs to be fetched | 
 **includeEvse** | **Boolean**| Populate evse | [optional] 
 **includeOrganization** | **Boolean**| Populate organization | [optional] 
 **includeRate** | **Boolean**| Populate rate | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getConnectors

> getConnectors(opts)



List connectors

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.ConnectorsApi();
let opts = {
  'paginateLimit': 20, // Number | Number of results per page
  'paginatePage': "paginatePage_example", // String | The queried page index
  'paginateEnabled': true, // Boolean | Enable pagination
  'sortBy': "'createdAt'", // String | Sort data by this key
  'sortOrder': "'desc'", // String | asc to sort ascending (default is desc - descending)
  'createdAtGte': new Date("2013-10-20T19:20:30+01:00"), // Date | Date as ISO String
  'createdAtLte': new Date("2013-10-20T19:20:30+01:00"), // Date | Date as ISO String
  'updatedAtGte': new Date("2013-10-20T19:20:30+01:00"), // Date | Date as ISO String
  'updatedAtLte': new Date("2013-10-20T19:20:30+01:00"), // Date | Date as ISO String
  'includeEvse': true, // Boolean | Populate evse
  'includeOrganization': true, // Boolean | Populate organization
  'includeRate': true // Boolean | Populate rate
};
apiInstance.getConnectors(opts, (error, data, response) => {
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
 **paginateLimit** | **Number**| Number of results per page | [optional] [default to 20]
 **paginatePage** | **String**| The queried page index | [optional] 
 **paginateEnabled** | **Boolean**| Enable pagination | [optional] [default to true]
 **sortBy** | **String**| Sort data by this key | [optional] [default to &#39;createdAt&#39;]
 **sortOrder** | **String**| asc to sort ascending (default is desc - descending) | [optional] [default to &#39;desc&#39;]
 **createdAtGte** | **Date**| Date as ISO String | [optional] 
 **createdAtLte** | **Date**| Date as ISO String | [optional] 
 **updatedAtGte** | **Date**| Date as ISO String | [optional] 
 **updatedAtLte** | **Date**| Date as ISO String | [optional] 
 **includeEvse** | **Boolean**| Populate evse | [optional] 
 **includeOrganization** | **Boolean**| Populate organization | [optional] 
 **includeRate** | **Boolean**| Populate rate | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## patchConnector

> PatchChargeStation200Response patchConnector(id, postConnectorsRequest)



Update a connector&#39;s data

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.ConnectorsApi();
let id = "id_example"; // String | ID of connector that needs to be updated
let postConnectorsRequest = new EDrvApi.PostConnectorsRequest(); // PostConnectorsRequest | Include connector properties to update here
apiInstance.patchConnector(id, postConnectorsRequest, (error, data, response) => {
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
 **id** | **String**| ID of connector that needs to be updated | 
 **postConnectorsRequest** | [**PostConnectorsRequest**](PostConnectorsRequest.md)| Include connector properties to update here | 

### Return type

[**PatchChargeStation200Response**](PatchChargeStation200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postConnectors

> PatchChargeStation200Response postConnectors(postConnectorsRequest)



Create a new connector

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.ConnectorsApi();
let postConnectorsRequest = new EDrvApi.PostConnectorsRequest(); // PostConnectorsRequest | Include Connector properties to create here
apiInstance.postConnectors(postConnectorsRequest, (error, data, response) => {
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
 **postConnectorsRequest** | [**PostConnectorsRequest**](PostConnectorsRequest.md)| Include Connector properties to create here | 

### Return type

[**PatchChargeStation200Response**](PatchChargeStation200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

