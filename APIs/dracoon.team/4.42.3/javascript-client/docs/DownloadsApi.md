# DracoonApi.DownloadsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**downloadAvatar**](DownloadsApi.md#downloadAvatar) | **GET** /v4/downloads/avatar/{user_id}/{uuid} | Download avatar
[**downloadFileViaToken**](DownloadsApi.md#downloadFileViaToken) | **GET** /v4/downloads/{token} | Download file
[**downloadFileViaToken1**](DownloadsApi.md#downloadFileViaToken1) | **HEAD** /v4/downloads/{token} | Download file
[**downloadZipArchiveViaToken**](DownloadsApi.md#downloadZipArchiveViaToken) | **GET** /v4/downloads/zip/{token} | Download ZIP archive



## downloadAvatar

> String downloadAvatar(userId, uuid)

Download avatar

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.11.0&lt;/h3&gt;  ### Description: Download avatar for given user ID and UUID.  ### Precondition: Valid UUID.  ### Postcondition: Stream is returned.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';

let apiInstance = new DracoonApi.DownloadsApi();
let userId = 789; // Number | User ID
let uuid = "uuid_example"; // String | UUID of the avatar
apiInstance.downloadAvatar(userId, uuid, (error, data, response) => {
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
 **userId** | **Number**| User ID | 
 **uuid** | **String**| UUID of the avatar | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## downloadFileViaToken

> downloadFileViaToken(token, opts)

Download file

### Description: Download a file.  ### Precondition: Valid download token.  ### Postcondition: Stream is returned.  ### Further Information: Range requests are supported.

### Example

```javascript
import DracoonApi from 'dracoon_api';

let apiInstance = new DracoonApi.DownloadsApi();
let token = "token_example"; // String | Download token
let opts = {
  'range': "range_example", // String | Range   e.g. `bytes=0-999`
  'genericMimetype': true, // Boolean | Always return `application/octet-stream` instead of specific mimetype
  'inline': true // Boolean | Use Content-Disposition: `inline` instead of `attachment`
};
apiInstance.downloadFileViaToken(token, opts, (error, data, response) => {
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
 **token** | **String**| Download token | 
 **range** | **String**| Range   e.g. &#x60;bytes&#x3D;0-999&#x60; | [optional] 
 **genericMimetype** | **Boolean**| Always return &#x60;application/octet-stream&#x60; instead of specific mimetype | [optional] 
 **inline** | **Boolean**| Use Content-Disposition: &#x60;inline&#x60; instead of &#x60;attachment&#x60; | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## downloadFileViaToken1

> downloadFileViaToken1(token, opts)

Download file

### Description: Download a file.  ### Precondition: Valid download token.  ### Postcondition: Stream is returned.  ### Further Information: Range requests are supported.

### Example

```javascript
import DracoonApi from 'dracoon_api';

let apiInstance = new DracoonApi.DownloadsApi();
let token = "token_example"; // String | Download token
let opts = {
  'range': "range_example", // String | Range   e.g. `bytes=0-999`
  'genericMimetype': true, // Boolean | Always return `application/octet-stream` instead of specific mimetype
  'inline': true // Boolean | Use Content-Disposition: `inline` instead of `attachment`
};
apiInstance.downloadFileViaToken1(token, opts, (error, data, response) => {
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
 **token** | **String**| Download token | 
 **range** | **String**| Range   e.g. &#x60;bytes&#x3D;0-999&#x60; | [optional] 
 **genericMimetype** | **Boolean**| Always return &#x60;application/octet-stream&#x60; instead of specific mimetype | [optional] 
 **inline** | **Boolean**| Use Content-Disposition: &#x60;inline&#x60; instead of &#x60;attachment&#x60; | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## downloadZipArchiveViaToken

> downloadZipArchiveViaToken(token)

Download ZIP archive

### Description: Download multiple files in a ZIP archive.  ### Precondition: Valid download token.  ### Postcondition: Stream is returned.  ### Further Information: Create a download token with &#x60;POST /nodes/zip&#x60; API.

### Example

```javascript
import DracoonApi from 'dracoon_api';

let apiInstance = new DracoonApi.DownloadsApi();
let token = "token_example"; // String | Download token
apiInstance.downloadZipArchiveViaToken(token, (error, data, response) => {
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
 **token** | **String**| Download token | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream

