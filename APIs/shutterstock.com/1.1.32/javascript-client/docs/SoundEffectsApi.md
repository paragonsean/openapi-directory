# ShutterstockApiExplorer.SoundEffectsApi

All URIs are relative to *https://api.shutterstock.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**downloadSfx**](SoundEffectsApi.md#downloadSfx) | **POST** /v2/sfx/licenses/{id}/downloads | Download sound effects
[**getSfxDetails**](SoundEffectsApi.md#getSfxDetails) | **GET** /v2/sfx/{id} | Get details about sound effects
[**getSfxLicenseList**](SoundEffectsApi.md#getSfxLicenseList) | **GET** /v2/sfx/licenses | List sound effects licenses
[**getSfxListDetails**](SoundEffectsApi.md#getSfxListDetails) | **GET** /v2/sfx | List details about sound effects
[**licensesSFX**](SoundEffectsApi.md#licensesSFX) | **POST** /v2/sfx/licenses | License sound effects
[**searchSFX**](SoundEffectsApi.md#searchSFX) | **GET** /v2/sfx/search | Search for sound effects



## downloadSfx

> SfxUrl downloadSfx(id)

Download sound effects

This endpoint redownloads sound effects that you have already received a license for. The download links in the response are valid for 8 hours.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.SoundEffectsApi();
let id = "123"; // String | License ID
apiInstance.downloadSfx(id, (error, data, response) => {
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
 **id** | **String**| License ID | 

### Return type

[**SfxUrl**](SfxUrl.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSfxDetails

> SFX getSfxDetails(id, opts)

Get details about sound effects

This endpoint shows information about a sound effect.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new ShutterstockApiExplorer.SoundEffectsApi();
let id = 442583; // Number | Audio track ID
let opts = {
  'language': new ShutterstockApiExplorer.Language(), // Language | Language for the keywords and categories in the response
  'view': "full", // String | Amount of detail to render in the response
  'library': "shutterstock", // String | Which library to fetch from
  'searchId': "00000000-0000-0000-0000-000000000000" // String | The ID of the search that is related to this request
};
apiInstance.getSfxDetails(id, opts, (error, data, response) => {
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
 **id** | **Number**| Audio track ID | 
 **language** | [**Language**](.md)| Language for the keywords and categories in the response | [optional] 
 **view** | **String**| Amount of detail to render in the response | [optional] [default to &#39;minimal&#39;]
 **library** | **String**| Which library to fetch from | [optional] 
 **searchId** | **String**| The ID of the search that is related to this request | [optional] 

### Return type

[**SFX**](SFX.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSfxLicenseList

> DownloadHistoryDataList getSfxLicenseList(opts)

List sound effects licenses

This endpoint lists existing licenses.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.SoundEffectsApi();
let opts = {
  'sfxId': "12345678", // String | Show licenses for the specified sound effects ID
  'license': "standard", // String | Show sound effects that are available with the specified license, such as `standard` or `enhanced`; prepending a `-` sign excludes results from that license
  'page': 1, // Number | Page number
  'perPage': 20, // Number | Number of results per page
  'sort': "'newest'", // String | Sort order
  'username': "aUniqueUsername", // String | Filter licenses by username of licensee
  'startDate': new Date("2021-03-29T13:25:13.521Z"), // Date | Show licenses created on or after the specified date
  'endDate': new Date("2021-03-29T13:25:13.521Z"), // Date | Show licenses created before the specified date
  'licenseId': "licenseId_example", // String | Filter by the license ID
  'downloadAvailability': "'all'", // String | Filter licenses by download availability
  'teamHistory': false // Boolean | Set to true to see license history for all members of your team.
};
apiInstance.getSfxLicenseList(opts, (error, data, response) => {
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
 **sfxId** | **String**| Show licenses for the specified sound effects ID | [optional] 
 **license** | **String**| Show sound effects that are available with the specified license, such as &#x60;standard&#x60; or &#x60;enhanced&#x60;; prepending a &#x60;-&#x60; sign excludes results from that license | [optional] 
 **page** | **Number**| Page number | [optional] [default to 1]
 **perPage** | **Number**| Number of results per page | [optional] [default to 20]
 **sort** | **String**| Sort order | [optional] [default to &#39;newest&#39;]
 **username** | **String**| Filter licenses by username of licensee | [optional] 
 **startDate** | **Date**| Show licenses created on or after the specified date | [optional] 
 **endDate** | **Date**| Show licenses created before the specified date | [optional] 
 **licenseId** | **String**| Filter by the license ID | [optional] 
 **downloadAvailability** | **String**| Filter licenses by download availability | [optional] [default to &#39;all&#39;]
 **teamHistory** | **Boolean**| Set to true to see license history for all members of your team. | [optional] [default to false]

### Return type

[**DownloadHistoryDataList**](DownloadHistoryDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSfxListDetails

> SFXDataList getSfxListDetails(id, opts)

List details about sound effects

This endpoint shows information about sound effects.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new ShutterstockApiExplorer.SoundEffectsApi();
let id = ["null"]; // [String] | One or more sound effect IDs
let opts = {
  'view': "minimal", // String | Amount of detail to render in the response
  'language': new ShutterstockApiExplorer.Language(), // Language | Language for the keywords and categories in the response
  'library': "shutterstock", // String | Which library to fetch from
  'searchId': "00000000-0000-0000-0000-000000000000" // String | The ID of the search that is related to this request
};
apiInstance.getSfxListDetails(id, opts, (error, data, response) => {
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
 **id** | [**[String]**](String.md)| One or more sound effect IDs | 
 **view** | **String**| Amount of detail to render in the response | [optional] [default to &#39;minimal&#39;]
 **language** | [**Language**](.md)| Language for the keywords and categories in the response | [optional] 
 **library** | **String**| Which library to fetch from | [optional] 
 **searchId** | **String**| The ID of the search that is related to this request | [optional] 

### Return type

[**SFXDataList**](SFXDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## licensesSFX

> LicenseSFXResultDataList licensesSFX(licenseSFXRequest)

License sound effects

This endpoint licenses sounds effect assets.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new ShutterstockApiExplorer.SoundEffectsApi();
let licenseSFXRequest = {"$ref":"#/components/schemas/LicenseSFXRequest/example"}; // LicenseSFXRequest | 
apiInstance.licensesSFX(licenseSFXRequest, (error, data, response) => {
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
 **licenseSFXRequest** | [**LicenseSFXRequest**](LicenseSFXRequest.md)|  | 

### Return type

[**LicenseSFXResultDataList**](LicenseSFXResultDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchSFX

> SFXSearchResults searchSFX(opts)

Search for sound effects

This endpoint searches for sound effects. If you specify more than one search parameter, the API uses an AND condition.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new ShutterstockApiExplorer.SoundEffectsApi();
let opts = {
  'addedDate': new Date("2022-09-23"), // Date | Show sound effects added on the specified date
  'addedDateStart': new Date("2021-03-29"), // Date | Show sound effects added on or after the specified date
  'addedDateEnd': new Date("2021-03-29"), // Date | Show sound effects added before the specified date
  'duration': 180, // Number | Show sound effects with the specified duration in seconds
  'durationFrom': 30, // Number | Show sound effects with the specified duration or longer in seconds
  'durationTo': 180, // Number | Show sound effects with the specified duration or shorter in seconds
  'page': 1, // Number | Page number
  'perPage': 1, // Number | Number of results per page
  'query': "drum", // String | One or more search terms separated by spaces
  'safe': true, // Boolean | Enable or disable safe search
  'sort': "popular", // String | Sort by
  'view': "full", // String | Amount of detail to render in the response
  'language': new ShutterstockApiExplorer.Language() // Language | Set query and result language (uses Accept-Language header if not set)
};
apiInstance.searchSFX(opts, (error, data, response) => {
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
 **addedDate** | **Date**| Show sound effects added on the specified date | [optional] 
 **addedDateStart** | **Date**| Show sound effects added on or after the specified date | [optional] 
 **addedDateEnd** | **Date**| Show sound effects added before the specified date | [optional] 
 **duration** | **Number**| Show sound effects with the specified duration in seconds | [optional] 
 **durationFrom** | **Number**| Show sound effects with the specified duration or longer in seconds | [optional] 
 **durationTo** | **Number**| Show sound effects with the specified duration or shorter in seconds | [optional] 
 **page** | **Number**| Page number | [optional] [default to 1]
 **perPage** | **Number**| Number of results per page | [optional] [default to 20]
 **query** | **String**| One or more search terms separated by spaces | [optional] 
 **safe** | **Boolean**| Enable or disable safe search | [optional] [default to true]
 **sort** | **String**| Sort by | [optional] [default to &#39;popular&#39;]
 **view** | **String**| Amount of detail to render in the response | [optional] [default to &#39;minimal&#39;]
 **language** | [**Language**](.md)| Set query and result language (uses Accept-Language header if not set) | [optional] 

### Return type

[**SFXSearchResults**](SFXSearchResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

