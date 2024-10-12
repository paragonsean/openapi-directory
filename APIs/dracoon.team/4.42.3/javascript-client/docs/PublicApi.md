# DracoonApi.PublicApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelFileUploadViaShare**](PublicApi.md#cancelFileUploadViaShare) | **DELETE** /v4/public/shares/uploads/{access_key}/{upload_id} | Cancel file upload
[**checkPublicDownloadSharePassword**](PublicApi.md#checkPublicDownloadSharePassword) | **HEAD** /v4/public/shares/downloads/{access_key} | Check public Download Share password
[**completeFileUploadViaShare**](PublicApi.md#completeFileUploadViaShare) | **PUT** /v4/public/shares/uploads/{access_key}/{upload_id} | Complete file upload
[**completeS3FileUploadViaShare**](PublicApi.md#completeS3FileUploadViaShare) | **PUT** /v4/public/shares/uploads/{access_key}/{upload_id}/s3 | Complete S3 file upload
[**createShareUploadChannel**](PublicApi.md#createShareUploadChannel) | **POST** /v4/public/shares/uploads/{access_key} | Create new file upload channel
[**downloadFileViaTokenPublic**](PublicApi.md#downloadFileViaTokenPublic) | **GET** /v4/public/shares/downloads/{access_key}/{token} | Download file with token
[**downloadFileViaTokenPublic1**](PublicApi.md#downloadFileViaTokenPublic1) | **HEAD** /v4/public/shares/downloads/{access_key}/{token} | Download file with token
[**generateDownloadUrlPublic**](PublicApi.md#generateDownloadUrlPublic) | **POST** /v4/public/shares/downloads/{access_key} | Generate download URL
[**generatePresignedUrlsPublic**](PublicApi.md#generatePresignedUrlsPublic) | **POST** /v4/public/shares/uploads/{access_key}/{upload_id}/s3_urls | Generate presigned URLs for S3 file upload
[**requestActiveDirectoryAuthInfo**](PublicApi.md#requestActiveDirectoryAuthInfo) | **GET** /v4/public/system/info/auth/ad | Request Active Directory authentication information
[**requestOpenIdAuthInfo**](PublicApi.md#requestOpenIdAuthInfo) | **GET** /v4/public/system/info/auth/openid | Request OpenID Connect provider authentication information
[**requestPublicDownloadShareInfo**](PublicApi.md#requestPublicDownloadShareInfo) | **GET** /v4/public/shares/downloads/{access_key} | Request public Download Share information
[**requestPublicUploadShareInfo**](PublicApi.md#requestPublicUploadShareInfo) | **GET** /v4/public/shares/uploads/{access_key} | Request public Upload Share information
[**requestSoftwareVersion**](PublicApi.md#requestSoftwareVersion) | **GET** /v4/public/software/version | Request software version information
[**requestSystemInfo**](PublicApi.md#requestSystemInfo) | **GET** /v4/public/system/info | Request system information
[**requestSystemTime**](PublicApi.md#requestSystemTime) | **GET** /v4/public/time | Request system time
[**requestThirdPartyDependencies**](PublicApi.md#requestThirdPartyDependencies) | **GET** /v4/public/software/third_party_dependencies | Request third-party software dependencies
[**requestUploadStatusPublic**](PublicApi.md#requestUploadStatusPublic) | **GET** /v4/public/shares/uploads/{access_key}/{upload_id} | Request status of S3 file upload
[**uploadFileAsMultipartPublic1**](PublicApi.md#uploadFileAsMultipartPublic1) | **POST** /v4/public/shares/uploads/{access_key}/{upload_id} | Upload file



## cancelFileUploadViaShare

> cancelFileUploadViaShare(accessKey, uploadId)

Cancel file upload

### Description: Abort (chunked) upload via Upload Share.  ### Precondition: Valid Upload ID.  ### Postcondition: Aborts upload and invalidates upload ID / token.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';

let apiInstance = new DracoonApi.PublicApi();
let accessKey = "accessKey_example"; // String | Access key
let uploadId = "uploadId_example"; // String | Upload channel ID
apiInstance.cancelFileUploadViaShare(accessKey, uploadId, (error, data, response) => {
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
 **accessKey** | **String**| Access key | 
 **uploadId** | **String**| Upload channel ID | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## checkPublicDownloadSharePassword

> checkPublicDownloadSharePassword(accessKey, opts)

Check public Download Share password

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.36.0&lt;/h3&gt;  ### Description: Check password for a public Download Share  ### Precondition: None.  ### Postcondition: None.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';

let apiInstance = new DracoonApi.PublicApi();
let accessKey = "accessKey_example"; // String | Access key
let opts = {
  'password': "password_example" // String | Download share password
};
apiInstance.checkPublicDownloadSharePassword(accessKey, opts, (error, data, response) => {
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
 **accessKey** | **String**| Access key | 
 **password** | **String**| Download share password | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## completeFileUploadViaShare

> PublicUploadedFileData completeFileUploadViaShare(accessKey, uploadId, opts)

Complete file upload

### Description: Finalize (chunked) upload via Upload Share.  ### Precondition: Valid upload ID.   Only returns users that owns one of the following permissions: &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage download share&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage upload share&lt;/span&gt;  ### Postcondition: Finalizes upload.  ### Further Information: Chunked uploads (range requests) are supported.    Please ensure that all chunks have been transferred correctly before finishing the upload.   If file hash has been created in time a &#x60;201 Created&#x60; will be responded and hash will be part of response, otherwise it will be a &#x60;202 Accepted&#x60; without it. 

### Example

```javascript
import DracoonApi from 'dracoon_api';

let apiInstance = new DracoonApi.PublicApi();
let accessKey = "accessKey_example"; // String | Access key
let uploadId = "uploadId_example"; // String | Upload channel ID
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'userFileKeyList': new DracoonApi.UserFileKeyList() // UserFileKeyList | 
};
apiInstance.completeFileUploadViaShare(accessKey, uploadId, opts, (error, data, response) => {
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
 **accessKey** | **String**| Access key | 
 **uploadId** | **String**| Upload channel ID | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **userFileKeyList** | [**UserFileKeyList**](UserFileKeyList.md)|  | [optional] 

### Return type

[**PublicUploadedFileData**](PublicUploadedFileData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## completeS3FileUploadViaShare

> completeS3FileUploadViaShare(accessKey, uploadId, completeS3ShareUploadRequest)

Complete S3 file upload

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.15.0&lt;/h3&gt;  ### Description: Finishes a S3 file upload and closes the corresponding upload channel.  ### Precondition: Valid upload ID.   Only returns users that owns one of the following permissions: &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage download share&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage upload share&lt;/span&gt;  ### Postcondition: Upload channel is closed. S3 multipart upload request is completed.  ### Further Information: None. 

### Example

```javascript
import DracoonApi from 'dracoon_api';

let apiInstance = new DracoonApi.PublicApi();
let accessKey = "accessKey_example"; // String | Access key
let uploadId = "uploadId_example"; // String | Upload channel ID
let completeS3ShareUploadRequest = new DracoonApi.CompleteS3ShareUploadRequest(); // CompleteS3ShareUploadRequest | 
apiInstance.completeS3FileUploadViaShare(accessKey, uploadId, completeS3ShareUploadRequest, (error, data, response) => {
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
 **accessKey** | **String**| Access key | 
 **uploadId** | **String**| Upload channel ID | 
 **completeS3ShareUploadRequest** | [**CompleteS3ShareUploadRequest**](CompleteS3ShareUploadRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createShareUploadChannel

> CreateShareUploadChannelResponse createShareUploadChannel(accessKey, createShareUploadChannelRequest)

Create new file upload channel

### Description:   Create a new upload channel.  ### Precondition: None.  ### Postcondition: Upload channel is created and corresponding upload URL, token &amp; upload ID are returned.  ### Further Information: Use &#x60;uploadUrl&#x60; the upload &#x60;token&#x60; is deprecated.    Please provide the size of the intended upload so that the quota can be checked in advanced and no data is transferred unnecessarily.  ### Node naming convention: * Node (room, folder, file) names are limited to **150** characters. * Illegal names:   &#x60;&#39;CON&#39;, &#39;PRN&#39;, &#39;AUX&#39;, &#39;NUL&#39;, &#39;COM1&#39;, &#39;COM2&#39;, &#39;COM3&#39;, &#39;COM4&#39;, &#39;COM5&#39;, &#39;COM6&#39;, &#39;COM7&#39;, &#39;COM8&#39;, &#39;COM9&#39;, &#39;LPT1&#39;, &#39;LPT2&#39;, &#39;LPT3&#39;, &#39;LPT4&#39;, &#39;LPT5&#39;, &#39;LPT6&#39;, &#39;LPT7&#39;, &#39;LPT8&#39;, &#39;LPT9&#39;, (and any of those with an extension)&#x60; * Illegal characters in names:   &#x60;&#39;\\\\&#39;, &#39;&lt;&#39;,&#39;&gt;&#39;, &#39;:&#39;, &#39;\\\&quot;&#39;, &#39;|&#39;, &#39;?&#39;, &#39;*&#39;, &#39;/&#39;, leading &#39;-&#39;, trailing &#39;.&#39; &#x60; 

### Example

```javascript
import DracoonApi from 'dracoon_api';

let apiInstance = new DracoonApi.PublicApi();
let accessKey = "accessKey_example"; // String | Access key
let createShareUploadChannelRequest = new DracoonApi.CreateShareUploadChannelRequest(); // CreateShareUploadChannelRequest | 
apiInstance.createShareUploadChannel(accessKey, createShareUploadChannelRequest, (error, data, response) => {
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
 **accessKey** | **String**| Access key | 
 **createShareUploadChannelRequest** | [**CreateShareUploadChannelRequest**](CreateShareUploadChannelRequest.md)|  | 

### Return type

[**CreateShareUploadChannelResponse**](CreateShareUploadChannelResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## downloadFileViaTokenPublic

> downloadFileViaTokenPublic(accessKey, token, opts)

Download file with token

### Description:   Download a file (or zip archive if target is a folder or room).  ### Precondition: Valid download token.  ### Postcondition: Stream is returned.  ### Further Information: Range requests are supported.   Range requests are illegal for zip archive download.

### Example

```javascript
import DracoonApi from 'dracoon_api';

let apiInstance = new DracoonApi.PublicApi();
let accessKey = "accessKey_example"; // String | Access key
let token = "token_example"; // String | Download token
let opts = {
  'range': "range_example", // String | Range   e.g. `bytes=0-999`
  'genericMimetype': true, // Boolean | Always return `application/octet-stream` instead of specific mimetype
  'inline': true // Boolean | Use Content-Disposition: `inline` instead of `attachment`
};
apiInstance.downloadFileViaTokenPublic(accessKey, token, opts, (error, data, response) => {
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
 **accessKey** | **String**| Access key | 
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


## downloadFileViaTokenPublic1

> downloadFileViaTokenPublic1(accessKey, token, opts)

Download file with token

### Description:   Download a file (or zip archive if target is a folder or room).  ### Precondition: Valid download token.  ### Postcondition: Stream is returned.  ### Further Information: Range requests are supported.   Range requests are illegal for zip archive download.

### Example

```javascript
import DracoonApi from 'dracoon_api';

let apiInstance = new DracoonApi.PublicApi();
let accessKey = "accessKey_example"; // String | Access key
let token = "token_example"; // String | Download token
let opts = {
  'range': "range_example", // String | Range   e.g. `bytes=0-999`
  'genericMimetype': true, // Boolean | Always return `application/octet-stream` instead of specific mimetype
  'inline': true // Boolean | Use Content-Disposition: `inline` instead of `attachment`
};
apiInstance.downloadFileViaTokenPublic1(accessKey, token, opts, (error, data, response) => {
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
 **accessKey** | **String**| Access key | 
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


## generateDownloadUrlPublic

> PublicDownloadTokenGenerateResponse generateDownloadUrlPublic(accessKey, opts)

Generate download URL

### Description: Generate a download URL to retrieve a shared file.  ### Precondition: None.  ### Postcondition: Download URL and token are generated and returned.  ### Further Information: Use &#x60;downloadUrl&#x60; the download &#x60;token&#x60; is deprecated.

### Example

```javascript
import DracoonApi from 'dracoon_api';

let apiInstance = new DracoonApi.PublicApi();
let accessKey = "accessKey_example"; // String | Access key
let opts = {
  'publicDownloadTokenGenerateRequest': new DracoonApi.PublicDownloadTokenGenerateRequest() // PublicDownloadTokenGenerateRequest | 
};
apiInstance.generateDownloadUrlPublic(accessKey, opts, (error, data, response) => {
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
 **accessKey** | **String**| Access key | 
 **publicDownloadTokenGenerateRequest** | [**PublicDownloadTokenGenerateRequest**](PublicDownloadTokenGenerateRequest.md)|  | [optional] 

### Return type

[**PublicDownloadTokenGenerateResponse**](PublicDownloadTokenGenerateResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## generatePresignedUrlsPublic

> PresignedUrlList generatePresignedUrlsPublic(accessKey, uploadId, generatePresignedUrlsRequest, opts)

Generate presigned URLs for S3 file upload

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.15.0&lt;/h3&gt;  ### Description: Generate presigned URLs for S3 file upload.  ### Precondition: Valid upload ID  ### Postcondition: List of presigned URLs is returned.  ### Further Information: The size for each part must be &gt;&#x3D; 5 MB, except for the last part.   The part number of the first part in S3 is 1 (not 0).   Use HTTP method &#x60;PUT&#x60; for uploading bytes via presigned URL.

### Example

```javascript
import DracoonApi from 'dracoon_api';

let apiInstance = new DracoonApi.PublicApi();
let accessKey = "accessKey_example"; // String | Access key
let uploadId = "uploadId_example"; // String | Upload channel ID
let generatePresignedUrlsRequest = new DracoonApi.GeneratePresignedUrlsRequest(); // GeneratePresignedUrlsRequest | 
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example" // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
};
apiInstance.generatePresignedUrlsPublic(accessKey, uploadId, generatePresignedUrlsRequest, opts, (error, data, response) => {
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
 **accessKey** | **String**| Access key | 
 **uploadId** | **String**| Upload channel ID | 
 **generatePresignedUrlsRequest** | [**GeneratePresignedUrlsRequest**](GeneratePresignedUrlsRequest.md)|  | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 

### Return type

[**PresignedUrlList**](PresignedUrlList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## requestActiveDirectoryAuthInfo

> ActiveDirectoryAuthInfo requestActiveDirectoryAuthInfo(opts)

Request Active Directory authentication information

### Description:   Provides information about Active Directory authentication options.  ### Precondition: None.  ### Postcondition: Active Directory authentication options information is returned.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';

let apiInstance = new DracoonApi.PublicApi();
let opts = {
  'isGlobalAvailable': true // Boolean | Show only global available items
};
apiInstance.requestActiveDirectoryAuthInfo(opts, (error, data, response) => {
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
 **isGlobalAvailable** | **Boolean**| Show only global available items | [optional] 

### Return type

[**ActiveDirectoryAuthInfo**](ActiveDirectoryAuthInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestOpenIdAuthInfo

> OpenIdAuthInfo requestOpenIdAuthInfo(opts)

Request OpenID Connect provider authentication information

### Description:   Provides information about OpenID Connect authentication options.  ### Precondition: None.  ### Postcondition: OpenID Connect authentication options information is returned.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';

let apiInstance = new DracoonApi.PublicApi();
let opts = {
  'isGlobalAvailable': true // Boolean | Show only global available items
};
apiInstance.requestOpenIdAuthInfo(opts, (error, data, response) => {
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
 **isGlobalAvailable** | **Boolean**| Show only global available items | [optional] 

### Return type

[**OpenIdAuthInfo**](OpenIdAuthInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestPublicDownloadShareInfo

> PublicDownloadShare requestPublicDownloadShareInfo(accessKey, opts)

Request public Download Share information

### Description:   Retrieve the public information of a Download Share.  ### Precondition: None.  ### Postcondition: Download Share information is returned.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';

let apiInstance = new DracoonApi.PublicApi();
let accessKey = "accessKey_example"; // String | Access key
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example" // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
};
apiInstance.requestPublicDownloadShareInfo(accessKey, opts, (error, data, response) => {
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
 **accessKey** | **String**| Access key | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 

### Return type

[**PublicDownloadShare**](PublicDownloadShare.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestPublicUploadShareInfo

> PublicUploadShare requestPublicUploadShareInfo(accessKey, opts)

Request public Upload Share information

### Description:   Provides information about the desired Upload Share.  ### Precondition: Only &#x60;userUserPublicKeyList&#x60; is returned to the users who owns one of the following permissions: &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage download share&lt;/span&gt;, &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; manage upload share&lt;/span&gt;  ### Postcondition: None.  ### Further Information: If no password is set, the returned information is reduced to the following attributes (if available):  * &#x60;name&#x60; * &#x60;createdAt&#x60; * &#x60;isProtected&#x60; * &#x60;isEncrypted&#x60; * &#x60;showUploadedFiles&#x60; * &#x60;userUserPublicKeyList&#x60; (if parent is end-to-end encrypted)  Only if the password is transmitted as &#x60;X-Sds-Share-Password&#x60; header, all values are returned. 

### Example

```javascript
import DracoonApi from 'dracoon_api';

let apiInstance = new DracoonApi.PublicApi();
let accessKey = "accessKey_example"; // String | Access key
let opts = {
  'xSdsSharePassword': "xSdsSharePassword_example", // String | Upload share password. Should be base64-encoded.  Plain X-Sds-Share-Passwords are *deprecated* and will be removed in the future
  'xSdsDateFormat': "xSdsDateFormat_example" // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
};
apiInstance.requestPublicUploadShareInfo(accessKey, opts, (error, data, response) => {
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
 **accessKey** | **String**| Access key | 
 **xSdsSharePassword** | **String**| Upload share password. Should be base64-encoded.  Plain X-Sds-Share-Passwords are *deprecated* and will be removed in the future | [optional] 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 

### Return type

[**PublicUploadShare**](PublicUploadShare.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestSoftwareVersion

> SoftwareVersionData requestSoftwareVersion(opts)

Request software version information

### Description:   Public software version information.  ### Precondition: None.  ### Postcondition: Sofware version information is returned.  ### Further Information: The version of DRACOON Server consists of two components: * **API** * **Core** (referred to as _\&quot;Server\&quot;_)  which are versioned individually.

### Example

```javascript
import DracoonApi from 'dracoon_api';

let apiInstance = new DracoonApi.PublicApi();
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example" // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
};
apiInstance.requestSoftwareVersion(opts, (error, data, response) => {
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
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 

### Return type

[**SoftwareVersionData**](SoftwareVersionData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestSystemInfo

> SystemInfo requestSystemInfo(opts)

Request system information

### Description:   Provides information about system.  ### Precondition: None.  ### Postcondition: System information is returned.  ### Further Information: Authentication methods are sorted by **priority** attribute.   Smaller values have higher priority.   Authentication method with highest priority is considered as default.  ### System information: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Setting | Description | Value | | :--- | :--- | :--- | | &#x60;languageDefault&#x60; | Defines which language should be default. | &#x60;ISO 639-1 code&#x60; | | &#x60;hideLoginInputFields&#x60; | Defines if login fields should be hidden. | &#x60;true or false&#x60; | | &#x60;s3Hosts&#x60; | List of available S3 hosts. | &#x60;String array&#x60; | | &#x60;s3EnforceDirectUpload&#x60; | Determines whether S3 direct upload is enforced or not. | &#x60;true or false&#x60; | | &#x60;useS3Storage&#x60; | Determines whether S3 Storage enabled and used. | &#x60;true or false&#x60; |  &lt;/details&gt;  ### Authentication methods: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Authentication Method | Description | | :--- | :--- | | &#x60;basic&#x60; | **Basic** authentication globally allowed.&lt;br&gt;This option **MUST** be activated to allow users to log in with their credentials stored in the database.&lt;br&gt;Formerly known as &#x60;sql&#x60;. | | &#x60;active_directory&#x60; | **Active Directory** authentication globally allowed.&lt;br&gt;This option **MUST** be activated to allow users to log in with their Active Directory credentials. | | &#x60;radius&#x60; | **RADIUS** authentication globally allowed.&lt;br&gt;This option **MUST** be activated to allow users to log in with their RADIUS username, their PIN and a token password. | | &#x60;openid&#x60; | **OpenID Connect** authentication globally allowed.This option **MUST** be activated to allow users to log in with their OpenID Connect identity. | | &#x60;hideLoginInputFields&#x60; | Determines whether input fields for login should be enabled | &#x60;true or false&#x60; |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';

let apiInstance = new DracoonApi.PublicApi();
let opts = {
  'isEnabled': true // Boolean | Show only enabled authentication methods
};
apiInstance.requestSystemInfo(opts, (error, data, response) => {
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
 **isEnabled** | **Boolean**| Show only enabled authentication methods | [optional] 

### Return type

[**SystemInfo**](SystemInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestSystemTime

> SdsServerTime requestSystemTime(opts)

Request system time

### Description:   Retrieve the actual server time.  ### Precondition: None.  ### Postcondition: Server time is returned.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';

let apiInstance = new DracoonApi.PublicApi();
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example" // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
};
apiInstance.requestSystemTime(opts, (error, data, response) => {
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
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 

### Return type

[**SdsServerTime**](SdsServerTime.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestThirdPartyDependencies

> [ThirdPartyDependenciesData] requestThirdPartyDependencies()

Request third-party software dependencies

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.9.0&lt;/h3&gt;  ### Description:   Provides information about used third-party software dependencies.  ### Precondition: None.  ### Postcondition: List of the third-party software dependencies used by **DRACOON Core** (referred to as _\&quot;Server\&quot;_) is returned.  ### Further Information: None.  

### Example

```javascript
import DracoonApi from 'dracoon_api';

let apiInstance = new DracoonApi.PublicApi();
apiInstance.requestThirdPartyDependencies((error, data, response) => {
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

[**[ThirdPartyDependenciesData]**](ThirdPartyDependenciesData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestUploadStatusPublic

> S3ShareUploadStatus requestUploadStatusPublic(accessKey, uploadId)

Request status of S3 file upload

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.15.0&lt;/h3&gt;  ### Description: Request status of a S3 file upload.  ### Precondition: An upload channel has been created and the user has &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; create&lt;/span&gt; permissions in the parent container (room or folder).  ### Postcondition: Status of S3 multipart upload request is returned.  ### Further Information: None.  ### Possible errors: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Http Status | Error Code | Description | | :--- | :--- | :--- | | &#x60;400 Bad Request&#x60; | &#x60;-80000&#x60; | Mandatory fields cannot be empty | | &#x60;400 Bad Request&#x60; | &#x60;-80001&#x60; | Invalid positive number | | &#x60;400 Bad Request&#x60; | &#x60;-80002&#x60; | Invalid number | | &#x60;400 Bad Request&#x60; | &#x60;-40001&#x60; | (Target) room is not encrypted | | &#x60;400 Bad Request&#x60; | &#x60;-40755&#x60; | Bad file name | | &#x60;400 Bad Request&#x60; | &#x60;-40763&#x60; | File key must be set for an upload into encrypted room | | &#x60;400 Bad Request&#x60; | &#x60;-50506&#x60; | Exceeds the number of files for this Upload Share | | &#x60;403 Forbidden&#x60; |  | Access denied | | &#x60;404 Not Found&#x60; | &#x60;-20501&#x60; | Upload not found | | &#x60;404 Not Found&#x60; | &#x60;-40000&#x60; | Container not found | | &#x60;404 Not Found&#x60; | &#x60;-41000&#x60; | Node not found | | &#x60;404 Not Found&#x60; | &#x60;-70501&#x60; | User not found | | &#x60;409 Conflict&#x60; | &#x60;-40010&#x60; | Container cannot be overwritten | | &#x60;409 Conflict&#x60; |  | File cannot be overwritten | | &#x60;500 Internal Server Error&#x60; |  | System Error | | &#x60;502 Bad Gateway&#x60; |  | S3 Error | | &#x60;502 Insufficient Storage&#x60; | &#x60;-50504&#x60; | Exceeds the quota for this Upload Share | | &#x60;502 Insufficient Storage&#x60; | &#x60;-40200&#x60; | Exceeds the free node quota in room | | &#x60;502 Insufficient Storage&#x60; | &#x60;-90200&#x60; | Exceeds the free customer quota | | &#x60;502 Insufficient Storage&#x60; | &#x60;-90201&#x60; | Exceeds the free customer physical disk space |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';

let apiInstance = new DracoonApi.PublicApi();
let accessKey = "accessKey_example"; // String | Access key
let uploadId = "uploadId_example"; // String | Upload channel ID
apiInstance.requestUploadStatusPublic(accessKey, uploadId, (error, data, response) => {
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
 **accessKey** | **String**| Access key | 
 **uploadId** | **String**| Upload channel ID | 

### Return type

[**S3ShareUploadStatus**](S3ShareUploadStatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## uploadFileAsMultipartPublic1

> ChunkUploadResponse uploadFileAsMultipartPublic1(accessKey, uploadId, file, opts)

Upload file

### Description:   Chunked upload of files via Upload Share.  ### Precondition: Valid upload ID.  ### Postcondition: Chunk of file is uploaded.  ### Further Information: Chunked uploads (range requests) are supported.  Following &#x60;Content-Types&#x60; are supported by this API: * &#x60;multipart/form-data&#x60; * provided &#x60;Content-Type&#x60;    For both file upload types set the correct &#x60;Content-Type&#x60; header and body.    ### Examples:    * &#x60;multipart/form-data&#x60; &#x60;&#x60;&#x60; POST /api/v4/public/shares/uploads/{access_key}{upload_id} HTTP/1.1  Header: ... Content-Type: multipart/form-data; boundary&#x3D;----WebKitFormBoundary7MA4YWxkTrZu0gW ...  Body: ------WebKitFormBoundary7MA4YWxkTrZu0gW Content-Disposition: form-data; name&#x3D;\&quot;file\&quot;; filename&#x3D;\&quot;file.txt\&quot; Content-Type: text/plain  Content of file.txt ------WebKitFormBoundary7MA4YWxkTrZu0gW-- &#x60;&#x60;&#x60;  * any other &#x60;Content-Type&#x60;   &#x60;&#x60;&#x60; POST /api/v4/public/shares/uploads/{access_key}{upload_id} HTTP/1.1  Header: ... Content-Type: { ... } ...  Body: raw content &#x60;&#x60;&#x60;

### Example

```javascript
import DracoonApi from 'dracoon_api';

let apiInstance = new DracoonApi.PublicApi();
let accessKey = "accessKey_example"; // String | Access key
let uploadId = "uploadId_example"; // String | Upload channel ID
let file = "/path/to/file"; // File | File
let opts = {
  'contentRange': "contentRange_example", // String | Content-Range   e.g. `bytes 0-999/3980`
  'xSdsDateFormat': "xSdsDateFormat_example" // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
};
apiInstance.uploadFileAsMultipartPublic1(accessKey, uploadId, file, opts, (error, data, response) => {
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
 **accessKey** | **String**| Access key | 
 **uploadId** | **String**| Upload channel ID | 
 **file** | **File**| File | 
 **contentRange** | **String**| Content-Range   e.g. &#x60;bytes 0-999/3980&#x60; | [optional] 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 

### Return type

[**ChunkUploadResponse**](ChunkUploadResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

