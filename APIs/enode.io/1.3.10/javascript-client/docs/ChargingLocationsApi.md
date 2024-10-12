# EnodeApi.ChargingLocationsApi

All URIs are relative to *https://api.test.enode.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteCharginglocationsCharginglocationid**](ChargingLocationsApi.md#deleteCharginglocationsCharginglocationid) | **DELETE** /charging-locations/{chargingLocationId} | Delete Charging Location
[**getCharginglocations**](ChargingLocationsApi.md#getCharginglocations) | **GET** /charging-locations | List Charging Locations
[**getCharginglocationsCharginglocationid**](ChargingLocationsApi.md#getCharginglocationsCharginglocationid) | **GET** /charging-locations/{chargingLocationId} | Get Charging Location
[**postCharginglocations**](ChargingLocationsApi.md#postCharginglocations) | **POST** /charging-locations | Create Charging Location
[**putCharginglocationsCharginglocationid**](ChargingLocationsApi.md#putCharginglocationsCharginglocationid) | **PUT** /charging-locations/{chargingLocationId} | Update Charging Location



## deleteCharginglocationsCharginglocationid

> deleteCharginglocationsCharginglocationid(chargingLocationId)

Delete Charging Location

Delete a Charging Location

### Example

```javascript
import EnodeApi from 'enode_api';
let defaultClient = EnodeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: UserAccessToken
let UserAccessToken = defaultClient.authentications['UserAccessToken'];
UserAccessToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnodeApi.ChargingLocationsApi();
let chargingLocationId = "chargingLocationId_example"; // String | ID of the Charging Location
apiInstance.deleteCharginglocationsCharginglocationid(chargingLocationId, (error, data, response) => {
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
 **chargingLocationId** | **String**| ID of the Charging Location | 

### Return type

null (empty response body)

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getCharginglocations

> [Object] getCharginglocations()

List Charging Locations

Returns a list of Charging Locations registered to the User

### Example

```javascript
import EnodeApi from 'enode_api';
let defaultClient = EnodeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: UserAccessToken
let UserAccessToken = defaultClient.authentications['UserAccessToken'];
UserAccessToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnodeApi.ChargingLocationsApi();
apiInstance.getCharginglocations((error, data, response) => {
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

**[Object]**

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCharginglocationsCharginglocationid

> Object getCharginglocationsCharginglocationid(chargingLocationId)

Get Charging Location

### Example

```javascript
import EnodeApi from 'enode_api';
let defaultClient = EnodeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: UserAccessToken
let UserAccessToken = defaultClient.authentications['UserAccessToken'];
UserAccessToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnodeApi.ChargingLocationsApi();
let chargingLocationId = "chargingLocationId_example"; // String | ID of the Charging Location
apiInstance.getCharginglocationsCharginglocationid(chargingLocationId, (error, data, response) => {
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
 **chargingLocationId** | **String**| ID of the Charging Location | 

### Return type

**Object**

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postCharginglocations

> Object postCharginglocations(opts)

Create Charging Location

### Example

```javascript
import EnodeApi from 'enode_api';
let defaultClient = EnodeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: UserAccessToken
let UserAccessToken = defaultClient.authentications['UserAccessToken'];
UserAccessToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnodeApi.ChargingLocationsApi();
let opts = {
  'postCharginglocationsRequest': new EnodeApi.PostCharginglocationsRequest() // PostCharginglocationsRequest | 
};
apiInstance.postCharginglocations(opts, (error, data, response) => {
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
 **postCharginglocationsRequest** | [**PostCharginglocationsRequest**](PostCharginglocationsRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putCharginglocationsCharginglocationid

> Object putCharginglocationsCharginglocationid(chargingLocationId, opts)

Update Charging Location

Updates a charging location with new configuration

### Example

```javascript
import EnodeApi from 'enode_api';
let defaultClient = EnodeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: UserAccessToken
let UserAccessToken = defaultClient.authentications['UserAccessToken'];
UserAccessToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnodeApi.ChargingLocationsApi();
let chargingLocationId = "chargingLocationId_example"; // String | ID of the Charging Location
let opts = {
  'body': null // Object | 
};
apiInstance.putCharginglocationsCharginglocationid(chargingLocationId, opts, (error, data, response) => {
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
 **chargingLocationId** | **String**| ID of the Charging Location | 
 **body** | **Object**|  | [optional] 

### Return type

**Object**

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

