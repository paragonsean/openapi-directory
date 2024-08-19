# BandsintownApi.ArtistInformationApi

All URIs are relative to *https://rest.bandsintown.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**artist**](ArtistInformationApi.md#artist) | **GET** /artists/{artistname} | Get artist information



## artist

> ArtistData artist(artistname, appId)

Get artist information

Get artist information 

### Example

```javascript
import BandsintownApi from 'bandsintown_api';

let apiInstance = new BandsintownApi.ArtistInformationApi();
let artistname = "artistname_example"; // String | The name of the artist. If it contains one of the special characters below, please be sure to replace it by the corresponding code: for / use %252F, for ? use %253F, for * use %252A, and for \" use %27C
let appId = "appId_example"; // String | The application ID assigned to you by Bandsintown
apiInstance.artist(artistname, appId, (error, data, response) => {
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
 **artistname** | **String**| The name of the artist. If it contains one of the special characters below, please be sure to replace it by the corresponding code: for / use %252F, for ? use %253F, for * use %252A, and for \&quot; use %27C | 
 **appId** | **String**| The application ID assigned to you by Bandsintown | 

### Return type

[**ArtistData**](ArtistData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

