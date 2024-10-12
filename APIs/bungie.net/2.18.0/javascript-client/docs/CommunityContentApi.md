# BungieNetApi.CommunityContentApi

All URIs are relative to *https://www.bungie.net/Platform*

Method | HTTP request | Description
------------- | ------------- | -------------
[**communityContentGetCommunityContent**](CommunityContentApi.md#communityContentGetCommunityContent) | **GET** /CommunityContent/Get/{sort}/{mediaFilter}/{page}/ | 



## communityContentGetCommunityContent

> CommunityContentGetCommunityContent200Response communityContentGetCommunityContent(mediaFilter, page, sort)



Returns community content.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.CommunityContentApi();
let mediaFilter = 56; // Number | The type of media to get
let page = 56; // Number | Zero based page
let sort = 56; // Number | The sort mode.
apiInstance.communityContentGetCommunityContent(mediaFilter, page, sort, (error, data, response) => {
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
 **mediaFilter** | **Number**| The type of media to get | 
 **page** | **Number**| Zero based page | 
 **sort** | **Number**| The sort mode. | 

### Return type

[**CommunityContentGetCommunityContent200Response**](CommunityContentGetCommunityContent200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

