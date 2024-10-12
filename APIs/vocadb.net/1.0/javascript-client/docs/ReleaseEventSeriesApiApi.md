# VocaDbWeb.ReleaseEventSeriesApiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiReleaseEventSeriesGet**](ReleaseEventSeriesApiApi.md#apiReleaseEventSeriesGet) | **GET** /api/releaseEventSeries | 
[**apiReleaseEventSeriesIdDelete**](ReleaseEventSeriesApiApi.md#apiReleaseEventSeriesIdDelete) | **DELETE** /api/releaseEventSeries/{id} | 
[**apiReleaseEventSeriesIdForEditGet**](ReleaseEventSeriesApiApi.md#apiReleaseEventSeriesIdForEditGet) | **GET** /api/releaseEventSeries/{id}/for-edit | 
[**apiReleaseEventSeriesIdGet**](ReleaseEventSeriesApiApi.md#apiReleaseEventSeriesIdGet) | **GET** /api/releaseEventSeries/{id} | 



## apiReleaseEventSeriesGet

> ReleaseEventSeriesForApiContractPartialFindResult apiReleaseEventSeriesGet(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.ReleaseEventSeriesApiApi();
let opts = {
  'query': "''", // String | 
  'fields': new VocaDbWeb.ReleaseEventSeriesOptionalFields(), // ReleaseEventSeriesOptionalFields | 
  'start': 0, // Number | 
  'maxResults': 10, // Number | 
  'getTotalCount': false, // Boolean | 
  'nameMatchMode': new VocaDbWeb.NameMatchMode(), // NameMatchMode | 
  'lang': new VocaDbWeb.ContentLanguagePreference() // ContentLanguagePreference | 
};
apiInstance.apiReleaseEventSeriesGet(opts, (error, data, response) => {
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
 **fields** | [**ReleaseEventSeriesOptionalFields**](.md)|  | [optional] 
 **start** | **Number**|  | [optional] [default to 0]
 **maxResults** | **Number**|  | [optional] [default to 10]
 **getTotalCount** | **Boolean**|  | [optional] [default to false]
 **nameMatchMode** | [**NameMatchMode**](.md)|  | [optional] 
 **lang** | [**ContentLanguagePreference**](.md)|  | [optional] 

### Return type

[**ReleaseEventSeriesForApiContractPartialFindResult**](ReleaseEventSeriesForApiContractPartialFindResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiReleaseEventSeriesIdDelete

> apiReleaseEventSeriesIdDelete(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.ReleaseEventSeriesApiApi();
let id = 56; // Number | 
let opts = {
  'notes': "''", // String | 
  'hardDelete': false // Boolean | 
};
apiInstance.apiReleaseEventSeriesIdDelete(id, opts, (error, data, response) => {
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


## apiReleaseEventSeriesIdForEditGet

> ReleaseEventSeriesForEditForApiContract apiReleaseEventSeriesIdForEditGet(id)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.ReleaseEventSeriesApiApi();
let id = 56; // Number | 
apiInstance.apiReleaseEventSeriesIdForEditGet(id, (error, data, response) => {
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

### Return type

[**ReleaseEventSeriesForEditForApiContract**](ReleaseEventSeriesForEditForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiReleaseEventSeriesIdGet

> ReleaseEventSeriesForApiContract apiReleaseEventSeriesIdGet(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.ReleaseEventSeriesApiApi();
let id = 56; // Number | 
let opts = {
  'fields': new VocaDbWeb.ReleaseEventSeriesOptionalFields(), // ReleaseEventSeriesOptionalFields | 
  'lang': new VocaDbWeb.ContentLanguagePreference() // ContentLanguagePreference | 
};
apiInstance.apiReleaseEventSeriesIdGet(id, opts, (error, data, response) => {
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
 **fields** | [**ReleaseEventSeriesOptionalFields**](.md)|  | [optional] 
 **lang** | [**ContentLanguagePreference**](.md)|  | [optional] 

### Return type

[**ReleaseEventSeriesForApiContract**](ReleaseEventSeriesForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

