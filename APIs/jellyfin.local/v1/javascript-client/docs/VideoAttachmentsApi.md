# JellyfinApi.VideoAttachmentsApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAttachment**](VideoAttachmentsApi.md#getAttachment) | **GET** /Videos/{videoId}/{mediaSourceId}/Attachments/{index} | Get video attachment.



## getAttachment

> File getAttachment(videoId, mediaSourceId, index)

Get video attachment.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.VideoAttachmentsApi();
let videoId = "videoId_example"; // String | Video ID.
let mediaSourceId = "mediaSourceId_example"; // String | Media Source ID.
let index = 56; // Number | Attachment Index.
apiInstance.getAttachment(videoId, mediaSourceId, index, (error, data, response) => {
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
 **videoId** | **String**| Video ID. | 
 **mediaSourceId** | **String**| Media Source ID. | 
 **index** | **Number**| Attachment Index. | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase

