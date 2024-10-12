# NeutrinoApi.ImagingApi

All URIs are relative to *https://neutrinoapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hTMLRender**](ImagingApi.md#hTMLRender) | **POST** /html-render | HTML Render
[**imageResize**](ImagingApi.md#imageResize) | **POST** /image-resize | Image Resize
[**imageWatermark**](ImagingApi.md#imageWatermark) | **POST** /image-watermark | Image Watermark
[**qRCode**](ImagingApi.md#qRCode) | **POST** /qr-code | QR Code



## hTMLRender

> File hTMLRender(content, opts)

HTML Render

Render HTML content to PDF, JPG or PNG

### Example

```javascript
import NeutrinoApi from 'neutrino_api';
let defaultClient = NeutrinoApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: user-id
let user-id = defaultClient.authentications['user-id'];
user-id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user-id.apiKeyPrefix = 'Token';

let apiInstance = new NeutrinoApi.ImagingApi();
let content = "content_example"; // String | The HTML content. This can be either a URL to load from, a file upload (multipart/form-data) or an HTML content string
let opts = {
  'css': "css_example", // String | Inject custom CSS into the HTML. e.g. 'body { background-color: red;}'
  'delay': 0, // Number | Number of seconds to wait before rendering the page (can be useful for pages with animations etc)
  'footer': "footer_example", // String | The footer HTML to insert into each page. The following dynamic tags are supported: {date}, {title}, {url}, {pageNumber}, {totalPages}
  'format': "'PDF'", // String | Which format to output, available options are: PDF, PNG, JPG
  'grayscale': false, // Boolean | Render the final document in grayscale
  'header': "header_example", // String | The header HTML to insert into each page. The following dynamic tags are supported: {date}, {title}, {url}, {pageNumber}, {totalPages}
  'ignoreCertificateErrors': false, // Boolean | Ignore any TLS/SSL certificate errors
  'imageHeight': 56, // Number | If rendering to an image format (PNG or JPG) use this image height (in pixels). The default is automatic which dynamically sets the image height based on the content
  'imageWidth': 1024, // Number | If rendering to an image format (PNG or JPG) use this image width (in pixels)
  'landscape': false, // Boolean | Set the document to landscape orientation
  'margin': 0, // Number | The document margin (in mm)
  'marginBottom': 0, // Number | The document bottom margin (in mm)
  'marginLeft': 0, // Number | The document left margin (in mm)
  'marginRight': 0, // Number | The document right margin (in mm)
  'marginTop': 0, // Number | The document top margin (in mm)
  'pageHeight': 3.4, // Number | Set the PDF page height explicitly (in mm)
  'pageSize': "'A4'", // String | Set the document page size, can be one of: A0 - A9, B0 - B10, Comm10E, DLE or Letter
  'pageWidth': 3.4, // Number | Set the PDF page width explicitly (in mm)
  'timeout': 300, // Number | Timeout in seconds. Give up if still trying to load the HTML content after this number of seconds
  'title': "title_example", // String | The document title
  'zoom': 1 // Number | Set the zoom factor when rendering the page (2.0 for double size, 0.5 for half size)
};
apiInstance.hTMLRender(content, opts, (error, data, response) => {
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
 **content** | **String**| The HTML content. This can be either a URL to load from, a file upload (multipart/form-data) or an HTML content string | 
 **css** | **String**| Inject custom CSS into the HTML. e.g. &#39;body { background-color: red;}&#39; | [optional] 
 **delay** | **Number**| Number of seconds to wait before rendering the page (can be useful for pages with animations etc) | [optional] [default to 0]
 **footer** | **String**| The footer HTML to insert into each page. The following dynamic tags are supported: {date}, {title}, {url}, {pageNumber}, {totalPages} | [optional] 
 **format** | **String**| Which format to output, available options are: PDF, PNG, JPG | [optional] [default to &#39;PDF&#39;]
 **grayscale** | **Boolean**| Render the final document in grayscale | [optional] [default to false]
 **header** | **String**| The header HTML to insert into each page. The following dynamic tags are supported: {date}, {title}, {url}, {pageNumber}, {totalPages} | [optional] 
 **ignoreCertificateErrors** | **Boolean**| Ignore any TLS/SSL certificate errors | [optional] [default to false]
 **imageHeight** | **Number**| If rendering to an image format (PNG or JPG) use this image height (in pixels). The default is automatic which dynamically sets the image height based on the content | [optional] 
 **imageWidth** | **Number**| If rendering to an image format (PNG or JPG) use this image width (in pixels) | [optional] [default to 1024]
 **landscape** | **Boolean**| Set the document to landscape orientation | [optional] [default to false]
 **margin** | **Number**| The document margin (in mm) | [optional] [default to 0]
 **marginBottom** | **Number**| The document bottom margin (in mm) | [optional] [default to 0]
 **marginLeft** | **Number**| The document left margin (in mm) | [optional] [default to 0]
 **marginRight** | **Number**| The document right margin (in mm) | [optional] [default to 0]
 **marginTop** | **Number**| The document top margin (in mm) | [optional] [default to 0]
 **pageHeight** | **Number**| Set the PDF page height explicitly (in mm) | [optional] 
 **pageSize** | **String**| Set the document page size, can be one of: A0 - A9, B0 - B10, Comm10E, DLE or Letter | [optional] [default to &#39;A4&#39;]
 **pageWidth** | **Number**| Set the PDF page width explicitly (in mm) | [optional] 
 **timeout** | **Number**| Timeout in seconds. Give up if still trying to load the HTML content after this number of seconds | [optional] [default to 300]
 **title** | **String**| The document title | [optional] 
 **zoom** | **Number**| Set the zoom factor when rendering the page (2.0 for double size, 0.5 for half size) | [optional] [default to 1]

### Return type

**File**

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## imageResize

> File imageResize(imageUrl, width, opts)

Image Resize

Resize an image and output as either JPEG or PNG

### Example

```javascript
import NeutrinoApi from 'neutrino_api';
let defaultClient = NeutrinoApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: user-id
let user-id = defaultClient.authentications['user-id'];
user-id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user-id.apiKeyPrefix = 'Token';

let apiInstance = new NeutrinoApi.ImagingApi();
let imageUrl = "imageUrl_example"; // String | The URL or Base64 encoded Data URL for the source image. You can also upload an image file directly using multipart/form-data
let width = 56; // Number | The width to resize to (in px)
let opts = {
  'bgColor': "'transparent'", // String | The image background color in hexadecimal notation (e.g. #0000ff). For PNG output the special value of 'transparent' can also be used. For JPG output the default is black (#000000)
  'format': "'png'", // String | The output image format, can be either png or jpg
  'height': 56, // Number | The height to resize to (in px). If you don't set this field then the height will be automatic based on the requested width and image aspect ratio
  'resizeMode': "'scale'" // String | The resize mode to use, we support 3 main resizing modes: <ul> <li><b>scale</b><br>Resize to within the width and height specified while preserving aspect ratio. In this mode the width or height will be automatically adjusted to fit the aspect ratio</li> <li><b>pad</b><br>Resize to exactly the width and height specified while preserving aspect ratio and pad any space left over. Any padded space will be filled in with the 'bg-color' value</li> <li><b>crop</b><br>Resize to exactly the width and height specified while preserving aspect ratio and crop any space which fall outside the area. The cropping window is centered on the original image</li> </ul>
};
apiInstance.imageResize(imageUrl, width, opts, (error, data, response) => {
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
 **imageUrl** | **String**| The URL or Base64 encoded Data URL for the source image. You can also upload an image file directly using multipart/form-data | 
 **width** | **Number**| The width to resize to (in px) | 
 **bgColor** | **String**| The image background color in hexadecimal notation (e.g. #0000ff). For PNG output the special value of &#39;transparent&#39; can also be used. For JPG output the default is black (#000000) | [optional] [default to &#39;transparent&#39;]
 **format** | **String**| The output image format, can be either png or jpg | [optional] [default to &#39;png&#39;]
 **height** | **Number**| The height to resize to (in px). If you don&#39;t set this field then the height will be automatic based on the requested width and image aspect ratio | [optional] 
 **resizeMode** | **String**| The resize mode to use, we support 3 main resizing modes: &lt;ul&gt; &lt;li&gt;&lt;b&gt;scale&lt;/b&gt;&lt;br&gt;Resize to within the width and height specified while preserving aspect ratio. In this mode the width or height will be automatically adjusted to fit the aspect ratio&lt;/li&gt; &lt;li&gt;&lt;b&gt;pad&lt;/b&gt;&lt;br&gt;Resize to exactly the width and height specified while preserving aspect ratio and pad any space left over. Any padded space will be filled in with the &#39;bg-color&#39; value&lt;/li&gt; &lt;li&gt;&lt;b&gt;crop&lt;/b&gt;&lt;br&gt;Resize to exactly the width and height specified while preserving aspect ratio and crop any space which fall outside the area. The cropping window is centered on the original image&lt;/li&gt; &lt;/ul&gt; | [optional] [default to &#39;scale&#39;]

### Return type

**File**

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## imageWatermark

> File imageWatermark(imageUrl, watermarkUrl, opts)

Image Watermark

Watermark one image with another image

### Example

```javascript
import NeutrinoApi from 'neutrino_api';
let defaultClient = NeutrinoApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: user-id
let user-id = defaultClient.authentications['user-id'];
user-id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user-id.apiKeyPrefix = 'Token';

let apiInstance = new NeutrinoApi.ImagingApi();
let imageUrl = "imageUrl_example"; // String | The URL or Base64 encoded Data URL for the source image. You can also upload an image file directly using multipart/form-data
let watermarkUrl = "watermarkUrl_example"; // String | The URL or Base64 encoded Data URL for the watermark image. You can also upload an image file directly using multipart/form-data
let opts = {
  'bgColor': "'transparent'", // String | The image background color in hexadecimal notation (e.g. #0000ff). For PNG output the special value of 'transparent' can also be used. For JPG output the default is black (#000000)
  'format': "'png'", // String | The output image format, can be either png or jpg
  'height': 56, // Number | If set resize the resulting image to this height (in px)
  'opacity': 50, // Number | The opacity of the watermark (0 to 100)
  'position': "'center'", // String | The position of the watermark image, possible values are: <br>center, top-left, top-center, top-right, bottom-left, bottom-center, bottom-right
  'resizeMode': "'scale'", // String | The resize mode to use, we support 3 main resizing modes: <ul> <li><b>scale</b><br>Resize to within the width and height specified while preserving aspect ratio. In this mode the width or height will be automatically adjusted to fit the aspect ratio</li> <li><b>pad</b><br>Resize to exactly the width and height specified while preserving aspect ratio and pad any space left over. Any padded space will be filled in with the 'bg-color' value</li> <li><b>crop</b><br>Resize to exactly the width and height specified while preserving aspect ratio and crop any space which fall outside the area. The cropping window is centered on the original image</li> </ul>
  'width': 56 // Number | If set resize the resulting image to this width (in px)
};
apiInstance.imageWatermark(imageUrl, watermarkUrl, opts, (error, data, response) => {
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
 **imageUrl** | **String**| The URL or Base64 encoded Data URL for the source image. You can also upload an image file directly using multipart/form-data | 
 **watermarkUrl** | **String**| The URL or Base64 encoded Data URL for the watermark image. You can also upload an image file directly using multipart/form-data | 
 **bgColor** | **String**| The image background color in hexadecimal notation (e.g. #0000ff). For PNG output the special value of &#39;transparent&#39; can also be used. For JPG output the default is black (#000000) | [optional] [default to &#39;transparent&#39;]
 **format** | **String**| The output image format, can be either png or jpg | [optional] [default to &#39;png&#39;]
 **height** | **Number**| If set resize the resulting image to this height (in px) | [optional] 
 **opacity** | **Number**| The opacity of the watermark (0 to 100) | [optional] [default to 50]
 **position** | **String**| The position of the watermark image, possible values are: &lt;br&gt;center, top-left, top-center, top-right, bottom-left, bottom-center, bottom-right | [optional] [default to &#39;center&#39;]
 **resizeMode** | **String**| The resize mode to use, we support 3 main resizing modes: &lt;ul&gt; &lt;li&gt;&lt;b&gt;scale&lt;/b&gt;&lt;br&gt;Resize to within the width and height specified while preserving aspect ratio. In this mode the width or height will be automatically adjusted to fit the aspect ratio&lt;/li&gt; &lt;li&gt;&lt;b&gt;pad&lt;/b&gt;&lt;br&gt;Resize to exactly the width and height specified while preserving aspect ratio and pad any space left over. Any padded space will be filled in with the &#39;bg-color&#39; value&lt;/li&gt; &lt;li&gt;&lt;b&gt;crop&lt;/b&gt;&lt;br&gt;Resize to exactly the width and height specified while preserving aspect ratio and crop any space which fall outside the area. The cropping window is centered on the original image&lt;/li&gt; &lt;/ul&gt; | [optional] [default to &#39;scale&#39;]
 **width** | **Number**| If set resize the resulting image to this width (in px) | [optional] 

### Return type

**File**

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## qRCode

> File qRCode(content, opts)

QR Code

Generate a QR code as a PNG image

### Example

```javascript
import NeutrinoApi from 'neutrino_api';
let defaultClient = NeutrinoApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: user-id
let user-id = defaultClient.authentications['user-id'];
user-id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user-id.apiKeyPrefix = 'Token';

let apiInstance = new NeutrinoApi.ImagingApi();
let content = "content_example"; // String | The content to encode into the QR code (e.g. a URL or a phone number)
let opts = {
  'bgColor': "'#ffffff'", // String | The QR code background color
  'fgColor': "'#000000'", // String | The QR code foreground color
  'height': 256, // Number | The height of the QR code (in px)
  'width': 256 // Number | The width of the QR code (in px)
};
apiInstance.qRCode(content, opts, (error, data, response) => {
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
 **content** | **String**| The content to encode into the QR code (e.g. a URL or a phone number) | 
 **bgColor** | **String**| The QR code background color | [optional] [default to &#39;#ffffff&#39;]
 **fgColor** | **String**| The QR code foreground color | [optional] [default to &#39;#000000&#39;]
 **height** | **Number**| The height of the QR code (in px) | [optional] [default to 256]
 **width** | **Number**| The width of the QR code (in px) | [optional] [default to 256]

### Return type

**File**

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

