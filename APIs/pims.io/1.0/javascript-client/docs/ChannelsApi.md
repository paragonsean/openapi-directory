# Pims.ChannelsApi

All URIs are relative to *https://demo.pims.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchAllChannels**](ChannelsApi.md#fetchAllChannels) | **GET** /channels | Find all channels
[**fetchAllEventsChannels**](ChannelsApi.md#fetchAllEventsChannels) | **GET** /events/{event_id}/channels | Find all channels for one event
[**fetchOneChannel**](ChannelsApi.md#fetchOneChannel) | **GET** /channels/{channel_id} | Get one channel by ID
[**fetchOneEventChannel**](ChannelsApi.md#fetchOneEventChannel) | **GET** /events/{event_id}/channels/{channel_id} | Get one event channel by ID



## fetchAllChannels

> [ChannelsEntity] fetchAllChannels(opts)

Find all channels

### Example

```javascript
import Pims from 'pims';
let defaultClient = Pims.ApiClient.instance;
// Configure HTTP basic authorization: Basic Auth
let Basic Auth = defaultClient.authentications['Basic Auth'];
Basic Auth.username = 'YOUR USERNAME';
Basic Auth.password = 'YOUR PASSWORD';

let apiInstance = new Pims.ChannelsApi();
let opts = {
  'label': "label_example", // String | Find only the channels whose label contains this value.
  'showIgnored': false, // Boolean | If set to `false`, show only the channels which are not ignored. If set to `true`, show all channels.
  'sort': "'label'", // String | Sort the channels in the corresponding order.
  'pageSize': 25, // Number | Pagination size, i.e. maximum number of items to be displayed in the response.
  'acceptLanguage': "'en'" // String | Language used for the translatable labels.
};
apiInstance.fetchAllChannels(opts, (error, data, response) => {
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
 **label** | **String**| Find only the channels whose label contains this value. | [optional] 
 **showIgnored** | **Boolean**| If set to &#x60;false&#x60;, show only the channels which are not ignored. If set to &#x60;true&#x60;, show all channels. | [optional] [default to false]
 **sort** | **String**| Sort the channels in the corresponding order. | [optional] [default to &#39;label&#39;]
 **pageSize** | **Number**| Pagination size, i.e. maximum number of items to be displayed in the response. | [optional] [default to 25]
 **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to &#39;en&#39;]

### Return type

[**[ChannelsEntity]**](ChannelsEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json


## fetchAllEventsChannels

> [EventsChannelsEntity] fetchAllEventsChannels(eventId, opts)

Find all channels for one event

### Example

```javascript
import Pims from 'pims';
let defaultClient = Pims.ApiClient.instance;
// Configure HTTP basic authorization: Basic Auth
let Basic Auth = defaultClient.authentications['Basic Auth'];
Basic Auth.username = 'YOUR USERNAME';
Basic Auth.password = 'YOUR PASSWORD';

let apiInstance = new Pims.ChannelsApi();
let eventId = 56; // Number | ID of the targeted event.
let opts = {
  'showIgnored': false, // Boolean | If set to `false`, show only the [event-]channels which are not ignored. If set to `true`, show everything.
  'pageSize': 25 // Number | Pagination size, i.e. maximum number of items to be displayed in the response.
};
apiInstance.fetchAllEventsChannels(eventId, opts, (error, data, response) => {
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
 **eventId** | **Number**| ID of the targeted event. | 
 **showIgnored** | **Boolean**| If set to &#x60;false&#x60;, show only the [event-]channels which are not ignored. If set to &#x60;true&#x60;, show everything. | [optional] [default to false]
 **pageSize** | **Number**| Pagination size, i.e. maximum number of items to be displayed in the response. | [optional] [default to 25]

### Return type

[**[EventsChannelsEntity]**](EventsChannelsEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json


## fetchOneChannel

> ChannelsEntity fetchOneChannel(channelId, opts)

Get one channel by ID

### Example

```javascript
import Pims from 'pims';
let defaultClient = Pims.ApiClient.instance;
// Configure HTTP basic authorization: Basic Auth
let Basic Auth = defaultClient.authentications['Basic Auth'];
Basic Auth.username = 'YOUR USERNAME';
Basic Auth.password = 'YOUR PASSWORD';

let apiInstance = new Pims.ChannelsApi();
let channelId = 56; // Number | ID of the targeted channel.
let opts = {
  'acceptLanguage': "'en'" // String | Language used for the translatable labels.
};
apiInstance.fetchOneChannel(channelId, opts, (error, data, response) => {
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
 **channelId** | **Number**| ID of the targeted channel. | 
 **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to &#39;en&#39;]

### Return type

[**ChannelsEntity**](ChannelsEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json


## fetchOneEventChannel

> EventsChannelsEntity fetchOneEventChannel(eventId, channelId)

Get one event channel by ID

### Example

```javascript
import Pims from 'pims';
let defaultClient = Pims.ApiClient.instance;
// Configure HTTP basic authorization: Basic Auth
let Basic Auth = defaultClient.authentications['Basic Auth'];
Basic Auth.username = 'YOUR USERNAME';
Basic Auth.password = 'YOUR PASSWORD';

let apiInstance = new Pims.ChannelsApi();
let eventId = 56; // Number | ID of the targeted event.
let channelId = 56; // Number | ID of the targeted event channel.
apiInstance.fetchOneEventChannel(eventId, channelId, (error, data, response) => {
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
 **eventId** | **Number**| ID of the targeted event. | 
 **channelId** | **Number**| ID of the targeted event channel. | 

### Return type

[**EventsChannelsEntity**](EventsChannelsEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json

