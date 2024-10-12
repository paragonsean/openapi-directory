# BbcIPlayerBusinessLayer.ChannelsApi

All URIs are relative to *https://ibl.api.bbci.co.uk/ibl/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getChannels**](ChannelsApi.md#getChannels) | **GET** /channels | List all the channels.
[**getHighlightsByChannel**](ChannelsApi.md#getHighlightsByChannel) | **GET** /channels/{channel}/highlights | List the highlights for a channel.
[**getScheduleByChannel**](ChannelsApi.md#getScheduleByChannel) | **GET** /channels/{channel}/schedule/{date} | Get schedule by channel



## getChannels

> Object getChannels(lang, opts)

List all the channels.

Get the list of all the channels TV &amp; iPlayer.

### Example

```javascript
import BbcIPlayerBusinessLayer from 'bbc_i_player_business_layer';

let apiInstance = new BbcIPlayerBusinessLayer.ChannelsApi();
let lang = "lang_example"; // String | The language for any applicable localised strings.
let opts = {
  'region': "region_example" // String | The region to get the channels for.
};
apiInstance.getChannels(lang, opts, (error, data, response) => {
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
 **lang** | **String**| The language for any applicable localised strings. | 
 **region** | **String**| The region to get the channels for. | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getHighlightsByChannel

> Object getHighlightsByChannel(channel, lang, rights, availability, opts)

List the highlights for a channel.

Get the editorial highlights of a given channel in TV &amp; iPlayer.

### Example

```javascript
import BbcIPlayerBusinessLayer from 'bbc_i_player_business_layer';

let apiInstance = new BbcIPlayerBusinessLayer.ChannelsApi();
let channel = "channel_example"; // String | The channel identifier to limit results to.
let lang = "lang_example"; // String | The language for any applicable localised strings.
let rights = "'web'"; // String | The rights group to limit results to.
let availability = "'available'"; // String | Whether to return all, or available programmes
let opts = {
  'live': true, // Boolean | Whether to include live programmes
  'mixin': ["null"] // [String] | Request additional data in the output
};
apiInstance.getHighlightsByChannel(channel, lang, rights, availability, opts, (error, data, response) => {
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
 **channel** | **String**| The channel identifier to limit results to. | 
 **lang** | **String**| The language for any applicable localised strings. | 
 **rights** | **String**| The rights group to limit results to. | [default to &#39;web&#39;]
 **availability** | **String**| Whether to return all, or available programmes | [default to &#39;available&#39;]
 **live** | **Boolean**| Whether to include live programmes | [optional] 
 **mixin** | [**[String]**](String.md)| Request additional data in the output | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getScheduleByChannel

> Object getScheduleByChannel(channel, date, lang, rights, availability)

Get schedule by channel

Get schedule by channel

### Example

```javascript
import BbcIPlayerBusinessLayer from 'bbc_i_player_business_layer';

let apiInstance = new BbcIPlayerBusinessLayer.ChannelsApi();
let channel = "channel_example"; // String | The channel identifier to limit results to.
let date = "date_example"; // String | The date to return the schedule for, yyyy-mm-dd format
let lang = "lang_example"; // String | The language for any applicable localised strings.
let rights = "'web'"; // String | The rights group to limit results to.
let availability = "'available'"; // String | Whether to return all, or available programmes
apiInstance.getScheduleByChannel(channel, date, lang, rights, availability, (error, data, response) => {
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
 **channel** | **String**| The channel identifier to limit results to. | 
 **date** | **String**| The date to return the schedule for, yyyy-mm-dd format | 
 **lang** | **String**| The language for any applicable localised strings. | 
 **rights** | **String**| The rights group to limit results to. | [default to &#39;web&#39;]
 **availability** | **String**| Whether to return all, or available programmes | [default to &#39;available&#39;]

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

