# AkeneoPimRestApi.ChannelApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**channelsPatch**](ChannelApi.md#channelsPatch) | **PATCH** /api/rest/v1/channels/{code} | Update/create a channel
[**channelsPost**](ChannelApi.md#channelsPost) | **POST** /api/rest/v1/channels | Create a new channel
[**getChannels**](ChannelApi.md#getChannels) | **GET** /api/rest/v1/channels | Get a list of channels
[**getChannelsCode**](ChannelApi.md#getChannelsCode) | **GET** /api/rest/v1/channels/{code} | Get a channel
[**severalChannelsPatch**](ChannelApi.md#severalChannelsPatch) | **PATCH** /api/rest/v1/channels | Update/create several channels



## channelsPatch

> channelsPatch(code, body)

Update/create a channel

This endpoint allows you to update a given channel. Know more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no channel exists for the given code, it creates it.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ChannelApi();
let code = "code_example"; // String | Code of the resource
let body = new AkeneoPimRestApi.ChannelsPostRequest(); // ChannelsPostRequest | 
apiInstance.channelsPatch(code, body, (error, data, response) => {
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
 **code** | **String**| Code of the resource | 
 **body** | [**ChannelsPostRequest**](ChannelsPostRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links


## channelsPost

> channelsPost(opts)

Create a new channel

This endpoint allows you to create a new channel.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ChannelApi();
let opts = {
  'body': new AkeneoPimRestApi.ChannelsPostRequest() // ChannelsPostRequest | 
};
apiInstance.channelsPost(opts, (error, data, response) => {
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
 **body** | [**ChannelsPostRequest**](ChannelsPostRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links


## getChannels

> Channels getChannels(opts)

Get a list of channels

This endpoint allows you to get a list of channels. Channels are paginated and sorted by code.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ChannelApi();
let opts = {
  'page': 1, // Number | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section
  'limit': 10, // Number | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
  'withCount': false // Boolean | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
};
apiInstance.getChannels(opts, (error, data, response) => {
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
 **page** | **Number**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1]
 **limit** | **Number**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10]
 **withCount** | **Boolean**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false]

### Return type

[**Channels**](Channels.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, _embedded, _links, current_page, code, message


## getChannelsCode

> ChannelsPostRequest getChannelsCode(code)

Get a channel

This endpoint allows you to get the information about a given channel.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ChannelApi();
let code = "code_example"; // String | Code of the resource
apiInstance.getChannelsCode(code, (error, data, response) => {
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
 **code** | **String**| Code of the resource | 

### Return type

[**ChannelsPostRequest**](ChannelsPostRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## severalChannelsPatch

> PatchAssetCategories200Response severalChannelsPatch(opts)

Update/create several channels

This endpoint allows you to update and/or create several channels at once.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ChannelApi();
let opts = {
  'body': new AkeneoPimRestApi.SeveralChannelsPatchRequest() // SeveralChannelsPatchRequest | 
};
apiInstance.severalChannelsPatch(opts, (error, data, response) => {
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
 **body** | [**SeveralChannelsPatchRequest**](SeveralChannelsPatchRequest.md)|  | [optional] 

### Return type

[**PatchAssetCategories200Response**](PatchAssetCategories200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, x-example-1, x-example-2, x-example-3, code, message

