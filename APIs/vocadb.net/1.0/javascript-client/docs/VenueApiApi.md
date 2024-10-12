# VocaDbWeb.VenueApiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiVenuesGet**](VenueApiApi.md#apiVenuesGet) | **GET** /api/venues | 
[**apiVenuesIdDelete**](VenueApiApi.md#apiVenuesIdDelete) | **DELETE** /api/venues/{id} | 
[**apiVenuesIdReportsPost**](VenueApiApi.md#apiVenuesIdReportsPost) | **POST** /api/venues/{id}/reports | 



## apiVenuesGet

> VenueForApiContractPartialFindResult apiVenuesGet(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.VenueApiApi();
let opts = {
  'query': "''", // String | 
  'fields': new VocaDbWeb.VenueOptionalFields(), // VenueOptionalFields | 
  'start': 0, // Number | 
  'maxResults': 10, // Number | 
  'getTotalCount': false, // Boolean | 
  'nameMatchMode': new VocaDbWeb.NameMatchMode(), // NameMatchMode | 
  'lang': new VocaDbWeb.ContentLanguagePreference(), // ContentLanguagePreference | 
  'sortRule': new VocaDbWeb.VenueSortRule(), // VenueSortRule | 
  'latitude': 3.4, // Number | 
  'longitude': 3.4, // Number | 
  'radius': 3.4, // Number | 
  'distanceUnit': new VocaDbWeb.DistanceUnit() // DistanceUnit | 
};
apiInstance.apiVenuesGet(opts, (error, data, response) => {
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
 **fields** | [**VenueOptionalFields**](.md)|  | [optional] 
 **start** | **Number**|  | [optional] [default to 0]
 **maxResults** | **Number**|  | [optional] [default to 10]
 **getTotalCount** | **Boolean**|  | [optional] [default to false]
 **nameMatchMode** | [**NameMatchMode**](.md)|  | [optional] 
 **lang** | [**ContentLanguagePreference**](.md)|  | [optional] 
 **sortRule** | [**VenueSortRule**](.md)|  | [optional] 
 **latitude** | **Number**|  | [optional] 
 **longitude** | **Number**|  | [optional] 
 **radius** | **Number**|  | [optional] 
 **distanceUnit** | [**DistanceUnit**](.md)|  | [optional] 

### Return type

[**VenueForApiContractPartialFindResult**](VenueForApiContractPartialFindResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiVenuesIdDelete

> apiVenuesIdDelete(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.VenueApiApi();
let id = 56; // Number | 
let opts = {
  'notes': "''", // String | 
  'hardDelete': false // Boolean | 
};
apiInstance.apiVenuesIdDelete(id, opts, (error, data, response) => {
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


## apiVenuesIdReportsPost

> apiVenuesIdReportsPost(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.VenueApiApi();
let id = 56; // Number | 
let opts = {
  'reportType': new VocaDbWeb.VenueReportType(), // VenueReportType | 
  'notes': "notes_example", // String | 
  'versionNumber': 56 // Number | 
};
apiInstance.apiVenuesIdReportsPost(id, opts, (error, data, response) => {
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
 **reportType** | [**VenueReportType**](.md)|  | [optional] 
 **notes** | **String**|  | [optional] 
 **versionNumber** | **Number**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

