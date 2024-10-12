# BrowshotApi.BatchApi

All URIs are relative to *https://api.browshot.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createBatch**](BatchApi.md#createBatch) | **POST** /batch/ceate | Requests thousands of screenshtos at once
[**getBatchInfo**](BatchApi.md#getBatchInfo) | **GET** /batch/info | Get the batch status



## createBatch

> [Batch] createBatch(instanceId, opts)

Requests thousands of screenshtos at once

Get hundreds or thousands of screenshots from a text file. You can use this API call or the dashboard. Unlike the other API calls, you must issue a POST request with the Content-Type \&quot;multipart/form-data\&quot; in order to upload the text file. The text file must contain the list of URLs to request, 1 URL per line. Failed screenshots will be tried up to 3 times before giving up. 

### Example

```javascript
import BrowshotApi from 'browshot_api';
let defaultClient = BrowshotApi.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';

let apiInstance = new BrowshotApi.BatchApi();
let instanceId = 56; // Number | instance ID to use
let opts = {
  'hosting': "hosting_example", // String | hosting option - s3 or browshot
  'hostingHeight': 56, // Number | maximum height of the thumbnail to host
  'hostingWidth': 56, // Number | maximum height of the thumbnail to host
  'hostingScale': 1.0, // Number | scale of the thumbnail to host
  'hostingBucket': "hostingBucket_example", // String | S3 bucket to upload the screenshot or thumbnail (required for S3)
  'hostingFile': "hostingFile_example", // String | file name to use (for S3 only)
  'hostingHeaders': "hostingHeaders_example", // String | list of headers to add to the S3 object (for S3 only)
  'file': "/path/to/file", // File | text file to use
  'size': "'screen'", // String | screenshots size - \\\"screen\\\" (default) or \\\"page\\\"
  'name': "name_example", // String | name of the batch
  'width': 1024, // Number | thumbnail width.
  'height': 56, // Number | thumbnail height
  'delay': 5, // Number | number of seconds to wait after the page has loaded. This is used to let JavaScript run longer before taking the screenshot. Use delay=0 to take screenshots faster.
  'flashDelay': 10, // Number | number of seconds to wait after the page has loaded if Flash elements are present. Use flash_delay=0 to take screenshots faster.
  'screenWidth': 1024, // Number | width of the browser window. For desktop browsers only.
  'screenHeight': 768, // Number | height of the browser window. For desktop browsers only. (Note: full-page screenshots can have a height of up to 15,000px)
  'priority': 56, // Number | assign priority to the screenshot (for private instances only)
  'referer': "referer_example", // String | use a custom referrer header - paid screenshots only
  'postData': "postData_example", // String | send a POST requests with post_data, useful for filling out forms - paid screenshots only
  'cookie': "cookie_example", // String | set a cookie for the URL requested (see Custom POST Data, Referer and Cookie) Cookies should be separated by a ; - paid screenshots only
  'script': "script_example", // String | URL of javascript file to execute after the page load event
  'details': 2, // Number | level of information available with screenshot/info
  'html': 0, // Number | saves the HTML of the rendered page which can be retrieved by the API call screenshot/html. This feature costs *1 credit* per screenshot.
  'maxWait': 0, // Number | maximum number of seconds to wait before triggering the PageLoad event. Note that delay will still be used. (default: 0 = disabled)
  'headers': "headers_example", // String | any custom HTTP headers. (Not supported with Internet Explorer)
  'format': "'png'" // String | image as PNG or JPEG
};
apiInstance.createBatch(instanceId, opts, (error, data, response) => {
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
 **instanceId** | **Number**| instance ID to use | 
 **hosting** | **String**| hosting option - s3 or browshot | [optional] 
 **hostingHeight** | **Number**| maximum height of the thumbnail to host | [optional] 
 **hostingWidth** | **Number**| maximum height of the thumbnail to host | [optional] 
 **hostingScale** | **Number**| scale of the thumbnail to host | [optional] [default to 1.0]
 **hostingBucket** | **String**| S3 bucket to upload the screenshot or thumbnail (required for S3) | [optional] 
 **hostingFile** | **String**| file name to use (for S3 only) | [optional] 
 **hostingHeaders** | **String**| list of headers to add to the S3 object (for S3 only) | [optional] 
 **file** | **File**| text file to use | [optional] 
 **size** | **String**| screenshots size - \\\&quot;screen\\\&quot; (default) or \\\&quot;page\\\&quot; | [optional] [default to &#39;screen&#39;]
 **name** | **String**| name of the batch | [optional] 
 **width** | **Number**| thumbnail width. | [optional] [default to 1024]
 **height** | **Number**| thumbnail height | [optional] 
 **delay** | **Number**| number of seconds to wait after the page has loaded. This is used to let JavaScript run longer before taking the screenshot. Use delay&#x3D;0 to take screenshots faster. | [optional] [default to 5]
 **flashDelay** | **Number**| number of seconds to wait after the page has loaded if Flash elements are present. Use flash_delay&#x3D;0 to take screenshots faster. | [optional] [default to 10]
 **screenWidth** | **Number**| width of the browser window. For desktop browsers only. | [optional] [default to 1024]
 **screenHeight** | **Number**| height of the browser window. For desktop browsers only. (Note: full-page screenshots can have a height of up to 15,000px) | [optional] [default to 768]
 **priority** | **Number**| assign priority to the screenshot (for private instances only) | [optional] 
 **referer** | **String**| use a custom referrer header - paid screenshots only | [optional] 
 **postData** | **String**| send a POST requests with post_data, useful for filling out forms - paid screenshots only | [optional] 
 **cookie** | **String**| set a cookie for the URL requested (see Custom POST Data, Referer and Cookie) Cookies should be separated by a ; - paid screenshots only | [optional] 
 **script** | **String**| URL of javascript file to execute after the page load event | [optional] 
 **details** | **Number**| level of information available with screenshot/info | [optional] [default to 2]
 **html** | **Number**| saves the HTML of the rendered page which can be retrieved by the API call screenshot/html. This feature costs *1 credit* per screenshot. | [optional] [default to 0]
 **maxWait** | **Number**| maximum number of seconds to wait before triggering the PageLoad event. Note that delay will still be used. (default: 0 &#x3D; disabled) | [optional] [default to 0]
 **headers** | **String**| any custom HTTP headers. (Not supported with Internet Explorer) | [optional] 
 **format** | **String**| image as PNG or JPEG | [optional] [default to &#39;png&#39;]

### Return type

[**[Batch]**](Batch.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## getBatchInfo

> Batch getBatchInfo(id)

Get the batch status

Get the status of a batch requested through the API or through the dashboard. 

### Example

```javascript
import BrowshotApi from 'browshot_api';
let defaultClient = BrowshotApi.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';

let apiInstance = new BrowshotApi.BatchApi();
let id = 56; // Number | batch ID
apiInstance.getBatchInfo(id, (error, data, response) => {
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
 **id** | **Number**| batch ID | 

### Return type

[**Batch**](Batch.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

