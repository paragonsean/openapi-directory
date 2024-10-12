# Vimeo.OnDemandRegionsApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addVodRegion**](OnDemandRegionsApi.md#addVodRegion) | **PUT** /ondemand/pages/{ondemand_id}/regions/{country} | Add a specific region to an On Demand page
[**deleteVodRegion**](OnDemandRegionsApi.md#deleteVodRegion) | **DELETE** /ondemand/pages/{ondemand_id}/regions/{country} | Remove a specific region from an On Demand page
[**deleteVodRegions**](OnDemandRegionsApi.md#deleteVodRegions) | **DELETE** /ondemand/pages/{ondemand_id}/regions | Remove a list of regions from an On Demand page
[**getRegion**](OnDemandRegionsApi.md#getRegion) | **GET** /ondemand/regions/{country} | Get a specific On Demand region
[**getRegions**](OnDemandRegionsApi.md#getRegions) | **GET** /ondemand/regions | Get all the On Demand regions
[**getVodRegion**](OnDemandRegionsApi.md#getVodRegion) | **GET** /ondemand/pages/{ondemand_id}/regions/{country} | Get a specific region of an On Demand page
[**getVodRegions**](OnDemandRegionsApi.md#getVodRegions) | **GET** /ondemand/pages/{ondemand_id}/regions | Get all the regions of an On Demand page
[**setVodRegions**](OnDemandRegionsApi.md#setVodRegions) | **PUT** /ondemand/pages/{ondemand_id}/regions | Add a list of regions to an On Demand page



## addVodRegion

> OnDemandRegion addVodRegion(country, ondemandId)

Add a specific region to an On Demand page

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.OnDemandRegionsApi();
let country = "US"; // String | The country code.
let ondemandId = 61326; // Number | The ID of the On Demand.
apiInstance.addVodRegion(country, ondemandId, (error, data, response) => {
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
 **country** | **String**| The country code. | 
 **ondemandId** | **Number**| The ID of the On Demand. | 

### Return type

[**OnDemandRegion**](OnDemandRegion.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.ondemand.region+json


## deleteVodRegion

> deleteVodRegion(country, ondemandId)

Remove a specific region from an On Demand page

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.OnDemandRegionsApi();
let country = "US"; // String | The country code.
let ondemandId = 61326; // Number | The ID of the On Demand.
apiInstance.deleteVodRegion(country, ondemandId, (error, data, response) => {
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
 **country** | **String**| The country code. | 
 **ondemandId** | **Number**| The ID of the On Demand. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.ondemand.region+json


## deleteVodRegions

> [OnDemandRegion] deleteVodRegions(ondemandId, opts)

Remove a list of regions from an On Demand page

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.OnDemandRegionsApi();
let ondemandId = 61326; // Number | The ID of the On Demand.
let opts = {
  'deleteVodRegionsRequest': new Vimeo.DeleteVodRegionsRequest() // DeleteVodRegionsRequest | 
};
apiInstance.deleteVodRegions(ondemandId, opts, (error, data, response) => {
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
 **ondemandId** | **Number**| The ID of the On Demand. | 
 **deleteVodRegionsRequest** | [**DeleteVodRegionsRequest**](DeleteVodRegionsRequest.md)|  | [optional] 

### Return type

[**[OnDemandRegion]**](OnDemandRegion.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.ondemand.region+json
- **Accept**: application/vnd.vimeo.ondemand.region+json


## getRegion

> OnDemandRegion getRegion(country)

Get a specific On Demand region

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.OnDemandRegionsApi();
let country = "US"; // String | The country code.
apiInstance.getRegion(country, (error, data, response) => {
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
 **country** | **String**| The country code. | 

### Return type

[**OnDemandRegion**](OnDemandRegion.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.ondemand.region+json


## getRegions

> [OnDemandRegion] getRegions()

Get all the On Demand regions

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.OnDemandRegionsApi();
apiInstance.getRegions((error, data, response) => {
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

[**[OnDemandRegion]**](OnDemandRegion.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.ondemand.region+json


## getVodRegion

> OnDemandRegion getVodRegion(country, ondemandId)

Get a specific region of an On Demand page

Checks whether an On Demand page belongs to a region.

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.OnDemandRegionsApi();
let country = "US"; // String | The country code.
let ondemandId = 61326; // Number | The ID of the On Demand.
apiInstance.getVodRegion(country, ondemandId, (error, data, response) => {
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
 **country** | **String**| The country code. | 
 **ondemandId** | **Number**| The ID of the On Demand. | 

### Return type

[**OnDemandRegion**](OnDemandRegion.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.ondemand.region+json


## getVodRegions

> [OnDemandRegion] getVodRegions(ondemandId)

Get all the regions of an On Demand page

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.OnDemandRegionsApi();
let ondemandId = 61326; // Number | The ID of the On Demand.
apiInstance.getVodRegions(ondemandId, (error, data, response) => {
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
 **ondemandId** | **Number**| The ID of the On Demand. | 

### Return type

[**[OnDemandRegion]**](OnDemandRegion.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.ondemand.region+json


## setVodRegions

> OnDemandRegion setVodRegions(ondemandId, setVodRegionsRequest)

Add a list of regions to an On Demand page

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.OnDemandRegionsApi();
let ondemandId = 61326; // Number | The ID of the On Demand.
let setVodRegionsRequest = new Vimeo.SetVodRegionsRequest(); // SetVodRegionsRequest | 
apiInstance.setVodRegions(ondemandId, setVodRegionsRequest, (error, data, response) => {
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
 **ondemandId** | **Number**| The ID of the On Demand. | 
 **setVodRegionsRequest** | [**SetVodRegionsRequest**](SetVodRegionsRequest.md)|  | 

### Return type

[**OnDemandRegion**](OnDemandRegion.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.ondemand.region+json
- **Accept**: application/vnd.vimeo.ondemand.region+json

