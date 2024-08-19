# EDrvApi.DriversApi

All URIs are relative to *http://api.edrv.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteDriver**](DriversApi.md#deleteDriver) | **DELETE** /v1/drivers/{id} | 
[**getDriver**](DriversApi.md#getDriver) | **GET** /v1/drivers/{id} | 
[**getDrivers**](DriversApi.md#getDrivers) | **GET** /v1/drivers | 
[**patchDriver**](DriversApi.md#patchDriver) | **PATCH** /v1/drivers/{id} | 
[**postDrivers**](DriversApi.md#postDrivers) | **POST** /v1/drivers | 



## deleteDriver

> deleteDriver(id)



Delete a driver

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.DriversApi();
let id = "id_example"; // String | The driver id that needs to be deleted
apiInstance.deleteDriver(id, (error, data, response) => {
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
 **id** | **String**| The driver id that needs to be deleted | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDriver

> getDriver(id, opts)



Get a driver&#39;s data

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.DriversApi();
let id = "id_example"; // String | The driver id that needs to be fetched
let opts = {
  'includeTokens': true, // Boolean | Populate tokens
  'includeGroup': true, // Boolean | Populate group
  'includeOrganization': true // Boolean | Populate organization
};
apiInstance.getDriver(id, opts, (error, data, response) => {
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
 **id** | **String**| The driver id that needs to be fetched | 
 **includeTokens** | **Boolean**| Populate tokens | [optional] 
 **includeGroup** | **Boolean**| Populate group | [optional] 
 **includeOrganization** | **Boolean**| Populate organization | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDrivers

> GetDrivers200Response getDrivers(opts)



List all drivers

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.DriversApi();
let opts = {
  'active': true, // Boolean | Get a list of active drivers
  'paginateLimit': 20, // Number | Number of results per page
  'paginatePage': "paginatePage_example", // String | The queried page index
  'paginateEnabled': true, // Boolean | Enable pagination
  'sortBy': "'createdAt'", // String | Sort data by this key
  'sortOrder': "'desc'", // String | asc to sort ascending (default is desc - descending)
  'createdAtGte': new Date("2013-10-20T19:20:30+01:00"), // Date | Date as ISO String
  'createdAtLte': new Date("2013-10-20T19:20:30+01:00"), // Date | Date as ISO String
  'updatedAtGte': new Date("2013-10-20T19:20:30+01:00"), // Date | Date as ISO String
  'updatedAtLte': new Date("2013-10-20T19:20:30+01:00"), // Date | Date as ISO String
  'includeTokens': true, // Boolean | Populate tokens
  'includeGroup': true, // Boolean | Populate group
  'includeOrganization': true // Boolean | Populate organization
};
apiInstance.getDrivers(opts, (error, data, response) => {
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
 **active** | **Boolean**| Get a list of active drivers | [optional] 
 **paginateLimit** | **Number**| Number of results per page | [optional] [default to 20]
 **paginatePage** | **String**| The queried page index | [optional] 
 **paginateEnabled** | **Boolean**| Enable pagination | [optional] [default to true]
 **sortBy** | **String**| Sort data by this key | [optional] [default to &#39;createdAt&#39;]
 **sortOrder** | **String**| asc to sort ascending (default is desc - descending) | [optional] [default to &#39;desc&#39;]
 **createdAtGte** | **Date**| Date as ISO String | [optional] 
 **createdAtLte** | **Date**| Date as ISO String | [optional] 
 **updatedAtGte** | **Date**| Date as ISO String | [optional] 
 **updatedAtLte** | **Date**| Date as ISO String | [optional] 
 **includeTokens** | **Boolean**| Populate tokens | [optional] 
 **includeGroup** | **Boolean**| Populate group | [optional] 
 **includeOrganization** | **Boolean**| Populate organization | [optional] 

### Return type

[**GetDrivers200Response**](GetDrivers200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchDriver

> GetDrivers200Response patchDriver(id, patchDriverRequest)



Update a driver&#39;s data

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.DriversApi();
let id = "id_example"; // String | ID of driver that needs to be updated
let patchDriverRequest = new EDrvApi.PatchDriverRequest(); // PatchDriverRequest | Include driver properties to create here
apiInstance.patchDriver(id, patchDriverRequest, (error, data, response) => {
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
 **id** | **String**| ID of driver that needs to be updated | 
 **patchDriverRequest** | [**PatchDriverRequest**](PatchDriverRequest.md)| Include driver properties to create here | 

### Return type

[**GetDrivers200Response**](GetDrivers200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postDrivers

> PatchChargeStation200Response postDrivers(postDriversRequest)



Create a new driver

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.DriversApi();
let postDriversRequest = new EDrvApi.PostDriversRequest(); // PostDriversRequest | Include driver properties to create here
apiInstance.postDrivers(postDriversRequest, (error, data, response) => {
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
 **postDriversRequest** | [**PostDriversRequest**](PostDriversRequest.md)| Include driver properties to create here | 

### Return type

[**PatchChargeStation200Response**](PatchChargeStation200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

