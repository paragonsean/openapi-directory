# FastApi.DiscordApi

All URIs are relative to *http://botschaft.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**discordGetDiscordGet**](DiscordApi.md#discordGetDiscordGet) | **GET** /discord | Discord Get
[**discordPostDiscordPost**](DiscordApi.md#discordPostDiscordPost) | **POST** /discord | Discord Post



## discordGetDiscordGet

> Object discordGetDiscordGet(channel, opts)

Discord Get

### Example

```javascript
import FastApi from 'fast_api';

let apiInstance = new FastApi.DiscordApi();
let channel = "channel_example"; // String | 
let opts = {
  'message': "message_example", // String | 
  'base64Message': "base64Message_example", // String | 
  'authorization': "authorization_example" // String | 
};
apiInstance.discordGetDiscordGet(channel, opts, (error, data, response) => {
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
 **channel** | **String**|  | 
 **message** | **String**|  | [optional] 
 **base64Message** | **String**|  | [optional] 
 **authorization** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## discordPostDiscordPost

> Object discordPostDiscordPost(discordMessageRequest, opts)

Discord Post

### Example

```javascript
import FastApi from 'fast_api';

let apiInstance = new FastApi.DiscordApi();
let discordMessageRequest = new FastApi.DiscordMessageRequest(); // DiscordMessageRequest | 
let opts = {
  'authorization': "authorization_example" // String | 
};
apiInstance.discordPostDiscordPost(discordMessageRequest, opts, (error, data, response) => {
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
 **discordMessageRequest** | [**DiscordMessageRequest**](DiscordMessageRequest.md)|  | 
 **authorization** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

