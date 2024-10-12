# BrowshotApi.ScreenshotApi

All URIs are relative to *https://api.browshot.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createMultipleScreenshots**](ScreenshotApi.md#createMultipleScreenshots) | **GET** /screenshot/multiple | Request multiple screenshots
[**createScreenshot**](ScreenshotApi.md#createScreenshot) | **GET** /screenshot/create | Request a screenshot
[**deleteScreenshot**](ScreenshotApi.md#deleteScreenshot) | **GET** /screenshot/delete | Delete screenshot data
[**getHTML**](ScreenshotApi.md#getHTML) | **GET** /screenshot/html | Get the HTML code
[**getMultipleScreenshotsInfo**](ScreenshotApi.md#getMultipleScreenshotsInfo) | **GET** /screenshot/list | Get information about screenshots
[**getScreenshotInfo**](ScreenshotApi.md#getScreenshotInfo) | **GET** /screenshot/info | Query screenshot status
[**getThumbnail**](ScreenshotApi.md#getThumbnail) | **GET** /screenshot/thumbnail | Retrieve a thumbnail image
[**hostScreenshot**](ScreenshotApi.md#hostScreenshot) | **GET** /screenshot/host | Host thumbnails on your own S3 account or on Browshot.
[**searchScreenshot**](ScreenshotApi.md#searchScreenshot) | **GET** /screenshot/search | Search for screenshots
[**shareScreenshot**](ScreenshotApi.md#shareScreenshot) | **GET** /screenshot/share | Share a screenshot



## createMultipleScreenshots

> ScreenshotList createMultipleScreenshots(url, instanceId, opts)

Request multiple screenshots

Request multiple screenshots in one API call. The API call accepts all the parameters supported by screenshot/create. You can specify up to 10 URLs and 10 instances for a total of 100 screenshots in one API call. 

### Example

```javascript
import BrowshotApi from 'browshot_api';
let defaultClient = BrowshotApi.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';

let apiInstance = new BrowshotApi.ScreenshotApi();
let url = "url_example"; // String | URL of the page to get a screenshot for. You can specify multiple url parameters (up to 10).
let instanceId = 56; // Number | instance ID to use. You can specify multiple instance_id parameters (up to 10).
let opts = {
  'size': "'screen'", // String | screenshot size - \"screen\" (default) or \"page\"
  'cache': 86400, // Number | use a previous screenshot (same URL, same instance) if it was done within <cache_value> seconds. The default value is 24hours. Specify cache=0 if you want a new screenshot.
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
  'hosting': "hosting_example", // String | hosting option - s3 or browshot
  'hostingHeight': 56, // Number | maximum height of the thumbnail to host
  'hostingWidth': 56, // Number | maximum height of the thumbnail to host
  'hostingScale': 1.0, // Number | scale of the thumbnail to host
  'hostingBucket': "hostingBucket_example", // String | S3 bucket to upload the screenshot or thumbnail (required for S3)
  'hostingFile': "hostingFile_example", // String | file name to use (for S3 only)
  'hostingHeaders': "hostingHeaders_example" // String | list of headers to add to the S3 object (for S3 only)
};
apiInstance.createMultipleScreenshots(url, instanceId, opts, (error, data, response) => {
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
 **url** | **String**| URL of the page to get a screenshot for. You can specify multiple url parameters (up to 10). | 
 **instanceId** | **Number**| instance ID to use. You can specify multiple instance_id parameters (up to 10). | 
 **size** | **String**| screenshot size - \&quot;screen\&quot; (default) or \&quot;page\&quot; | [optional] [default to &#39;screen&#39;]
 **cache** | **Number**| use a previous screenshot (same URL, same instance) if it was done within &lt;cache_value&gt; seconds. The default value is 24hours. Specify cache&#x3D;0 if you want a new screenshot. | [optional] [default to 86400]
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
 **hosting** | **String**| hosting option - s3 or browshot | [optional] 
 **hostingHeight** | **Number**| maximum height of the thumbnail to host | [optional] 
 **hostingWidth** | **Number**| maximum height of the thumbnail to host | [optional] 
 **hostingScale** | **Number**| scale of the thumbnail to host | [optional] [default to 1.0]
 **hostingBucket** | **String**| S3 bucket to upload the screenshot or thumbnail (required for S3) | [optional] 
 **hostingFile** | **String**| file name to use (for S3 only) | [optional] 
 **hostingHeaders** | **String**| list of headers to add to the S3 object (for S3 only) | [optional] 

### Return type

[**ScreenshotList**](ScreenshotList.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createScreenshot

> Screenshot createScreenshot(url, instanceId, opts)

Request a screenshot

Screenshots requests to private and shared instances require a positive balance.  *IMPORTANT*: Remember that you can only do 100 free screenshots per month. To used a premium instance, use instance_id&#x3D;65 for example. 

### Example

```javascript
import BrowshotApi from 'browshot_api';
let defaultClient = BrowshotApi.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';

let apiInstance = new BrowshotApi.ScreenshotApi();
let url = "url_example"; // String | URL of the page to get a screenshot for
let instanceId = 56; // Number | instance ID to use
let opts = {
  'size': "'screen'", // String | screenshot size - \"screen\" (default) or \"page\"
  'cache': 86400, // Number | use a previous screenshot (same URL, same instance) if it was done within <cache_value> seconds. The default value is 24hours. Specify cache=0 if you want a new screenshot.
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
  'shots': 1, // Number | take multiple screenshots of the same page. This costs 1 additional credit for every 2 additional screenshots.
  'shotInterval': 5, // Number | number of seconds between 2 screenshots
  'hosting': "hosting_example", // String | hosting option - s3 or browshot
  'hostingHeight': 56, // Number | maximum height of the thumbnail to host
  'hostingWidth': 56, // Number | maximum height of the thumbnail to host
  'hostingScale': 1.0, // Number | scale of the thumbnail to host
  'hostingBucket': "hostingBucket_example", // String | S3 bucket to upload the screenshot or thumbnail (required for S3)
  'hostingFile': "hostingFile_example", // String | file name to use (for S3 only)
  'hostingHeaders': "hostingHeaders_example" // String | list of headers to add to the S3 object (for S3 only)
};
apiInstance.createScreenshot(url, instanceId, opts, (error, data, response) => {
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
 **url** | **String**| URL of the page to get a screenshot for | 
 **instanceId** | **Number**| instance ID to use | 
 **size** | **String**| screenshot size - \&quot;screen\&quot; (default) or \&quot;page\&quot; | [optional] [default to &#39;screen&#39;]
 **cache** | **Number**| use a previous screenshot (same URL, same instance) if it was done within &lt;cache_value&gt; seconds. The default value is 24hours. Specify cache&#x3D;0 if you want a new screenshot. | [optional] [default to 86400]
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
 **shots** | **Number**| take multiple screenshots of the same page. This costs 1 additional credit for every 2 additional screenshots. | [optional] [default to 1]
 **shotInterval** | **Number**| number of seconds between 2 screenshots | [optional] [default to 5]
 **hosting** | **String**| hosting option - s3 or browshot | [optional] 
 **hostingHeight** | **Number**| maximum height of the thumbnail to host | [optional] 
 **hostingWidth** | **Number**| maximum height of the thumbnail to host | [optional] 
 **hostingScale** | **Number**| scale of the thumbnail to host | [optional] [default to 1.0]
 **hostingBucket** | **String**| S3 bucket to upload the screenshot or thumbnail (required for S3) | [optional] 
 **hostingFile** | **String**| file name to use (for S3 only) | [optional] 
 **hostingHeaders** | **String**| list of headers to add to the S3 object (for S3 only) | [optional] 

### Return type

[**Screenshot**](Screenshot.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteScreenshot

> [ScreenshotShort] deleteScreenshot(id, opts)

Delete screenshot data

You can delete details of your screenshots to remove any confidential information. 

### Example

```javascript
import BrowshotApi from 'browshot_api';
let defaultClient = BrowshotApi.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';

let apiInstance = new BrowshotApi.ScreenshotApi();
let id = 56; // Number | screenshot ID
let opts = {
  'data': "'image'" // String | data to remove. You can specify multiple of them (separated by a ,): *image* (image files), *url* (url requested), *metadata* (time added, time finished, post data, cookie and referer used for the screenshot), *all* (all data and files) 
};
apiInstance.deleteScreenshot(id, opts, (error, data, response) => {
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
 **id** | **Number**| screenshot ID | 
 **data** | **String**| data to remove. You can specify multiple of them (separated by a ,): *image* (image files), *url* (url requested), *metadata* (time added, time finished, post data, cookie and referer used for the screenshot), *all* (all data and files)  | [optional] [default to &#39;image&#39;]

### Return type

[**[ScreenshotShort]**](ScreenshotShort.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getHTML

> getHTML(id)

Get the HTML code

Retrieve the HTML code of the rendered page. This API call should be used when html&#x3D;1 was specified in the screenshot request. 

### Example

```javascript
import BrowshotApi from 'browshot_api';
let defaultClient = BrowshotApi.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';

let apiInstance = new BrowshotApi.ScreenshotApi();
let id = 56; // Number | screenshot ID
apiInstance.getHTML(id, (error, data, response) => {
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
 **id** | **Number**| screenshot ID | 

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getMultipleScreenshotsInfo

> [ScreenshotList] getMultipleScreenshotsInfo(opts)

Get information about screenshots

Get information about the last 100 screenshots requested.

### Example

```javascript
import BrowshotApi from 'browshot_api';
let defaultClient = BrowshotApi.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';

let apiInstance = new BrowshotApi.ScreenshotApi();
let opts = {
  'limit': 100, // Number | maximum number of screenshots' information to return
  'status': "status_example" // String | get list of screenshot in a given status (error, finished, in_process)
};
apiInstance.getMultipleScreenshotsInfo(opts, (error, data, response) => {
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
 **limit** | **Number**| maximum number of screenshots&#39; information to return | [optional] [default to 100]
 **status** | **String**| get list of screenshot in a given status (error, finished, in_process) | [optional] 

### Return type

[**[ScreenshotList]**](ScreenshotList.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getScreenshotInfo

> [Screenshot] getScreenshotInfo(id, opts)

Query screenshot status

Once a screenshot has been requested, its status must be checked until it is either \&quot;error\&quot; or \&quot;finished\&quot;.

### Example

```javascript
import BrowshotApi from 'browshot_api';
let defaultClient = BrowshotApi.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';

let apiInstance = new BrowshotApi.ScreenshotApi();
let id = 56; // Number | screenshot ID received from /api/v1/screenshot/create
let opts = {
  'details': 2 // Number | level of details about the screenshot and the page
};
apiInstance.getScreenshotInfo(id, opts, (error, data, response) => {
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
 **id** | **Number**| screenshot ID received from /api/v1/screenshot/create | 
 **details** | **Number**| level of details about the screenshot and the page | [optional] [default to 2]

### Return type

[**[Screenshot]**](Screenshot.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getThumbnail

> getThumbnail(id, opts)

Retrieve a thumbnail image

Unlike the other API calls, this API sends back the thumbnail as a PNG file, not JSON. The HTTP response code indicates whether the screenshot was successful (200), or incomplete (404) or failed (404). If the screenshot failed or is not finished, a default image \&quot;Not found\&quot; is sent.  You can crop your screenshots. The crop is done first, then the thumbnail. You can take a 1024x768 screenshot, crop it to 768x768, and get it scaled down to 300x300. 

### Example

```javascript
import BrowshotApi from 'browshot_api';
let defaultClient = BrowshotApi.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';

let apiInstance = new BrowshotApi.ScreenshotApi();
let id = 56; // Number | screenshot ID
let opts = {
  'width': 56, // Number | width of the thumbnail
  'height': 56, // Number | height of the thumbnail
  'scale': 1.0, // Number | scale of the thumbnail
  'zoom': 100, // Number | zoom 1 to 100 percent
  'ratio': "'fit'", // String | Use fit to keep the original page ration, and fill to get a thumbnail for the exact width and height.  specified. If you provide both width and height, you need to specify the ratio: fit to keep the original width/height ratio (the thumbnail might be smaller than the specified width and height), or fill to crop the image if necessary.
  'left': 0, // Number | left edge of the area to be cropped
  'right': 0, // Number | right edge of the area to be cropped
  'top': 0, // Number | top edge of the area to be cropped
  'bottom': 56, // Number | bottom edge of the area to be cropped
  'format': "'png'", // String | image as PNG or JPEG
  'shot': 1, // Number | get the second or third screenshot if multiple screenshots were requested
  'quality': 100 // Number | JPEG quality factor (for JPEG thumbnails only)
};
apiInstance.getThumbnail(id, opts, (error, data, response) => {
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
 **id** | **Number**| screenshot ID | 
 **width** | **Number**| width of the thumbnail | [optional] 
 **height** | **Number**| height of the thumbnail | [optional] 
 **scale** | **Number**| scale of the thumbnail | [optional] [default to 1.0]
 **zoom** | **Number**| zoom 1 to 100 percent | [optional] [default to 100]
 **ratio** | **String**| Use fit to keep the original page ration, and fill to get a thumbnail for the exact width and height.  specified. If you provide both width and height, you need to specify the ratio: fit to keep the original width/height ratio (the thumbnail might be smaller than the specified width and height), or fill to crop the image if necessary. | [optional] [default to &#39;fit&#39;]
 **left** | **Number**| left edge of the area to be cropped | [optional] [default to 0]
 **right** | **Number**| right edge of the area to be cropped | [optional] [default to 0]
 **top** | **Number**| top edge of the area to be cropped | [optional] [default to 0]
 **bottom** | **Number**| bottom edge of the area to be cropped | [optional] 
 **format** | **String**| image as PNG or JPEG | [optional] [default to &#39;png&#39;]
 **shot** | **Number**| get the second or third screenshot if multiple screenshots were requested | [optional] [default to 1]
 **quality** | **Number**| JPEG quality factor (for JPEG thumbnails only) | [optional] [default to 100]

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## hostScreenshot

> [ScreenshotHost] hostScreenshot(id, hosting, opts)

Host thumbnails on your own S3 account or on Browshot.

You can host screenshots and thumbnails on your own S3 account or on Browshot.

### Example

```javascript
import BrowshotApi from 'browshot_api';
let defaultClient = BrowshotApi.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';

let apiInstance = new BrowshotApi.ScreenshotApi();
let id = 56; // Number | screenshot ID
let hosting = "hosting_example"; // String | hosting option: s3 or browshot
let opts = {
  'width': 56, // Number | width of the thumbnail
  'height': 56, // Number | height of the thumbnail
  'scale': 1.0, // Number | scale of the thumbnail
  'bucket': "bucket_example", // String | S3 bucket to upload the screenshot or thumbnail - required with hosting=s3
  'file': "file_example", // String | file name to use - optional, used with hosting=s3
  'headers': "headers_example" // String | HTTP headers to add to your S3 object - optional, used with hosting=s3
};
apiInstance.hostScreenshot(id, hosting, opts, (error, data, response) => {
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
 **id** | **Number**| screenshot ID | 
 **hosting** | **String**| hosting option: s3 or browshot | 
 **width** | **Number**| width of the thumbnail | [optional] 
 **height** | **Number**| height of the thumbnail | [optional] 
 **scale** | **Number**| scale of the thumbnail | [optional] [default to 1.0]
 **bucket** | **String**| S3 bucket to upload the screenshot or thumbnail - required with hosting&#x3D;s3 | [optional] 
 **file** | **String**| file name to use - optional, used with hosting&#x3D;s3 | [optional] 
 **headers** | **String**| HTTP headers to add to your S3 object - optional, used with hosting&#x3D;s3 | [optional] 

### Return type

[**[ScreenshotHost]**](ScreenshotHost.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchScreenshot

> [ScreenshotList] searchScreenshot(url, opts)

Search for screenshots

Search for screenshots of a specific URL.

### Example

```javascript
import BrowshotApi from 'browshot_api';
let defaultClient = BrowshotApi.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';

let apiInstance = new BrowshotApi.ScreenshotApi();
let url = "url_example"; // String | look for a string matching the URL requested
let opts = {
  'limit': 50, // Number | maximum number of screenshots' information to return
  'status': "status_example" // String | get list of screenshot in a given status (error, finished, in_process)
};
apiInstance.searchScreenshot(url, opts, (error, data, response) => {
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
 **url** | **String**| look for a string matching the URL requested | 
 **limit** | **Number**| maximum number of screenshots&#39; information to return | [optional] [default to 50]
 **status** | **String**| get list of screenshot in a given status (error, finished, in_process) | [optional] 

### Return type

[**[ScreenshotList]**](ScreenshotList.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## shareScreenshot

> [ScreenshotHost] shareScreenshot(id, opts)

Share a screenshot

You can make your screenshots public, add notes, and share it with your friends and colleagues. Only screenshots which are successfully completed can be shared.n the thumbnail. You can take a 1024x768 screenshot, crop it to 768x768, and get it scaled down to 300x300. 

### Example

```javascript
import BrowshotApi from 'browshot_api';
let defaultClient = BrowshotApi.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';

let apiInstance = new BrowshotApi.ScreenshotApi();
let id = 56; // Number | screenshot ID
let opts = {
  'note': "note_example" // String | note to add on the sharing page
};
apiInstance.shareScreenshot(id, opts, (error, data, response) => {
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
 **id** | **Number**| screenshot ID | 
 **note** | **String**| note to add on the sharing page | [optional] 

### Return type

[**[ScreenshotHost]**](ScreenshotHost.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

