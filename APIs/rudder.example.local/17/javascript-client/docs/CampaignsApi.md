# RudderApi.CampaignsApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allCampaigns**](CampaignsApi.md#allCampaigns) | **GET** /campaigns | Get all campaigns details
[**deleteCampaign**](CampaignsApi.md#deleteCampaign) | **DELETE** /campaigns/{id} | Delete a campaign
[**deleteCampaignEvent**](CampaignsApi.md#deleteCampaignEvent) | **DELETE** /campaigns/events/{id} | Delete a campaign event details
[**getAllCampaignEvents**](CampaignsApi.md#getAllCampaignEvents) | **GET** /campaigns/events | Get all campaign events
[**getCampaign**](CampaignsApi.md#getCampaign) | **GET** /campaigns/{id} | Get a campaign details
[**getCampaignEvent**](CampaignsApi.md#getCampaignEvent) | **GET** /campaigns/events/{id} | Get a campaign event details
[**getEventsCampaign**](CampaignsApi.md#getEventsCampaign) | **GET** /campaigns/{id}/events | Get campaign events for a campaign
[**saveCampaign**](CampaignsApi.md#saveCampaign) | **POST** /campaigns | Save a campaign
[**saveCampaignEvent**](CampaignsApi.md#saveCampaignEvent) | **POST** /campaigns/events/{id} | Update an existing event
[**scheduleCampaign**](CampaignsApi.md#scheduleCampaign) | **POST** /campaigns/{id}/schedule | Schedule a campaign event for a campaign



## allCampaigns

> AllCampaigns200Response allCampaigns(opts)

Get all campaigns details

Get all campaigns details

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.CampaignsApi();
let opts = {
  'campaignType': "system-update", // String | Type of the campaigns we want
  'status': "enabled" // String | Status of the campaigns we want
};
apiInstance.allCampaigns(opts, (error, data, response) => {
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
 **campaignType** | **String**| Type of the campaigns we want | [optional] 
 **status** | **String**| Status of the campaigns we want | [optional] 

### Return type

[**AllCampaigns200Response**](AllCampaigns200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteCampaign

> DeleteCampaign200Response deleteCampaign(id)

Delete a campaign

Delete a campaign

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.CampaignsApi();
let id = "0076a379-f32d-4732-9e91-33ab219d8fde"; // String | Id of the campaign
apiInstance.deleteCampaign(id, (error, data, response) => {
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
 **id** | **String**| Id of the campaign | 

### Return type

[**DeleteCampaign200Response**](DeleteCampaign200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteCampaignEvent

> DeleteCampaignEvent200Response deleteCampaignEvent(id)

Delete a campaign event details

Delete a campaign event details

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.CampaignsApi();
let id = "0076a379-f32d-4732-9e91-33ab219d8fde"; // String | Id of the campaign event
apiInstance.deleteCampaignEvent(id, (error, data, response) => {
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
 **id** | **String**| Id of the campaign event | 

### Return type

[**DeleteCampaignEvent200Response**](DeleteCampaignEvent200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllCampaignEvents

> GetAllCampaignEvents200Response getAllCampaignEvents(opts)

Get all campaign events

Get all campaign events

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.CampaignsApi();
let opts = {
  'campaignType': "system-update", // String | Type of the campaigns we want
  'state': "enabled", // String | Status of the campaign events we want
  'campaignId': "system-update", // String | id of the campaigns we want
  'limit': 56, // Number | Max number of elements in response
  'offset': 56, // Number | Offset of data in response (skip X elements)
  'before': new Date("2013-10-20"), // Date | 
  'after': new Date("2013-10-20"), // Date | 
  'order': "order_example", // String | 
  'asc': "asc_example" // String | 
};
apiInstance.getAllCampaignEvents(opts, (error, data, response) => {
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
 **campaignType** | **String**| Type of the campaigns we want | [optional] 
 **state** | **String**| Status of the campaign events we want | [optional] 
 **campaignId** | **String**| id of the campaigns we want | [optional] 
 **limit** | **Number**| Max number of elements in response | [optional] 
 **offset** | **Number**| Offset of data in response (skip X elements) | [optional] 
 **before** | **Date**|  | [optional] 
 **after** | **Date**|  | [optional] 
 **order** | **String**|  | [optional] 
 **asc** | **String**|  | [optional] 

### Return type

[**GetAllCampaignEvents200Response**](GetAllCampaignEvents200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCampaign

> GetCampaign200Response getCampaign(id)

Get a campaign details

Get a campaign details

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.CampaignsApi();
let id = "0076a379-f32d-4732-9e91-33ab219d8fde"; // String | Id of the campaign
apiInstance.getCampaign(id, (error, data, response) => {
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
 **id** | **String**| Id of the campaign | 

### Return type

[**GetCampaign200Response**](GetCampaign200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCampaignEvent

> GetAllCampaignEvents200Response getCampaignEvent(id)

Get a campaign event details

Get a campaign event details

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.CampaignsApi();
let id = "0076a379-f32d-4732-9e91-33ab219d8fde"; // String | Id of the campaign event
apiInstance.getCampaignEvent(id, (error, data, response) => {
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
 **id** | **String**| Id of the campaign event | 

### Return type

[**GetAllCampaignEvents200Response**](GetAllCampaignEvents200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventsCampaign

> GetEventsCampaign200Response getEventsCampaign(id, opts)

Get campaign events for a campaign

Get campaign events for a campaign

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.CampaignsApi();
let id = "0076a379-f32d-4732-9e91-33ab219d8fde"; // String | Id of the campaign
let opts = {
  'campaignType': "system-update", // String | Type of the campaigns we want
  'state': "enabled", // String | Status of the campaign events we want
  'limit': 56, // Number | Max number of elements in response
  'offset': 56, // Number | Offset of data in response (skip X elements)
  'before': new Date("2013-10-20"), // Date | 
  'after': new Date("2013-10-20"), // Date | 
  'order': "order_example", // String | 
  'asc': "asc_example" // String | 
};
apiInstance.getEventsCampaign(id, opts, (error, data, response) => {
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
 **id** | **String**| Id of the campaign | 
 **campaignType** | **String**| Type of the campaigns we want | [optional] 
 **state** | **String**| Status of the campaign events we want | [optional] 
 **limit** | **Number**| Max number of elements in response | [optional] 
 **offset** | **Number**| Offset of data in response (skip X elements) | [optional] 
 **before** | **Date**|  | [optional] 
 **after** | **Date**|  | [optional] 
 **order** | **String**|  | [optional] 
 **asc** | **String**|  | [optional] 

### Return type

[**GetEventsCampaign200Response**](GetEventsCampaign200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## saveCampaign

> SaveCampaign200Response saveCampaign(campaignDetails)

Save a campaign

Save a campaign details

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.CampaignsApi();
let campaignDetails = new RudderApi.CampaignDetails(); // CampaignDetails | 
apiInstance.saveCampaign(campaignDetails, (error, data, response) => {
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
 **campaignDetails** | [**CampaignDetails**](CampaignDetails.md)|  | 

### Return type

[**SaveCampaign200Response**](SaveCampaign200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## saveCampaignEvent

> SaveCampaignEvent200Response saveCampaignEvent(id)

Update an existing event

Update an existing event

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.CampaignsApi();
let id = "0076a379-f32d-4732-9e91-33ab219d8fde"; // String | Id of the campaign event
apiInstance.saveCampaignEvent(id, (error, data, response) => {
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
 **id** | **String**| Id of the campaign event | 

### Return type

[**SaveCampaignEvent200Response**](SaveCampaignEvent200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## scheduleCampaign

> ScheduleCampaign200Response scheduleCampaign(id)

Schedule a campaign event for a campaign

Schedule a campaign event for a campaign

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.CampaignsApi();
let id = "0076a379-f32d-4732-9e91-33ab219d8fde"; // String | Id of the campaign
apiInstance.scheduleCampaign(id, (error, data, response) => {
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
 **id** | **String**| Id of the campaign | 

### Return type

[**ScheduleCampaign200Response**](ScheduleCampaign200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

