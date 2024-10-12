# RadioMusicServices.MusicExportApi

All URIs are relative to *https://rms.api.bbc.co.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteMusicPreferencesExport**](MusicExportApi.md#deleteMusicPreferencesExport) | **DELETE** /my/music/preferences/export | Music Export Preferences
[**deleteMusicPreferencesExportVendor**](MusicExportApi.md#deleteMusicPreferencesExportVendor) | **DELETE** /my/music/preferences/export/{vendor} | Music Export Vendor Preferences
[**getMusicExport**](MusicExportApi.md#getMusicExport) | **GET** /my/music/export | Music Exports
[**getMusicExportJobs**](MusicExportApi.md#getMusicExportJobs) | **GET** /my/music/exports/jobs | Music Export Jobs
[**getMusicExportTracks**](MusicExportApi.md#getMusicExportTracks) | **GET** /my/music/exports/tracks | Music Export Tracks
[**getMusicPreferencesExport**](MusicExportApi.md#getMusicPreferencesExport) | **GET** /my/music/preferences/export | Music Export Preferences
[**getMusicPreferencesExportVendor**](MusicExportApi.md#getMusicPreferencesExportVendor) | **GET** /my/music/preferences/export/{vendor} | Music Export Vendor Preferences
[**postMusicExportJob**](MusicExportApi.md#postMusicExportJob) | **POST** /my/music/exports/jobs | Music Export Jobs
[**postMusicPreferencesExport**](MusicExportApi.md#postMusicPreferencesExport) | **POST** /my/music/preferences/export | Music Export Preferences
[**postMusicPreferencesExportVendor**](MusicExportApi.md#postMusicPreferencesExportVendor) | **POST** /my/music/preferences/export/{vendor} | Music Export Vendor Preferences
[**putMusicPreferencesExportVendor**](MusicExportApi.md#putMusicPreferencesExportVendor) | **PUT** /my/music/preferences/export/{vendor} | Music Export Vendor Preferences



## deleteMusicPreferencesExport

> MusicExportSuccess deleteMusicPreferencesExport(authorization, xAuthenticationProvider, xAPIKey)

Music Export Preferences

Remove export preferences (e.g. 3rd party vendors, partner id&#39;s) for a given BBC Music user. 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicExportApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
apiInstance.deleteMusicPreferencesExport(authorization, xAuthenticationProvider, xAPIKey, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 

### Return type

[**MusicExportSuccess**](MusicExportSuccess.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteMusicPreferencesExportVendor

> deleteMusicPreferencesExportVendor(authorization, xAuthenticationProvider, xAPIKey, vendor)

Music Export Vendor Preferences

Remove Vendor specific export preferences (e.g. 3rd party vendors, partner id&#39;s) for a given BBC Music user. 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicExportApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let vendor = "vendor_example"; // String | Supported 3rd Party Vendor
apiInstance.deleteMusicPreferencesExportVendor(authorization, xAuthenticationProvider, xAPIKey, vendor, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **vendor** | **String**| Supported 3rd Party Vendor | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMusicExport

> MusicExportJob getMusicExport(authorization, xAuthenticationProvider, xAPIKey, opts)

Music Exports

Returns status of all previous third party export actions for a given BBC Music user. 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicExportApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let opts = {
  'offset': 56, // Number | Paginated results offset
  'limit': 56 // Number | Paginated results limit
};
apiInstance.getMusicExport(authorization, xAuthenticationProvider, xAPIKey, opts, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **offset** | **Number**| Paginated results offset | [optional] 
 **limit** | **Number**| Paginated results limit | [optional] 

### Return type

[**MusicExportJob**](MusicExportJob.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMusicExportJobs

> MusicExportJob getMusicExportJobs(authorization, xAuthenticationProvider, xAPIKey, over16, opts)

Music Export Jobs

All items associated to a users export request 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicExportApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let over16 = true; // Boolean | Boolean age check
let opts = {
  'vendor': "vendor_example" // String | Specify Vendor Jobs
};
apiInstance.getMusicExportJobs(authorization, xAuthenticationProvider, xAPIKey, over16, opts, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **over16** | **Boolean**| Boolean age check | 
 **vendor** | **String**| Specify Vendor Jobs | [optional] 

### Return type

[**MusicExportJob**](MusicExportJob.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMusicExportTracks

> MusicExportJob getMusicExportTracks(authorization, xAuthenticationProvider, xAPIKey, over16, opts)

Music Export Tracks

Retrieves vendor and status specific tracks 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicExportApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let over16 = true; // Boolean | Boolean age check
let opts = {
  'offset': 56, // Number | Paginated results offset
  'limit': 56, // Number | Paginated results limit
  'vendor': "vendor_example", // String | Specify Vendor Tracks
  'status': "status_example" // String | Specify Track status
};
apiInstance.getMusicExportTracks(authorization, xAuthenticationProvider, xAPIKey, over16, opts, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **over16** | **Boolean**| Boolean age check | 
 **offset** | **Number**| Paginated results offset | [optional] 
 **limit** | **Number**| Paginated results limit | [optional] 
 **vendor** | **String**| Specify Vendor Tracks | [optional] 
 **status** | **String**| Specify Track status | [optional] 

### Return type

[**MusicExportJob**](MusicExportJob.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMusicPreferencesExport

> MusicExportPreferencesResponse getMusicPreferencesExport(authorization, xAuthenticationProvider, xAPIKey)

Music Export Preferences

Returns export preferences (e.g. 3rd party vendors, partner id&#39;s) for a given BBC Music user. 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicExportApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
apiInstance.getMusicPreferencesExport(authorization, xAuthenticationProvider, xAPIKey, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 

### Return type

[**MusicExportPreferencesResponse**](MusicExportPreferencesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMusicPreferencesExportVendor

> MusicExportPreferencesResponse getMusicPreferencesExportVendor(authorization, xAuthenticationProvider, xAPIKey, vendor)

Music Export Vendor Preferences

Returns vendor specific export preferences for a given BBC Music user. 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicExportApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let vendor = "vendor_example"; // String | Supported 3rd Party Vendor
apiInstance.getMusicPreferencesExportVendor(authorization, xAuthenticationProvider, xAPIKey, vendor, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **vendor** | **String**| Supported 3rd Party Vendor | 

### Return type

[**MusicExportPreferencesResponse**](MusicExportPreferencesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postMusicExportJob

> MusicExportSuccess postMusicExportJob(authorization, xAuthenticationProvider, xAPIKey, over16, body, opts)

Music Export Jobs

Create Export Job for a user 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicExportApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let over16 = true; // Boolean | Boolean age check
let body = [new RadioMusicServices.MusicExportJob()]; // [MusicExportJob] | 
let opts = {
  'vendor': "vendor_example" // String | Specify Vendor Jobs
};
apiInstance.postMusicExportJob(authorization, xAuthenticationProvider, xAPIKey, over16, body, opts, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **over16** | **Boolean**| Boolean age check | 
 **body** | [**[MusicExportJob]**](MusicExportJob.md)|  | 
 **vendor** | **String**| Specify Vendor Jobs | [optional] 

### Return type

[**MusicExportSuccess**](MusicExportSuccess.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postMusicPreferencesExport

> MusicExportSuccess postMusicPreferencesExport(authorization, xAuthenticationProvider, xAPIKey, body)

Music Export Preferences

Create export preferences (e.g. 3rd party vendors, partner id&#39;s) for a given BBC Music user. 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicExportApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let body = new RadioMusicServices.MusicExportPreferences(); // MusicExportPreferences | 
apiInstance.postMusicPreferencesExport(authorization, xAuthenticationProvider, xAPIKey, body, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **body** | [**MusicExportPreferences**](MusicExportPreferences.md)|  | 

### Return type

[**MusicExportSuccess**](MusicExportSuccess.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postMusicPreferencesExportVendor

> postMusicPreferencesExportVendor(authorization, xAuthenticationProvider, xAPIKey, vendor, body)

Music Export Vendor Preferences

Create Vendor specific export preferences (e.g. 3rd party vendors, partner id&#39;s) for a given BBC Music user. 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicExportApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let vendor = "vendor_example"; // String | Supported 3rd Party Vendor
let body = new RadioMusicServices.MusicExportPreferences(); // MusicExportPreferences | 
apiInstance.postMusicPreferencesExportVendor(authorization, xAuthenticationProvider, xAPIKey, vendor, body, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **vendor** | **String**| Supported 3rd Party Vendor | 
 **body** | [**MusicExportPreferences**](MusicExportPreferences.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putMusicPreferencesExportVendor

> putMusicPreferencesExportVendor(authorization, xAuthenticationProvider, xAPIKey, vendor, body)

Music Export Vendor Preferences

Update vendor specific export preferences for a given BBC Music user. 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicExportApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let vendor = "vendor_example"; // String | Supported 3rd Party Vendor
let body = new RadioMusicServices.MusicExportPreferences(); // MusicExportPreferences | 
apiInstance.putMusicPreferencesExportVendor(authorization, xAuthenticationProvider, xAPIKey, vendor, body, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **vendor** | **String**| Supported 3rd Party Vendor | 
 **body** | [**MusicExportPreferences**](MusicExportPreferences.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

