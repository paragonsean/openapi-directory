# RudderApi.SystemUpdateCampaignsApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCampaignEventResult**](SystemUpdateCampaignsApi.md#getCampaignEventResult) | **GET** /systemUpdate/events/{id}/result | Get a campaign event result
[**getCampaignEventResultForNode**](SystemUpdateCampaignsApi.md#getCampaignEventResultForNode) | **GET** /systemUpdate/events/{id}/result/{nodeId} | Get detailed campaign event result for a Node
[**getCampaignHistory**](SystemUpdateCampaignsApi.md#getCampaignHistory) | **GET** /systemUpdate/campaigns/{id}/history | Get a campaign result history



## getCampaignEventResult

> GetCampaignEventResult200Response getCampaignEventResult(id)

Get a campaign event result

Get a campaign event result

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.SystemUpdateCampaignsApi();
let id = "0076a379-f32d-4732-9e91-33ab219d8fde"; // String | Id of the campaign event
apiInstance.getCampaignEventResult(id, (error, data, response) => {
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

[**GetCampaignEventResult200Response**](GetCampaignEventResult200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCampaignEventResultForNode

> GetCampaignEventResultForNode200Response getCampaignEventResultForNode(id, nodeId)

Get detailed campaign event result for a Node

Get detailed campaign event result for a Node

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.SystemUpdateCampaignsApi();
let id = "0076a379-f32d-4732-9e91-33ab219d8fde"; // String | Id of the campaign event
let nodeId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the target node
apiInstance.getCampaignEventResultForNode(id, nodeId, (error, data, response) => {
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
 **nodeId** | **String**| Id of the target node | 

### Return type

[**GetCampaignEventResultForNode200Response**](GetCampaignEventResultForNode200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCampaignHistory

> GetCampaignHistory200Response getCampaignHistory(id, opts)

Get a campaign result history

Get a campaign result history

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.SystemUpdateCampaignsApi();
let id = "0076a379-f32d-4732-9e91-33ab219d8fde"; // String | Id of the campaign
let opts = {
  'limit': 56, // Number | Max number of elements in response
  'offset': 56, // Number | Offset of data in response (skip X elements)
  'before': new Date("2013-10-20"), // Date | 
  'after': new Date("2013-10-20"), // Date | 
  'order': "order_example", // String | 
  'asc': "asc_example" // String | 
};
apiInstance.getCampaignHistory(id, opts, (error, data, response) => {
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
 **limit** | **Number**| Max number of elements in response | [optional] 
 **offset** | **Number**| Offset of data in response (skip X elements) | [optional] 
 **before** | **Date**|  | [optional] 
 **after** | **Date**|  | [optional] 
 **order** | **String**|  | [optional] 
 **asc** | **String**|  | [optional] 

### Return type

[**GetCampaignHistory200Response**](GetCampaignHistory200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

