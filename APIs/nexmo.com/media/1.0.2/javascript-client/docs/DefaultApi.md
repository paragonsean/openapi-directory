# MediaApi.DefaultApi

All URIs are relative to *https://api.nexmo.com/v3/media*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteAMediaItem**](DefaultApi.md#deleteAMediaItem) | **DELETE** /:id | Delete a media item
[**listAndSearchMediaItems**](DefaultApi.md#listAndSearchMediaItems) | **GET** / | List and search media items
[**retrieveAMediaItem**](DefaultApi.md#retrieveAMediaItem) | **GET** /:id/info | Retrieve a media item
[**updateAMediaItem**](DefaultApi.md#updateAMediaItem) | **PUT** /:id/info | Update a media item



## deleteAMediaItem

> deleteAMediaItem()

Delete a media item

Delete a previously created media item by ID.

### Example

```javascript
import MediaApi from 'media_api';

let apiInstance = new MediaApi.DefaultApi();
apiInstance.deleteAMediaItem((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listAndSearchMediaItems

> ListAndSearchMediaItems200Response listAndSearchMediaItems(opts)

List and search media items

Retrieve information about multiple media items with the ability to search and paginate.

### Example

```javascript
import MediaApi from 'media_api';

let apiInstance = new MediaApi.DefaultApi();
let opts = {
  'order': "ascending", // String | The order of search results.
  'pageIndex': 1, // Number | Which page to retrieve in pagination
  'pageSize': 50, // Number | How many items at most per page
  'startTime': "2020-01-01T14:00:00.000Z", // String | Retrieve results created on or after this timestap.
  'endTime': "2020-01-01T14:00:00.000Z" // String | Retrieve results created on or before this timestamp.
};
apiInstance.listAndSearchMediaItems(opts, (error, data, response) => {
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
 **order** | **String**| The order of search results. | [optional] [default to &#39;descending&#39;]
 **pageIndex** | **Number**| Which page to retrieve in pagination | [optional] [default to 0]
 **pageSize** | **Number**| How many items at most per page | [optional] [default to 20]
 **startTime** | **String**| Retrieve results created on or after this timestap. | [optional] [default to &#39;1 week ago&#39;]
 **endTime** | **String**| Retrieve results created on or before this timestamp. | [optional] 

### Return type

[**ListAndSearchMediaItems200Response**](ListAndSearchMediaItems200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveAMediaItem

> Media retrieveAMediaItem()

Retrieve a media item

Retrieve information about a single media item

### Example

```javascript
import MediaApi from 'media_api';

let apiInstance = new MediaApi.DefaultApi();
apiInstance.retrieveAMediaItem((error, data, response) => {
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

[**Media**](Media.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateAMediaItem

> updateAMediaItem(opts)

Update a media item

Update a previously created media item by ID.

### Example

```javascript
import MediaApi from 'media_api';

let apiInstance = new MediaApi.DefaultApi();
let opts = {
  'description': "description_example", // String | A description of the media file.
  'maxDownloadsAllowed': 56, // Number | The maximum number of times the file may be downloaded. Unlimited when not provided.
  'metadataPrimary': "metadataPrimary_example", // String | A string containing metadata about the media file.
  'metadataSecondary': "metadataSecondary_example", // String | A string containing further metadata about the media file.
  'mimeType': "mimeType_example", // String | The MIME type of the media file.
  '_public': true, // Boolean | Whether the item is publicly available without authentication.
  'title': "title_example" // String | A string containing a title for the media file.
};
apiInstance.updateAMediaItem(opts, (error, data, response) => {
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
 **description** | **String**| A description of the media file. | [optional] 
 **maxDownloadsAllowed** | **Number**| The maximum number of times the file may be downloaded. Unlimited when not provided. | [optional] 
 **metadataPrimary** | **String**| A string containing metadata about the media file. | [optional] 
 **metadataSecondary** | **String**| A string containing further metadata about the media file. | [optional] 
 **mimeType** | **String**| The MIME type of the media file. | [optional] 
 **_public** | **Boolean**| Whether the item is publicly available without authentication. | [optional] 
 **title** | **String**| A string containing a title for the media file. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined

