# GeocoderRestApi.ParcelsApi

All URIs are relative to *https://geocoder.api.gov.bc.ca*

Method | HTTP request | Description
------------- | ------------- | -------------
[**parcelsPidsSiteIDOutputFormatGet**](ParcelsApi.md#parcelsPidsSiteIDOutputFormatGet) | **GET** /parcels/pids/{siteID}.{outputFormat} | Get a comma-separated string of all pids for a given site



## parcelsPidsSiteIDOutputFormatGet

> parcelsPidsSiteIDOutputFormatGet(siteID, outputFormat)

Get a comma-separated string of all pids for a given site

Represents all parcel identifiers associated with an individual site

### Example

```javascript
import GeocoderRestApi from 'geocoder_rest_api';
let defaultClient = GeocoderRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new GeocoderRestApi.ParcelsApi();
let siteID = "siteID_example"; // String | A unique, but not immutable, site identifier.
let outputFormat = "json"; // String | Results format. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputFormat target=\"_blank\">outputFormat</a>.   Note: GeoJSON and KML formats only support EPSG:4326 (outputSRS=4326)
apiInstance.parcelsPidsSiteIDOutputFormatGet(siteID, outputFormat, (error, data, response) => {
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
 **siteID** | **String**| A unique, but not immutable, site identifier. | 
 **outputFormat** | **String**| Results format. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputFormat target&#x3D;\&quot;_blank\&quot;&gt;outputFormat&lt;/a&gt;.   Note: GeoJSON and KML formats only support EPSG:4326 (outputSRS&#x3D;4326) | [default to &#39;json&#39;]

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

