# VocaDbWeb.ReleaseEventApiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiReleaseEventsEventIdAlbumsGet**](ReleaseEventApiApi.md#apiReleaseEventsEventIdAlbumsGet) | **GET** /api/releaseEvents/{eventId}/albums | 
[**apiReleaseEventsEventIdPublishedSongsGet**](ReleaseEventApiApi.md#apiReleaseEventsEventIdPublishedSongsGet) | **GET** /api/releaseEvents/{eventId}/published-songs | 
[**apiReleaseEventsEventIdReportsPost**](ReleaseEventApiApi.md#apiReleaseEventsEventIdReportsPost) | **POST** /api/releaseEvents/{eventId}/reports | 
[**apiReleaseEventsGet**](ReleaseEventApiApi.md#apiReleaseEventsGet) | **GET** /api/releaseEvents | 
[**apiReleaseEventsIdDelete**](ReleaseEventApiApi.md#apiReleaseEventsIdDelete) | **DELETE** /api/releaseEvents/{id} | 
[**apiReleaseEventsIdGet**](ReleaseEventApiApi.md#apiReleaseEventsIdGet) | **GET** /api/releaseEvents/{id} | 
[**apiReleaseEventsNamesGet**](ReleaseEventApiApi.md#apiReleaseEventsNamesGet) | **GET** /api/releaseEvents/names | 



## apiReleaseEventsEventIdAlbumsGet

> [AlbumForApiContract] apiReleaseEventsEventIdAlbumsGet(eventId, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.ReleaseEventApiApi();
let eventId = 56; // Number | 
let opts = {
  'fields': new VocaDbWeb.AlbumOptionalFields(), // AlbumOptionalFields | 
  'lang': new VocaDbWeb.ContentLanguagePreference() // ContentLanguagePreference | 
};
apiInstance.apiReleaseEventsEventIdAlbumsGet(eventId, opts, (error, data, response) => {
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
 **eventId** | **Number**|  | 
 **fields** | [**AlbumOptionalFields**](.md)|  | [optional] 
 **lang** | [**ContentLanguagePreference**](.md)|  | [optional] 

### Return type

[**[AlbumForApiContract]**](AlbumForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiReleaseEventsEventIdPublishedSongsGet

> [SongForApiContract] apiReleaseEventsEventIdPublishedSongsGet(eventId, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.ReleaseEventApiApi();
let eventId = 56; // Number | 
let opts = {
  'fields': new VocaDbWeb.SongOptionalFields(), // SongOptionalFields | 
  'lang': new VocaDbWeb.ContentLanguagePreference() // ContentLanguagePreference | 
};
apiInstance.apiReleaseEventsEventIdPublishedSongsGet(eventId, opts, (error, data, response) => {
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
 **eventId** | **Number**|  | 
 **fields** | [**SongOptionalFields**](.md)|  | [optional] 
 **lang** | [**ContentLanguagePreference**](.md)|  | [optional] 

### Return type

[**[SongForApiContract]**](SongForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiReleaseEventsEventIdReportsPost

> apiReleaseEventsEventIdReportsPost(eventId, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.ReleaseEventApiApi();
let eventId = 56; // Number | 
let opts = {
  'reportType': new VocaDbWeb.EventReportType(), // EventReportType | 
  'notes': "notes_example", // String | 
  'versionNumber': 56 // Number | 
};
apiInstance.apiReleaseEventsEventIdReportsPost(eventId, opts, (error, data, response) => {
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
 **eventId** | **Number**|  | 
 **reportType** | [**EventReportType**](.md)|  | [optional] 
 **notes** | **String**|  | [optional] 
 **versionNumber** | **Number**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiReleaseEventsGet

> ReleaseEventForApiContractPartialFindResult apiReleaseEventsGet(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.ReleaseEventApiApi();
let opts = {
  'query': "''", // String | 
  'nameMatchMode': new VocaDbWeb.NameMatchMode(), // NameMatchMode | 
  'seriesId': 0, // Number | 
  'afterDate': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'beforeDate': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'category': new VocaDbWeb.EventCategory(), // EventCategory | 
  'userCollectionId': 56, // Number | 
  'tagId': [null], // [Number] | 
  'childTags': false, // Boolean | 
  'artistId': [null], // [Number] | 
  'childVoicebanks': false, // Boolean | 
  'includeMembers': false, // Boolean | 
  'status': new VocaDbWeb.EntryStatus(), // EntryStatus | 
  'start': 0, // Number | 
  'maxResults': 10, // Number | 
  'getTotalCount': false, // Boolean | 
  'sort': new VocaDbWeb.EventSortRule(), // EventSortRule | 
  'fields': new VocaDbWeb.ReleaseEventOptionalFields(), // ReleaseEventOptionalFields | 
  'lang': new VocaDbWeb.ContentLanguagePreference(), // ContentLanguagePreference | 
  'sortDirection': new VocaDbWeb.SortDirection() // SortDirection | 
};
apiInstance.apiReleaseEventsGet(opts, (error, data, response) => {
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
 **query** | **String**|  | [optional] [default to &#39;&#39;]
 **nameMatchMode** | [**NameMatchMode**](.md)|  | [optional] 
 **seriesId** | **Number**|  | [optional] [default to 0]
 **afterDate** | **Date**|  | [optional] 
 **beforeDate** | **Date**|  | [optional] 
 **category** | [**EventCategory**](.md)|  | [optional] 
 **userCollectionId** | **Number**|  | [optional] 
 **tagId** | [**[Number]**](Number.md)|  | [optional] 
 **childTags** | **Boolean**|  | [optional] [default to false]
 **artistId** | [**[Number]**](Number.md)|  | [optional] 
 **childVoicebanks** | **Boolean**|  | [optional] [default to false]
 **includeMembers** | **Boolean**|  | [optional] [default to false]
 **status** | [**EntryStatus**](.md)|  | [optional] 
 **start** | **Number**|  | [optional] [default to 0]
 **maxResults** | **Number**|  | [optional] [default to 10]
 **getTotalCount** | **Boolean**|  | [optional] [default to false]
 **sort** | [**EventSortRule**](.md)|  | [optional] 
 **fields** | [**ReleaseEventOptionalFields**](.md)|  | [optional] 
 **lang** | [**ContentLanguagePreference**](.md)|  | [optional] 
 **sortDirection** | [**SortDirection**](.md)|  | [optional] 

### Return type

[**ReleaseEventForApiContractPartialFindResult**](ReleaseEventForApiContractPartialFindResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiReleaseEventsIdDelete

> apiReleaseEventsIdDelete(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.ReleaseEventApiApi();
let id = 56; // Number | 
let opts = {
  'notes': "''", // String | 
  'hardDelete': false // Boolean | 
};
apiInstance.apiReleaseEventsIdDelete(id, opts, (error, data, response) => {
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
 **id** | **Number**|  | 
 **notes** | **String**|  | [optional] [default to &#39;&#39;]
 **hardDelete** | **Boolean**|  | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiReleaseEventsIdGet

> ReleaseEventForApiContract apiReleaseEventsIdGet(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.ReleaseEventApiApi();
let id = 56; // Number | 
let opts = {
  'fields': new VocaDbWeb.ReleaseEventOptionalFields(), // ReleaseEventOptionalFields | 
  'lang': new VocaDbWeb.ContentLanguagePreference() // ContentLanguagePreference | 
};
apiInstance.apiReleaseEventsIdGet(id, opts, (error, data, response) => {
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
 **id** | **Number**|  | 
 **fields** | [**ReleaseEventOptionalFields**](.md)|  | [optional] 
 **lang** | [**ContentLanguagePreference**](.md)|  | [optional] 

### Return type

[**ReleaseEventForApiContract**](ReleaseEventForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiReleaseEventsNamesGet

> [String] apiReleaseEventsNamesGet(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.ReleaseEventApiApi();
let opts = {
  'query': "''", // String | 
  'maxResults': 10 // Number | 
};
apiInstance.apiReleaseEventsNamesGet(opts, (error, data, response) => {
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
 **query** | **String**|  | [optional] [default to &#39;&#39;]
 **maxResults** | **Number**|  | [optional] [default to 10]

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

